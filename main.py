from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, clientes, servicios, eventos
from database import Base, engine



import os

app = FastAPI(title="API Tracking")

# Configure CORS dynamically
env = os.getenv("ENVIRONMENT", "development")
if env == "production":
    allowed_origins_str = os.getenv("ALLOWED_ORIGINS", "")
    origins = [origin.strip() for origin in allowed_origins_str.split(",") if origin.strip()]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
else:
    # In development, allow any local or external IP/origin (supports multiple machines)
    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex="https?://.*",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(auth.router)
app.include_router(clientes.router)
app.include_router(servicios.router)
app.include_router(eventos.router)


@app.get("/")
def root():
    return {"message": "API Tracking funcionando correctamente"}