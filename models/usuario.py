from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base

class Usuario(Base):
    __tablename__ = "tbl_rusuarios"
    usu_iid = Column(Integer, primary_key=True, index=True)
    usu_idni = Column(Integer, nullable=False)
    usu_vnombre = Column(String, nullable=False)
    usu_vusuario = Column(String, nullable=False, unique=True)
    usu_vcontrasena = Column(String, nullable=False)
    usu_vtoken = Column(String)
    usu_vtoken_refresh = Column(String)
    usu_dfecha_registro = Column(TIMESTAMP, nullable=False)
    usu_vrol = Column(String, nullable=False)
