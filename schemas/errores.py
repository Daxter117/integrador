from pydantic import BaseModel

class Errores(BaseModel):
    tipo_error:str
    mensaje:str
    fecha_hora:str
    id_dispositivo:int