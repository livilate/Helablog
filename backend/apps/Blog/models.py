import uuid
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field, HttpUrl


class Ingredient(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "name": "ingrediente 1",
            }
        }


class Gusto(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    ingredients: List[Ingredient] = []
    stars: int

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "name": "gusto 1",
                "ingredients": [
                    {
                        "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                        "name": "ingrediente 1",
                    }
                ],
                "stars": 5,
            }
        }


class Imagen(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    url: HttpUrl
    name: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "url": "http://holacomoandas.com",
                "name": "ingrediente 1",
            }
        }


class Comentario(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    text: str = Field(...)
    date: datetime = datetime.now()

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "name": "hola",
                "text": "hola como andas? Muy rico",
                "date": datetime.now(),
            }
        }


class Publicacion(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    text: str = Field(...)
    stars: int
    date: datetime = datetime.now()
    comentarios: Optional[List[Comentario]] = None
    gustos: Optional[List[Gusto]] = None
    images: Optional[List[Imagen]] = None

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "name": "Nombre Heladeria",
                "text": "El texto de la heladeria",
                "stars": 5,
                "date": datetime.now(),
                "comentarios": [
                    {
                        "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                        "name": "hola",
                        "text": "hola como andas? Muy rico",
                        "date": datetime.now(),
                    }
                ],
                "gustos": [
                    {
                        "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                        "name": "gusto 1",
                        "ingredients": [
                            {
                                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                                "name": "ingrediente 1",
                            }
                        ],
                        "stars": 5,
                    }
                ],
                "images": [
                    {
                        "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                        "url": "http://holacomoandas.com",
                        "name": "ingrediente 1",
                    }
                ],
            }
        }


class UpdatePublicacionModel(BaseModel):
    name: Optional[str]
    text: Optional[str]
    stars: Optional[int]
    images: Optional[List[Imagen]] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "My other important task",
                "text": "asdasdasdasdas",
                "stars": 5,
                "images": [
                    {
                        "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                        "url": "http://holacomoandas.com",
                        "name": "ingrediente 1",
                    }
                ],
            }
        }
