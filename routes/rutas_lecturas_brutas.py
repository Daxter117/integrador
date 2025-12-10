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
def crear_lectura(lec: Lecturas_brutas):
    query = """
        INSERT INTO lecturas (valor_co2, valor_tvocs, id_dispositivo, fecha_hora)
        VALUES (%s, %s, %s, %s)
        RETURNING id_lectura;
    """
    valores = (lec.valor_co2, lec.valor_tvocs, lec.id_dispositivo, lec.fecha_hora)

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        new_id = cursor.fetchone()[0]
        connexion.commit()
        return {"message": "Lectura creada correctamente", "id_lectura": new_id}
    except Exception as err:
        connexion.rollback()
        return {"error": str(err)}


