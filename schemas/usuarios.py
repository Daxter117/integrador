from pydantic import BaseModel

class Usuarios(BaseModel):
    id_usuario:int
    nombre:str
    correo:str
    contrasena:str