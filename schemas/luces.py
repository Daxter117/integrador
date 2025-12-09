from pydantic import BaseModel

class Luces(BaseModel):
    id:int
    id_luz:int
    estado:float
    modo:float
    hora_inicio:str
    hora_fin:str

    id_dispositivo:int
