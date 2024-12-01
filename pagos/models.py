from pydantic import BaseModel, Field, ConfigDict
from typing import List
from datetime import date
from database import PyObjectId

class Pago(BaseModel):
    monto: int = Field(...)
    fecha: str = Field(...)
    idColegio: int = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "monto": 100,
                "fecha": "2024-10-10",
                "idColegio": 1,
            }
        },
    )

class PagoOut(Pago):
    id: PyObjectId = Field(alias="_id", default=None, serialization_alias="id")
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "64b9f1f4f1d2b2a3c4e5f6a7",
                "monto": 100,
                "fecha": "2024-10-10",
                "idColegio": 1,
            }
        },
    )
    

class PagoCollection(BaseModel):
    # A collection of places
    pagos: List[PagoOut] = Field(...)