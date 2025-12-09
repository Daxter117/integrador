from fastapi import APIRouter
from database.db import connexion
from schemas.lecturas_brutas import Lecturas_brutas

rutalecturas = APIRouter()

# ======================================
#   OBTENER TODAS LAS LECTURAS
# ======================================
@rutalecturas.get("/getlecturas")
def get_lecturas():
    try:
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM vista_lecturas_brutas;")
        return cursor.fetchall()
    except Exception as err:
        return {"error": str(err)}


# ======================================
#   CREAR LECTURA
# ======================================
@rutalecturas.post("/crearlectura")
def crear_lectura(lec: Lecturas_brutas):
    query = "SELECT crear_lectura(%s, %s, %s);"
    valores = (lec.valor_co2, lec.valor_tvocs, lec.id_dispositivo)

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        connexion.commit()
        return {"message": "Lectura creada correctamente"}
    except Exception as err:
        return {"error": str(err)}


# ======================================
#   ACTUALIZAR LECTURA
# ======================================
@rutalecturas.put("/actualizarlectura")
def actualizar_lectura(lec: Lecturas_brutas):
    query = "SELECT actualizar_lectura(%s, %s, %s, %s);"
    valores = (lec.id_lectura, lec.valor_co2, lec.valor_tvocs, lec.id_dispositivo)

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        connexion.commit()
        return {"message": "Lectura actualizada correctamente"}
    except Exception as err:
        return {"error": str(err)}


# ======================================
#   ELIMINAR LECTURA
# ======================================
@rutalecturas.delete("/eliminarlectura")
def eliminar_lectura(lec: Lecturas_brutas):
    query = "SELECT eliminar_lectura(%s);"
    valores = (lec.id_lectura,)

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        connexion.commit()
        return {"message": "Lectura eliminada correctamente"}
    except Exception as err:
        return {"error": str(err)}
