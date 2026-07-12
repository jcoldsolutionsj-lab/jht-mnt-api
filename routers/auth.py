from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.usuario import Usuario
from passlib.context import CryptContext
from jose import jwt
from config import SECRET_KEY, ALGORITHM

router = APIRouter(prefix="/auth", tags=["auth"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/ping")
def ping():
    return {"auth": "ok"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.usu_vusuario == username).first()
    if not user or not pwd_context.verify(password, user.usu_vcontrasena):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = jwt.encode({"sub": user.usu_vusuario, "rol": user.usu_vrol}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
