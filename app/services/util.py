from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import Integer
from pydantic import BaseModel
from typing import Any, Dict


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

def validate_non_negative_fields(model, data: dict):
    """
    Modeldeki Integer kolonların değerlerini kontrol eder.
    Negatif olan varsa ValueError fırlatır.
    """
    int_columns = [
        col.name for col in model.__table__.columns
        if isinstance(col.type, Integer)
    ]

    for col_name in int_columns:
        value = data.get(col_name)
        if value is not None and value < 0:
            raise ValueError(f"{col_name} cannot be negative. Given value: {value}")
        

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