from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from database import Base

class Evento(Base):
    __tablename__ = "tbl_revento"
    eve_iid = Column(Integer, primary_key=True, index=True)
    eve_vestado = Column(String, nullable=False)
    eve_vobservacion = Column(String, nullable=False)
    eve_dfecha_registro = Column(TIMESTAMP, nullable=False)
    ser_iid = Column(Integer, ForeignKey("tbl_hservicio.ser_iid"), nullable=False)
