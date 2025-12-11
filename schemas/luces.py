from pydantic import BaseModel

class Luces(BaseModel):
    id_luz:int
    estado:int
    modo:int
    hora_inicio:str
    hora_fin:str
    id_dispositivo:int
