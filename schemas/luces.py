from pydantic import BaseModel
from typing import Optional
 
class Luces(BaseModel):
    id_luz: int
    estado_luz: int
    modo_func: int
    hora_inicio: Optional[str] = None   # aceptar "08:00"
    hora_fin: Optional[str] = None      # aceptar "18:00"
    id_dispositivo: int
