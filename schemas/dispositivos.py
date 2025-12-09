from pydantic import BaseModel

class Dispositivos(BaseModel):
    id_dispositivo:int
    estado:str
    modo_operacion:str
    ip:str
    id_usuario:int
