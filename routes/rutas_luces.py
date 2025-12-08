from fastapi import APIRouter
from database.db import connexion
from schemas.luces import Luces

rutaluces = APIRouter()


# ================================
#     GET LUCES
# ================================
@rutaluces.post("/getluces")
def get_luces():
    consulta = "SELECT * FROM vista_luces"
    try:
        sql = connexion.cursor()
        sql.execute(consulta)
        resultado = sql.fetchall()
        return resultado
    except Exception as err:
        print("----- Error:", err)
        return {"error": str(err)}


# ================================
#     INSERTAR LUZ
# ================================
@rutaluces.post("/insertluz")
def insert_luz(luz: Luces):
    consulta = f"""
    CALL crear_luz(
        '{luz.nombre_luz}',
        '{luz.estado}',
        '{luz.id_dispositivo}'
    );
    """
    try:
        sql = connexion.cursor()
        sql.execute(consulta)
        connexion.commit()
        return {"message": "1"}
    except Exception as e:
        print("----- Error:", e)
        return {"error": str(e)}


# ================================
#     ELIMINAR LUZ
# ================================
@rutaluces.post("/delluz")
def delete_luz(luz: Luces):
    consulta = f"CALL eliminar_luz('{luz.id_luz}');"
    try:
        sql = connexion.cursor()
        sql.execute(consulta)
        connexion.commit()
        return {"message": "1"}
    except Exception as e:
        print("----- Error:", e)
        return {"error": str(e)}


# ================================
#     ACTUALIZAR LUZ
# ================================
@rutaluces.post("/updateluz")
def update_luz(luz: Luces):
    consulta = f"""
    CALL actualizar_luz(
        '{luz.id_luz}',
        '{luz.nombre_luz}',
        '{luz.estado}',
        '{luz.id_dispositivo}'
    );
    """
    try:
        sql = connexion.cursor()
        sql.execute(consulta)
        connexion.commit()
        return {"message": "1"}
    except Exception as e:
        print("----- Error:", e)
        return {"error": str(e)}
