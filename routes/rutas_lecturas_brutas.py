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
    query = "SELECT crear_lectura(%s, %s, %s, %s);"
    valores = (lec.valor_co2, lec.valor_tvocs, lec.id_dispositivo, lec.fecha_hora)

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        connexion.commit()
        return {"message": "Lectura creada correctamente"}
    except Exception as err:
        return {"error": str(err)}

