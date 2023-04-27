from fastapi import FastAPI
from api.routes import auth, stock
from api.middlewares.logging import log_requests


app = FastAPI()

app.middleware("http")(log_requests)

# Rutas de la aplicación
app.include_router(auth.router, prefix="/auth", tags=["auth"])

app.include_router(stock.router, prefix="/stocks", tags=["stocks"])
