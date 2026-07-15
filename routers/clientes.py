from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.cliente import Cliente
from schemas.cliente import ClienteCreate

router = APIRouter(prefix="/clientes", tags=["clientes"])

@router.get("/ping")
def ping():
    return {"clientes": "ok"}

@router.post("/")
def crear_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    # Validaciones básicas
    if "@" not in cliente.lea_vcorreo:
        raise HTTPException(status_code=400, detail="Correo inválido")
    if len(cliente.lea_vnombre) < 2:
        raise HTTPException(status_code=400, detail="Nombre demasiado corto")

    nuevo = Cliente(**cliente.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"message": "Cliente registrado correctamente", "cliente": nuevo}
