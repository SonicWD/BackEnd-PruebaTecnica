from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime
from typing import Optional

class TipoIdentificacion(str, Enum):
    dni = "DNI"
    nie = "NIE"
    pasaporte = "Pasaporte"

class ClienteCreate(BaseModel):
    nombre: str
    tipo_identificacion: TipoIdentificacion
    numero_identificacion: str
    correo: EmailStr
    edad: int
    telefono: str

    class Config:
        from_attributes = True

class ClienteResponse(BaseModel):
    id: int
    nombre: str
    tipo_identificacion: TipoIdentificacion
    numero_identificacion: str
    correo: EmailStr
    edad: int
    telefono: str
    fecha_creacion: datetime
    fecha_actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None
        }