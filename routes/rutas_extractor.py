from fastapi import APIRouter
from database.db import connexion
from schemas.extractores import extractores

rutaextractores = APIRouter()

# ======================================
#   OBTENER TODOS LOS EXTRACTORES
# ======================================
@rutaextractores.get("/extractores")
def get_extractores():
    consulta = "SELECT * FROM vista_extractores;"
    try:
        cursor = connexion.cursor()
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        return resultado
    except Exception as err:
        print("Error:", err)
        return {"error": str(err)}


# ======================================
#   CREAR EXTRACTOR
# ======================================
@rutaextractores.post("/extractores")
def crear_extractor(ex: extractores):
    query = f"""
        CALL crear_extractor(
            {ex.estado},
            {ex.modo_func},
            '{ex.hora_inicio}',
            '{ex.hora_fin}',
            {ex.umbral_co2},
            {ex.id_dispositivo}
        );
    """
    try:
        cursor = connexion.cursor()
        cursor.execute(query)
        connexion.commit()
        return {"message": "Extractor creado correctamente"}
    except Exception as err:
        print("Error:", err)
        return {"error": str(err)}


# ======================================
#   ACTUALIZAR EXTRACTOR
# ======================================
@rutaextractores.put("/extractores")
def actualizar_extractor(ex: extractores):
    query = f"""
        CALL actualizar_extractor(
            {ex.id_extractor},
            {ex.estado},
            {ex.modo_func},
            '{ex.hora_inicio}',
            '{ex.hora_fin}',
            {ex.umbral_co2},
            {ex.id_dispositivo}
        );
    """
    try:
        cursor = connexion.cursor()
        cursor.execute(query)
        connexion.commit()
        return {"message": "Extractor actualizado correctamente"}
    except Exception as err:
        print("Error:", err)
        return {"error": str(err)}


# ======================================
#   ELIMINAR EXTRACTOR
# ======================================
@rutaextractores.delete("/extractores")
def eliminar_extractor(ex: extractores):
    query = f"CALL eliminar_extractor({ex.id_extractor});"
    try:
        cursor = connexion.cursor()
        cursor.execute(query)
        connexion.commit()
        return {"message": "Extractor eliminado correctamente"}
    except Exception as err:
        print("Error:", err)
        return {"error": str(err)}
