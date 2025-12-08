from fastapi import FastAPI
from routes.rutas_dispositivos import rutadispositivos
from routes.rutas_lecturas_brutas import rutalecturas_brutas
from routes.rutas_usuarios import rutausuarios
from routes.rutaas_errores import rutaerrores
from routes.rutas_extractor import rutaextractores
from routes.rutas_luces import rutaluces

app = FastAPI()

app.include_router(rutaerrores)
app.include_router(rutadispositivos)
app.include_router(rutalecturas_brutas)
app.include_router(rutaextractores)
app.include_router(rutaluces)
app.include_router(rutausuarios)