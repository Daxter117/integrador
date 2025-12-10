from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.rutas_dispositivos import rutadispositivos
from routes.rutas_lecturas_brutas import rutalecturas
from routes.rutas_usuarios import rutausuarios
from routes.rutaas_errores import rutaerrores
from routes.rutas_extractor import rutaextractores
from routes.rutas_luces import rutaluces

app = FastAPI()

# ==================================
#   C O R S   (NECESARIO PARA WEB)
# ==================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes reemplazar con tu dominio si quieres
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================================
#   R O U T E R S
# ==================================
app.include_router(rutaerrores)
app.include_router(rutadispositivos)
app.include_router(rutalecturas)       # ← aquí ya se incluye el router corregido
app.include_router(rutaextractores)
app.include_router(rutaluces)
app.include_router(rutausuarios)
