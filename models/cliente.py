from sqlalchemy import Column, Integer, String
from database import Base

class Cliente(Base):
    __tablename__ = "tbl_rlead"
    lea_iid = Column(Integer, primary_key=True, index=True)
    lea_vservicio = Column(String, nullable=False)
    lea_vnombre = Column(String, nullable=False)
    lea_vapellido = Column(String, nullable=False)
    lea_vcorreo = Column(String, nullable=False)
    lea_itelefono = Column(Integer, nullable=False)
    lea_vempresa = Column(String, nullable=False)

