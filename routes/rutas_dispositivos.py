from fastapi import APIRouter
from database.db import connexion
from schemas.dispositivos import Dispositivos

rutadispositivos = APIRouter()

# ======================================
#   OBTENER DISPOSITIVOS
# ======================================
@rutadispositivos.get("/getdispositivos")
def get_dispositivos():
    try:
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM vista_dispositivos;")
        return cursor.fetchall()
    except Exception as err:
        return {"error": str(err)}

# ======================================
#   CREAR DISPOSITIVO
# ======================================
@rutadispositivos.post("/creardispositivo")
def crear_dispositivo(dis: Dispositivos):
    query = "SELECT crear_dispositivo(%s, %s, %s, %s);"
    valores = (dis.estado, dis.modo_operacion, dis.id_usuario, dis.ip)

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        connexion.commit()
        return {"message": "Dispositivo creado correctamente"}
    except Exception as err:
        return {"error": str(err)}

# ======================================
#   ACTUALIZAR DISPOSITIVO
# ======================================
@rutadispositivos.put("/actualizardispositivo")
def actualizar_dispositivo(dis: Dispositivos):
    query = "SELECT actualizar_dispositivo(%s, %s, %s, %s, %s);"
    valores = (dis.id_dispositivo, dis.estado, dis.modo_operacion, dis.id_usuario, dis.ip)

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        connexion.commit()
        return {"message": "Dispositivo actualizado correctamente"}
    except Exception as err:
        return {"error": str(err)}

# ======================================
#   ELIMINAR DISPOSITIVO
# ======================================
@rutadispositivos.delete("/eliminardispositivo")
def eliminar_dispositivo(dis: Dispositivos):
    query = "SELECT eliminar_dispositivo(%s);"
    valores = (dis.id_dispositivo,)

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        connexion.commit()
        return {"message": "Dispositivo eliminado correctamente"}
    except Exception as err:
        return {"error": str(err)}
