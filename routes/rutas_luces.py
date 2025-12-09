from fastapi import APIRouter
from database.db import connexion
from schemas.luces import Luces

rutaluces = APIRouter()

# ======================================
#   GET LUCES
# ======================================
@rutaluces.get("/getluces")
def get_luces():
    try:
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM vista_luces;")
        return cursor.fetchall()
    except Exception as err:
        return {"error": str(err)}


# ======================================
#   CREAR LUZ
# ======================================
@rutaluces.post("/crearluz")
def crear_luz(luz: Luces):
    query = "SELECT crear_luz(%s, %s, %s);"
    valores = (luz.estado_luz, luz.modo_func, luz.id_dispositivo)

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        connexion.commit()
        return {"message": "Luz creada correctamente"}
    except Exception as err:
        return {"error": str(err)}


# ======================================
#   ACTUALIZAR LUZ
# ======================================
@rutaluces.put("/actualizarluz")
def actualizar_luz(luz: Luces):
    query = "SELECT actualizar_luz(%s, %s, %s, %s);"
    valores = (luz.id_luz, luz.estado_luz, luz.modo_func, luz.id_dispositivo)

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        connexion.commit()
        return {"message": "Luz actualizada correctamente"}
    except Exception as err:
        return {"error": str(err)}


# ======================================
#   ELIMINAR LUZ
# ======================================
@rutaluces.delete("/eliminarluz")
def eliminar_luz(luz: Luces):
    query = "SELECT eliminar_luz(%s);"
    valores = (luz.id_luz,)

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        connexion.commit()
        return {"message": "Luz eliminada correctamente"}
    except Exception as err:
        return {"error": str(err)}
