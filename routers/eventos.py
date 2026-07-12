from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.evento import Evento

router = APIRouter(prefix="/eventos", tags=["eventos"])

@router.get("/ping")
def ping():
    return {"eventos": "ok"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def crear_evento(evento: dict, db: Session = Depends(get_db)):
    nuevo = Evento(**evento)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{id}")
def actualizar_evento(id: int, estado: str, db: Session = Depends(get_db)):
    evento = db.query(Evento).filter(Evento.eve_iid == id).first()
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    evento.eve_vestado = estado
    db.commit()
    return evento
