# API Tracking - Leads, Servicios y Eventos

Este proyecto es una **API REST** desarrollada con **FastAPI** y **PostgreSQL**, diseñada para gestionar clientes (leads), usuarios, servicios y eventos.  
La API está pensada para integrarse con un landing page y un gestor web independiente.

---

## 🚀 Tecnologías utilizadas

- **Lenguaje:** Python 3.10+
- **Framework:** FastAPI
- **Base de datos:** PostgreSQL
- **ORM:** SQLAlchemy
- **Autenticación:** JWT con `python-jose`
- **Encriptación de contraseñas:** Passlib (bcrypt)
- **Servidor de desarrollo:** Uvicorn

---

## 📦 Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tuusuario/tu-repo.git
   cd tu-repo
Crear entorno virtual:

bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Instalar dependencias:

bash
pip install -r requirements.txt
Configurar la conexión a la base de datos en config.py:

python
DATABASE_URL = "postgresql://usuario:password@host:puerto/db_tracking"
SECRET_KEY = "clave_super_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
▶️ Ejecución
Levantar el servidor con Uvicorn:

bash
uvicorn main:app --reload

Esto iniciará el servidor en:

API raíz: http://127.0.0.1:8000/

Documentación interactiva (Swagger): http://127.0.0.1:8000/docs (127.0.0.1 in Bing)

Documentación alternativa (ReDoc): http://127.0.0.1:8000/redoc (127.0.0.1 in Bing)

Endpoints principales
Clientes (Leads):

POST /clientes/ → Registrar un nuevo lead

GET /clientes/ → Listar leads registrados

Usuarios (Auth):

POST /auth/login → Login con usuario y contraseña, devuelve JWT

Servicios:

POST /servicios/ → Crear servicio

GET /servicios/ → Listar servicios

Eventos:

POST /eventos/ → Crear evento

PUT /eventos/{id} → Actualizar estado de evento




