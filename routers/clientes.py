from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.cliente import Cliente

router = APIRouter(prefix="/clientes", tags=["clientes"])

@router.get("/ping")
def ping():
    return {"clientes": "ok"}

@router.post("/")
def crear_cliente(cliente: dict, db: Session = Depends(get_db)):
    # Validaciones básicas
    if "@" not in cliente.get("lea_vcorreo", ""):
        raise HTTPException(status_code=400, detail="Correo inválido")
    if len(cliente.get("lea_vnombre", "")) < 2:
        raise HTTPException(status_code=400, detail="Nombre demasiado corto")

    nuevo = Cliente(**cliente)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"message": "Cliente registrado correctamente", "cliente": nuevo}
