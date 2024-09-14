from fastapi import FastAPI
from app.routes import router as main_router
from app.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://front-end-prueba-tecnica.vercel.app"],    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(main_router)
