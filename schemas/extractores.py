from pydantic import BaseModel
from typing import Optional
 
class Extractores(BaseModel):
    id_extractor: int
    estado: int
    modo_func: int
    hora_inicio: Optional[str] = "00:00:00"   # aceptar formato HH:MM:SS
    hora_fin: Optional[str] = "00:00:00"
    umbral_co2: float
    id_dispositivo: int
