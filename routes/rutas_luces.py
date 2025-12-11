from fastapi import APIRouter
from database.db import connexion
from schemas.luces import Luces
 
rutaluces = APIRouter()
 
# ======================================
#   ACTUALIZAR LUZ
# ======================================
@rutaluces.put("/actualizar_luz")
def actualizar_luz(luz: Luces):
    query = """
        UPDATE luces
        SET estado_luz = %s,
            modo_func = COALESCE(%s, 0),
            id_dispositivo = COALESCE(%s, 0)
        WHERE id_luz = %s
        RETURNING id_luz;
    """
    valores = (
        luz.estado_luz,
        luz.modo_func,
        luz.id_dispositivo,
        luz.id_luz
    )
 
    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        updated_id = cursor.fetchone()[0]
        connexion.commit()
        return {
            "message": "Luz actualizada correctamente",
            "id_luz": updated_id,
            "estado_luz": luz.estado_luz
        }
    except Exception as err:
        connexion.rollback()
        return {"error": str(err)}
