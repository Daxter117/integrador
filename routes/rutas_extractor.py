from fastapi import APIRouter
from database.db import connexion
from schemas.extractores import extractores   # <-- correcto, en minúsculas

rutaextractores = APIRouter()

# ======================================
#   GET EXTRACTORES
# ======================================
@rutaextractores.get("/getextractores")
def get_extractores():
    try:
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM vista_extractores;")
        return cursor.fetchall()
    except Exception as err:
        return {"error": str(err)}


# ======================================
#   CREAR EXTRACTOR
# ======================================
@rutaextractores.post("/crearextractor")
def crear_extractor(ext: extractores):     # <-- corregido
    query = "SELECT crear_extractor(%s, %s, %s, %s, %s, %s);"
    valores = (
        ext.estado,
        ext.modo_func,
        ext.hora_inicio,
        ext.hora_fin,
        ext.umbral_co2,
        ext.id_dispositivo
    )

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        connexion.commit()
        return {"message": "Extractor creado correctamente"}
    except Exception as err:
        return {"error": str(err)}


# ======================================
#   ACTUALIZAR EXTRACTOR
# ======================================
@rutaextractores.put("/actualizarextractor")
def actualizar_extractor(ext: extractores):   # <-- corregido
    query = "SELECT actualizar_extractor(%s, %s, %s, %s, %s, %s, %s);"
    valores = (
        ext.id_extractor,
        ext.estado,
        ext.modo_func,
        ext.hora_inicio,
        ext.hora_fin,
        ext.umbral_co2,
        ext.id_dispositivo
    )

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        connexion.commit()
        return {"message": "Extractor actualizado correctamente"}
    except Exception as err:
        return {"error": str(err)}


# ======================================
#   ELIMINAR EXTRACTOR
# ======================================
@rutaextractores.delete("/eliminarextractor")
def eliminar_extractor(ext: extractores):   # <-- corregido
    query = "SELECT eliminar_extractor(%s);"
    valores = (ext.id_extractor,)

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        connexion.commit()
        return {"message": "Extractor eliminado correctamente"}
    except Exception as err:
        return {"error": str(err)}
