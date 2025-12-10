from pydantic import BaseModel

class Lecturas_brutas(BaseModel):
    valor_co2: float
    valor_tvocs: float
    id_dispositivo: int
    fecha_hora: str 
