from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from app.database import Base
import enum

class TipoIdentificacion(enum.Enum):
    DNI = "DNI"
    NIE = "NIE"
    Pasaporte = "Pasaporte"

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    tipo_identificacion = Column(Enum(TipoIdentificacion))
    numero_identificacion = Column(String, unique=True, index=True)
    correo = Column(String, unique=True, index=True)
    edad = Column(Integer)
    telefono = Column(String)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())