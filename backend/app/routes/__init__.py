from fastapi import FastAPI
from app.routes.auth_routes import router as auth_router

def register_routers(app: FastAPI):
    app.include_router(auth_router)