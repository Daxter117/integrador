from fastapi import APIRouter
from database.db import connexion
from schemas.errores import Errores

rutaerrores = APIRouter()


# ================================
#     GET ERRORES
# ================================
@rutaerrores.post("/geterrores")
def get_errores():
    consulta = "SELECT * FROM vista_errores"
    try:
        sql = connexion.cursor()
        sql.execute(consulta)
        resultado = sql.fetchall()
        return resultado
    except Exception as err:
        print("----- Error:", err)
        return {"error": str(err)}


# ================================
#     INSERTAR ERROR
# ================================
@rutaerrores.post("/inserterror")
def insert_error(err: Errores):
    consulta = f"""
    CALL crear_error(
        '{err.fecha_hora}',
        '{err.descripcion}',
        '{err.id_dispositivo}'
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
#     ELIMINAR ERROR
# ================================
@rutaerrores.post("/delerror")
def delete_error(err: Errores):
    consulta = f"CALL eliminar_error('{err.id_error}');"
    try:
        sql = connexion.cursor()
        sql.execute(consulta)
        connexion.commit()
        return {"message": "1"}
    except Exception as e:
        print("----- Error:", e)
        return {"error": str(e)}


# ================================
#     ACTUALIZAR ERROR
# ================================
@rutaerrores.post("/updateerror")
def update_error(err: Errores):
    consulta = f"""
    CALL actualizar_error(
        '{err.id_error}',
        '{err.fecha_hora}',
        '{err.descripcion}',
        '{err.id_dispositivo}'
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
