from pydantic import BaseModel
from typing import Optional
 
class Luces(BaseModel):
    id_luz: int
    estado_luz: int
    modo_func: int
    hora_inicio: Optional[str] = "00:00:00"   # aceptar formato HH:MM:SS
    hora_fin: Optional[str] = "00:00:00"
    id_dispositivo: int
