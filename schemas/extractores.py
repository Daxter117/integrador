from pydantic import BaseModel

class extractores(BaseModel):
    id_extractor:int
    estado:int
    modo_func:int
    hora_ini:str
    hora_fin:str
    umbral:float
    id_dispositivo:int