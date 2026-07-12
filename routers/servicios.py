from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.servicio import Servicio

router = APIRouter(prefix="/servicios", tags=["servicios"])

@router.get("/ping")
def ping():
    return {"servicios": "ok"}

@router.post("/")
def crear_servicio(servicio: dict, db: Session = Depends(get_db)):
    nuevo = Servicio(**servicio)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"message": "Servicio creado correctamente", "servicio": nuevo}
