from fastapi import APIRouter
from database.db import connexion
from schemas.luces import Luces
 
rutaluces = APIRouter()
 
@rutaluces.put("/actualizar_luz")
def actualizar_luz(luz: Luces):
    query = """
        UPDATE luces
        SET estado_luz = %s,
            modo_func = %s,
            hora_inicio = %s,
            hora_fin = %s,
            id_dispositivo = %s
        WHERE id_luz = %s
        RETURNING id_luz;
    """
    valores = (
        luz.estado_luz,
        luz.modo_func,
        luz.hora_inicio,
        luz.hora_fin,
        luz.id_dispositivo,
        luz.id_luz
    )
    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        print("Valores recibidos:", valores)
        print("Filas afectadas:", cursor.rowcount)
        updated = cursor.fetchone()
        if updated is None:
            connexion.rollback()
            return {"error": "No se encontró el id_luz para actualizar"}
        connexion.commit()
        return {
            "message": "Luz actualizada correctamente",
            "id_luz": updated[0],
            "estado_luz": luz.estado_luz,
            "modo_func": luz.modo_func,
            "hora_inicio": luz.hora_inicio,
            "hora_fin": luz.hora_fin,
            "id_dispositivo": luz.id_dispositivo
        }
    except Exception as err:
        connexion.rollback()
        return {"error": str(err)}
