from fastapi import APIRouter
from database.db import connexion
from schemas.dispositivos import Dispositivos

rutadispositivos = APIRouter()

# ======================================
#   OBTENER TODOS LOS DISPOSITIVOS
# ======================================
@rutadispositivos.get("/dispositivos")
def get_dispositivos():
    consulta = "SELECT * FROM vista_dispositivos;"
    try:
        cursor = connexion.cursor()
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        return resultado
    except Exception as err:
        print("Error:", err)
        return {"error": str(err)}


# ======================================
#   CREAR DISPOSITIVO
# ======================================
@rutadispositivos.post("/dispositivos")
def crear_dispositivo(dev: Dispositivos):
    query = f"""
        CALL crear_dispositivo(
            {dev.estado},
            {dev.modo_operacion},
            {dev.id_usuario}
        );
    """
    try:
        cursor = connexion.cursor()
        cursor.execute(query)
        connexion.commit()
        return {"message": "Dispositivo creado correctamente"}
    except Exception as err:
        print("Error:", err)
        return {"error": str(err)}


# ======================================
#   ACTUALIZAR DISPOSITIVO
# ======================================
@rutadispositivos.put("/dispositivos")
def actualizar_dispositivo(dev: Dispositivos):
    query = f"""
        CALL actualizar_dispositivo(
            {dev.id_dispositivo},
            {dev.estado},
            {dev.modo_operacion},
            {dev.id_usuario}
        );
    """
    try:
        cursor = connexion.cursor()
        cursor.execute(query)
        connexion.commit()
        return {"message": "Dispositivo actualizado correctamente"}
    except Exception as err:
        print("Error:", err)
        return {"error": str(err)}


# ======================================
#   ELIMINAR DISPOSITIVO
# ======================================
@rutadispositivos.delete("/dispositivos")
def eliminar_dispositivo(dev: Dispositivos):
    query = f"CALL eliminar_dispositivo({dev.id_dispositivo});"
    try:
        cursor = connexion.cursor()
        cursor.execute(query)
        connexion.commit()
        return {"message": 'Dispositivo eliminado correctamente'}
    except Exception as err:
        print("Error:", err)
        return {"error": str(err)}
