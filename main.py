from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, clientes, servicios, eventos
from database import Base, engine



app = FastAPI(title="API Tracking")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all origins for development, you can restrict this in production
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