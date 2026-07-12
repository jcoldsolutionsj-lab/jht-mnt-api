from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base

class Servicio(Base):
    __tablename__ = "tbl_hservicio"
    ser_iid = Column(Integer, primary_key=True, index=True)
    ser_vcodigo_servicio = Column(String, nullable=False)
    ser_vorigen = Column(String, nullable=False)
    ser_vdestino = Column(String, nullable=False)
    ser_vremitente = Column(String, nullable=False)
    ser_vconsignado = Column(String, nullable=False)
    ser_vestado_pago = Column(String, nullable=False)
    ser_vplaca = Column(String)
    ser_dfecha_registro = Column(TIMESTAMP, nullable=False)
