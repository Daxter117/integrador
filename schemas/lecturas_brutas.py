from pydantic import BaseModel

class Lecturas_brutas(BaseModel):
    id_lectura:float
    valor_co2:float
    valor_tvocs:float
    fecha_hora:str