from fastapi import APIRouter
from database.db import connexion
from schemas.lecturas_brutas import Lecturas_brutas

rutalecturas = APIRouter()

# ======================================
#   OBTENER TODAS LAS LECTURAS
# ======================================
@rutalecturas.get("/lecturas")
def get_lecturas():
    consulta = "SELECT * FROM vista_lecturas_brutas;"
    try:
        cursor = connexion.cursor()
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        return resultado
    except Exception as err:
        print("Error:", err)
        return {"error": str(err)}


# ======================================
#   CREAR LECTURA
# ======================================
@rutalecturas.post("/lecturas")
def crear_lectura(lec: Lecturas_brutas):
    query = f"""
        CALL crear_lectura(
            {lec.valor_co2},
            {lec.valor_tvocs},
            {lec.id_dispositivo}
        );
    """
    try:
        cursor = connexion.cursor()
        cursor.execute(query)
        connexion.commit()
        return {"message": "Lectura creada correctamente"}
    except Exception as err:
        print("Error:", err)
        return {"error": str(err)}


# ======================================
#   ACTUALIZAR LECTURA
# ======================================
@rutalecturas.put("/lecturas")
def actualizar_lectura(lec: Lecturas_brutas):
    query = f"""
        CALL actualizar_lectura(
            {lec.id_lectura},
            {lec.valor_co2},
            {lec.valor_tvocs},
            {lec.id_dispositivo}
        );
    """
    try:
        cursor = connexion.cursor()
        cursor.execute(query)
        connexion.commit()
        return {"message": "Lectura actualizada correctamente"}
    except Exception as err:
        print("Error:", err)
        return {"error": str(err)}


# ======================================
#   ELIMINAR LECTURA
# ======================================
@rutalecturas.delete("/lecturas")
def eliminar_lectura(lec: Lecturas_brutas):
    query = f"CALL eliminar_lectura({lec.id_lectura});"
    try:
        cursor = connexion.cursor()
        cursor.execute(query)
        connexion.commit()
        return {"message": "Lectura eliminada correctamente"}
    except Exception as err:
        print("Error:", err)
        return {"error": str(err)}
