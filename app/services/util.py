from sqlalchemy.orm import Session, DeclarativeMeta
from sqlalchemy import DateTime
from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy import Integer
from pydantic import BaseModel
from typing import Any, Dict, List


def get_object_by_id(model, object_id: int, db: Session):
    # """
    # Verilen model tablosunda id'ye göre kayıt getirir.
    # Yoksa 404 hatası döner.
    # """
    obj = db.query(model).filter(model.id == object_id,
                                model.is_active == True).first()
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"{model.__name__} (ID: {object_id}) bulunamadı veya pasifleştirilmiş."
        )
    return obj

def validate_required_field(value):
    # """
    # Bir alanın boş olup olmadığını kontrol eder.
    # Eğer boşsa 400 hatası döner.
    # """
    if not value:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Area is required"
        )
    return value

#min değeri tutan fonksiyon default değer 
def validate_min_length(field_value: str, min_length: int = 2):
    if isinstance(field_value, str):  # sadece stringlerde kontrol yap
        if not field_value or len(field_value.strip()) < min_length:
            raise HTTPException(
                status_code=400,
                detail=f"Metinler en az {min_length} karakter uzunluğunda olmalı."
            )

def validate_list_not_empty(lst):
    # """
    # Liste boşsa HTTP 404 hatası fırlatır.
    # lst: sorgudan dönen liste :list ya da :dict vermediğin sürece ikisinde de çalışır
    # object_name: hata mesajında kullanılacak isim
    # """
    if not lst or len(lst) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No list found"
        )
    return lst

def ensure_dict(data: Any) -> Dict:
    # Verilen veriyi bir `dict`'e çevirir.
    # - Eğer Pydantic model ise: .model_dump() ile dict yapılır.
    # - Eğer zaten dict ise: olduğu gibi döner.
    # - Diğer tipler (int, list, vs.): 400 hatası fırlatır.
    
    if isinstance(data, dict):
        return data
    elif isinstance(data, BaseModel):
        return data.model_dump()
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Veri, bir sözlük (dict) veya Pydantic model olmalıdır. Alınan tip: {type(data).__name__}"
        )

def validate_non_negative_fields(model, data: dict):
    
    # """
    # Modeldeki Integer kolonların değerlerini kontrol eder.
    # Negatif olan varsa ValueError fırlatır.
    # """ 
    
    int_columns = [
        col.name for col in model.__table__.columns
        if isinstance(col.type, Integer) and not col.primary_key
    ]

    for col_name in int_columns:
        value = data.get(col_name)
        if value is not None and value < 0:
            raise HTTPException(
                status_code=400,
                detail=f"{col_name} alanı negatif olamaz. Değer: {value}"
            )
            



def validate_required_keys(model, data: dict):
    # """
    # Modeldeki `nullable=False` olan tüm alanların istekte mevcut ve boş olmayan olduğunu kontrol eder.
    # Eksikse 400 hatası fırlatır.
    
    # Args:
    #     data: Gelen veri (dict)
    #     model: SQLAlchemy modeli (örneğin: About_Contents, Device)
    # """
    # Sadece nullable=False olan kolonları al
    required_columns = [
        col.name for col in model.__table__.columns
        if col.nullable is False and not col.primary_key  # id gibi PK'leri hariç tut (isteğe bağlı)
    ]

    missing = []
    for field in required_columns:
        if field not in data:
            missing.append(field)
        elif data[field] is None:
            missing.append(field)
        elif isinstance(data[field], str) and data[field].strip() == "":
            missing.append(field)

    if missing:
        raise HTTPException(
            status_code=400,
            detail=f"Zorunlu alanlar eksik veya boş: {', '.join(missing)}"
        )

# YAVAŞ KALDIĞI İÇİN CRUD KATMANINDA KONTROL EDİLİOR
def validate_unique_field(
    model,
    data,
    exclude_id: int | None = None,
    db: Session = None
):
    # """
    # Belirtilen modelde bir alanın benzersizliğini kontrol eder.
    
    # Args:
    #     model: SQLAlchemy modeli (örn: User, Device, ChannelList)
    #     field_name: Benzersiz olmalı alan (örn: "email", "name", "channel_no")
    #     value: Kontrol edilecek değer
    #     exclude_id: Güncelleme sırasında kendi ID'sini hariç tutmak için (isteğe bağlı)
    #     db: Veritabanı oturumu

    # Raises:
    #     HTTPException: 400 - Bu değer zaten kullanılıyor
    
    
    # """
    
    if db is None:
        raise ValueError("db oturumu gereklidir")
    
    unique_columns = [
    col.name for col in model.__table__.columns
    if col.unique and not col.primary_key  # ✅ unique olanları al
    ]
    
    for unique_col in unique_columns:
        field_name = unique_col
        value = data.get(field_name)
        
        if value is None:
            continue  # None değerler benzersizlik kontrolü gerektirmez. 
                        # Bir değer unique olsa bile none olabilir. none ise zaten o değer yok demek eşsizliğini kontrol edecek değer yok. 
                        # Bu kodun işi boş yerleri değil unique olmasını kontrol ettiriyor.

        # Alan mevcut mu kontrol et
        if not hasattr(model, field_name):
            raise ValueError(f"{model.__name__} modelinde '{field_name}' alanı yok")

        query = db.query(model).filter(getattr(model, field_name) == value, model.is_active == True)

        # Güncelleme sırasında kendi ID'yi hariç tut
        if exclude_id is not None:
            query = query.filter(model.id != exclude_id)

        exists = query.first()

        if exists:
            field_readable = field_name.replace("_", " ").title()
            raise HTTPException(
                status_code=400,
                detail=f"{field_readable} '{value}' zaten kullanılıyor."
            )
            
#BASE MODEL ZATEN FORMAT KONTROLÜ YAPTIĞI İÇİN BU FONKSİYON GÖREVİNİ YERİNE GETİREMİYOR. AMA İLERDE GEREKİRSE KULLANILABİLİR.
def validate_datetime_fields(model,
    data: Dict,
    allow_none: bool = True
):
    # """
    # Belirtilen alanların datetime formatında olup olmadığını kontrol eder.
    
    # Args:
    #     data: Gelen veri (dict)
    #     datetime_fields: Kontrol edilecek alanların listesi (örn: ["add_time", "update_time"])
    #     allow_none: None değerlerine izin verilsin mi? (default: True)
    
    # Raises:
    #     HTTPException: 400 - Geçersiz tarih formatı
    # """
    
    datetime_fields = [
    col.name for col in model.__table__.columns
    if isinstance(col.type, DateTime)  # ✅ unique olanları al
    ]
    for field in datetime_fields:
        value = data.get(field)
        
        # None kontrolü
        if value is None:
            if not allow_none:
                raise HTTPException(
                    status_code=400,
                    detail=f"{field} alanı None olamaz."
                )
            continue  # None ve allow_none=True ise geçerli
        
        # Tip kontrolü: str veya datetime olmalı
        if isinstance(value, datetime):
            continue  # Zaten doğru tip
        
        if isinstance(value, str):
            try:
                # ISO format kontrolü (örn: "2025-08-28T10:30:00" veya "2025-08-28")
                datetime.fromisoformat(value.replace("Z", "+00:00"))
            except ValueError:
                raise HTTPException(
                    status_code=400,
                    detail=f"{field} alanı geçerli bir tarih formatında değil. ISO 8601 formatı kullanın. (Alınan değer: {value})"
                )
        else:
            raise HTTPException(
                status_code=400,
                detail=f"{field} alanı bir tarih (datetime) olmalıdır. (Alınan tip: {type(value).__name__})"
            )

# def validate_unique_field(
#     model,
#     field_name: str,
#     value,
#     exclude_id: int | None = None,
#     db: Session = None
# ):
#     """
#     Belirtilen modelde bir alanın benzersizliğini kontrol eder.
    
#     Args:
#         model: SQLAlchemy modeli (örn: User, Device, ChannelList)
#         field_name: Benzersiz olmalı alan (örn: "email", "name", "channel_no")
#         value: Kontrol edilecek değer
#         exclude_id: Güncelleme sırasında kendi ID'sini hariç tutmak için (isteğe bağlı)
#         db: Veritabanı oturumu

#     Raises:
#         HTTPException: 400 - Bu değer zaten kullanılıyor
#     """
#     if db is None:
#         raise ValueError("db oturumu gereklidir")

#     if value is None:
#         return  # None değerler benzersizlik kontrolü gerektirmez

#     # Alan mevcut mu kontrol et
#     if not hasattr(model, field_name):
#         raise ValueError(f"{model.__name__} modelinde '{field_name}' alanı yok")

#     # Sorguyu oluştur
#     query = db.query(model).filter(getattr(model, field_name) == value)

#     # Güncelleme sırasında kendi ID'yi hariç tut
#     if exclude_id is not None:
#         query = query.filter(model.id != exclude_id)

#     # Kayıt var mı?
#     exists = query.first()

#     if exists:
#         field_readable = field_name.replace("_", " ").title()
#         raise HTTPException(
#             status_code=400,
#             detail=f"{field_readable} '{value}' zaten kullanılıyor."
#         )