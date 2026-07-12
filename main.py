from fastapi import FastAPI
from routers import auth, clientes, servicios, eventos
from database import Base, engine



app = FastAPI(title="API Tracking")

app.include_router(auth.router)
app.include_router(clientes.router)
app.include_router(servicios.router)
app.include_router(eventos.router)


@app.get("/")
def root():
    return {"message": "API Tracking funcionando correctamente"}