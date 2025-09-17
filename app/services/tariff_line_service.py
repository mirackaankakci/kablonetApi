from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from app.crud.tariff_line_crud import (
    get_tariff_line_crud,
    get_tariff_line_by_id_crud,
    create_tariff_line_crud,
    update_tariff_line_crud,
    delete_tariff_line_crud,
)
from app.schemas.tariff_line_schema import TariffLineCreateRequest, TariffLineUpdateRequest
from app.db.models.TariffLine import TariffLine


class TariffLineService:
    
    @staticmethod
    def get_tariff_lines(db: Session):
        """Tüm tariff line'ları getir"""
        try:
            return get_tariff_line_crud(db)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Tariff lines getirilirken hata oluştu: {str(e)}"
            )

    @staticmethod
    def get_tariff_line_by_id(db: Session, tariff_line_id: int):
        """ID ile tariff line getir"""
        if tariff_line_id <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Geçersiz tariff line ID"
            )
            
        tariff_line = get_tariff_line_by_id_crud(db, tariff_line_id)
        if not tariff_line:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"ID {tariff_line_id} ile tariff line bulunamadı"
            )
        return tariff_line

    @staticmethod
    def create_tariff_line(db: Session, tariff_line_data: TariffLineCreateRequest):
        """Yeni tariff line oluştur"""
        
        # 1. Category ID kontrolü
        if not tariff_line_data.tariff_category_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Tariff category ID gerekli"
            )
            
        # 2. Order number kontrolü (eğer TariffLine'da order alanı varsa)
        if hasattr(tariff_line_data, 'order') and tariff_line_data.order is not None:
            if tariff_line_data.order < 0:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Order değeri negatif olamaz"
                )
        
        # 3. Duplicate kontrolü (aynı category'de aynı order)
        if hasattr(tariff_line_data, 'order') and tariff_line_data.order is not None:
            existing_lines = get_tariff_line_crud(db)
            for line in existing_lines:
                if (line.tariff_category_id == tariff_line_data.tariff_category_id and 
                    hasattr(line, 'order') and line.order == tariff_line_data.order):
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT,
                        detail=f"Bu kategoride {tariff_line_data.order} sırasında tariff line zaten mevcut"
                    )
        
        # 4. Data hazırlama
        try:
            # Pydantic model'den dict'e çevir
            payload = tariff_line_data.model_dump(exclude_unset=True)
            payload.pop("id", None)  # ID'yi kaldır (auto-generated)
            
            # 5. Database'e kaydet
            return create_tariff_line_crud(db, payload)
            
        except IntegrityError as e:
            db.rollback()
            if "foreign key" in str(e).lower():
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Geçersiz tariff category ID"
                )
            elif "unique" in str(e).lower():
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Bu tariff line zaten mevcut"
                )
            else:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Veritabanı hatası oluştu"
                )
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Tariff line oluşturulurken hata oluştu: {str(e)}"
            )

    @staticmethod
    def update_tariff_line(db: Session, tariff_line_id: int, tariff_line_data: TariffLineUpdateRequest):
        """Tariff line güncelle"""
        
        # 1. ID validasyonu
        if tariff_line_id <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Geçersiz tariff line ID"
            )
            
        # 2. Kayıt var mı kontrol et
        existing_line = get_tariff_line_by_id_crud(db, tariff_line_id)
        if not existing_line:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"ID {tariff_line_id} ile tariff line bulunamadı"
            )
            
        # 3. Order number kontrolü (eğer güncelleme varsa)
        if hasattr(tariff_line_data, 'order') and tariff_line_data.order is not None:
            if tariff_line_data.order < 0:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Order değeri negatif olamaz"
                )
                
        # 4. Duplicate kontrolü (eğer order değişiyorsa)
        if (hasattr(tariff_line_data, 'order') and tariff_line_data.order is not None and 
            hasattr(existing_line, 'order') and tariff_line_data.order != existing_line.order):
            
            existing_lines = get_tariff_line_crud(db)
            category_id = tariff_line_data.tariff_category_id or existing_line.tariff_category_id
            
            for line in existing_lines:
                if (line.id != tariff_line_id and 
                    line.tariff_category_id == category_id and
                    hasattr(line, 'order') and line.order == tariff_line_data.order):
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT,
                        detail=f"Bu kategoride {tariff_line_data.order} sırasında tariff line zaten mevcut"
                    )
        
        # 5. Data hazırlama ve güncelleme
        try:
            payload = tariff_line_data.model_dump(exclude_unset=True)
            payload.pop("id", None)
            
            return update_tariff_line_crud(db, tariff_line_id, payload)
            
        except IntegrityError as e:
            db.rollback()
            if "foreign key" in str(e).lower():
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Geçersiz tariff category ID"
                )
            else:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Veritabanı hatası oluştu"
                )
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Tariff line güncellenirken hata oluştu: {str(e)}"
            )

    @staticmethod
    def delete_tariff_line(db: Session, tariff_line_id: int):
        """Tariff line sil"""
        
        # 1. ID validasyonu
        if tariff_line_id <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Geçersiz tariff line ID"
            )
            
        # 2. Kayıt var mı kontrol et
        existing_line = get_tariff_line_by_id_crud(db, tariff_line_id)
        if not existing_line:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"ID {tariff_line_id} ile tariff line bulunamadı"
            )
            
        # 3. İlişkili kayıtlar var mı kontrol et (TariffCell vs.)
        # Bu kısımda business rule'lara göre kontrol yapılabilir
        
        try:
            return delete_tariff_line_crud(db, tariff_line_id)
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Bu tariff line başka kayıtlar tarafından kullanılıyor, silinemez"
            )
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Tariff line silinirken hata oluştu: {str(e)}"
            )
