from pydantic import BaseModel
from typing import Optional
 
class Extractores(BaseModel):
    id_extractor: int
    estado: int
    modo_func: int
    hora_inicio: Optional[str] = None   # aceptar "08:00"
    hora_fin: Optional[str] = None      # aceptar "18:00"
    umbral_co2: float
    id_dispositivo: int
