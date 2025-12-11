from fastapi import APIRouter
from database.db import connexion
from schemas.extractores import Extractores
 
rutaextractores = APIRouter()
 
@rutaextractores.put("/actualizar_extractor")
def actualizar_extractor(ext: Extractores):
    query = """
        UPDATE extractores
        SET estado = %s,
            modo_func = COALESCE(%s, 0),
            hora_inicio = COALESCE(%s, '00:00'),
            hora_fin = COALESCE(%s, '00:00'),
            umbral_co2 = COALESCE(%s, 0),
            id_dispositivo = COALESCE(%s, 0)
        WHERE id_extractor = %s
        RETURNING id_extractor;
    """
    valores = (
        ext.estado,
        ext.modo_func,
        ext.hora_inicio,
        ext.hora_fin,
        ext.umbral_co2,
        ext.id_dispositivo,
        ext.id_extractor
    )
    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        updated_id = cursor.fetchone()[0]
        connexion.commit()
        return {
            "message": "Extractor actualizado correctamente",
            "id_extractor": updated_id,
            "estado": ext.estado
        }
    except Exception as err:
        connexion.rollback()
        return {"error": str(err)}
