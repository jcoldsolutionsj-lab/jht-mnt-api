from pydantic import BaseModel, EmailStr

class ClienteCreate(BaseModel):
    lea_vservicio: str
    lea_vnombre: str
    lea_vapellido: str
    lea_vcorreo: EmailStr
    lea_itelefono: int
    lea_vempresa: str

    class Config:
        schema_extra = {
            "example": {
                "lea_vservicio": "Transporte",
                "lea_vnombre": "Carlos",
                "lea_vapellido": "Ramirez",
                "lea_vcorreo": "carlos.ramirez@example.com",
                "lea_itelefono": 987654321,
                "lea_vempresa": "Logistica SAC"
            }
        }
