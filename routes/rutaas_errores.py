from fastapi import APIRouter
from database.db import connexion
from schemas.errores import Errores

rutaerrores = APIRouter()

# ======================================
#   GET ERRORES
# ======================================
@rutaerrores.get("/geterrores")
def get_errores():
    try:
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM vista_errores;")
        return cursor.fetchall()
    except Exception as err:
        return {"error": str(err)}


# ======================================
#   CREAR ERROR
# ======================================
@rutaerrores.post("/crearerror")
def crear_error(err: Errores):
    query = "SELECT crear_error(%s, %s, %s);"
    valores = (err.tipo_error, err.mensaje, err.id_dispositivo)

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        connexion.commit()
        return {"message": "Error registrado correctamente"}
    except Exception as e:
        return {"error": str(e)}


# ======================================
#   ACTUALIZAR ERROR
# ======================================
@rutaerrores.put("/actualizarerror")
def actualizar_error(err: Errores):
    query = "SELECT actualizar_error(%s, %s, %s, %s);"
    valores = (err.id_error, err.tipo_error, err.mensaje, err.id_dispositivo)

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        connexion.commit()
        return {"message": "Error actualizado correctamente"}
    except Exception as e:
        return {"error": str(e)}


# ======================================
#   ELIMINAR ERROR
# ======================================
@rutaerrores.delete("/eliminarerror")
def eliminar_error(err: Errores):
    query = "SELECT eliminar_error(%s);"
    valores = (err.id_error,)

    try:
        cursor = connexion.cursor()
        cursor.execute(query, valores)
        connexion.commit()
        return {"message": "Error eliminado correctamente"}
    except Exception as e:
        return {"error": str(e)}
