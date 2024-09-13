from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Cliente
from app.schemas import ClienteCreate, ClienteResponse


router = APIRouter()


# Endpoint de saludo
@router.get("/")
def read_root():
    return {"Hello": "World"}


# Crear cliente
@router.post("/create_client", response_model=ClienteResponse)
def create_client(cliente: ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = db.query(Cliente).filter(
        (Cliente.numero_identificacion == cliente.numero_identificacion) |
        (Cliente.correo == cliente.correo)
    ).first()

    if db_cliente:
        raise HTTPException(
            status_code=400,
            detail="Client con ese número de identificación o correo ya exist")

    # Crear nuevo cliente
    nuevo_cliente = Cliente(
        nombre=cliente.nombre,
        tipo_identificacion=cliente.tipo_identificacion,
        numero_identificacion=cliente.numero_identificacion,
        correo=cliente.correo,
        edad=cliente.edad,
        telefono=cliente.telefono,
    )
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente


# Listar todos los clientes
@router.get("/list_clients", response_model=list[ClienteResponse])
def list_clients(db: Session = Depends(get_db)):
    clientes = db.query(Cliente).all()
    return clientes


# Actualizar cliente
@router.put("/update_client/{cliente_id}", response_model=ClienteResponse)
def update_client(cliente_id: int, cliente: ClienteCreate,
                  db: Session = Depends(get_db)):
    db_cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    # Verifica si otro cliente ya tiene ese número de identificación o correo
    existing_cliente = db.query(Cliente).filter(
        ((Cliente.numero_identificacion == cliente.numero_identificacion) |
         (Cliente.correo == cliente.correo)) &
        (Cliente.id != cliente_id)
    ).first()

    if existing_cliente:
        raise HTTPException(
            status_code=400,
            detail="Otro cliente ya tiene esa identificación o correo")

    # Actualiza los campos del cliente
    db_cliente.nombre = cliente.nombre
    db_cliente.tipo_identificacion = cliente.tipo_identificacion
    db_cliente.numero_identificacion = cliente.numero_identificacion
    db_cliente.correo = cliente.correo
    db_cliente.edad = cliente.edad
    db_cliente.telefono = cliente.telefono

    db.commit()
    db.refresh(db_cliente)
    return db_cliente


# Eliminar cliente
@router.delete("/delete_client/{cliente_id}", response_model=dict)
def delete_client(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    db.delete(db_cliente)
    db.commit()
    
    return {"message": f"Cliente con ID {cliente_id} eliminado exitosamente"}   