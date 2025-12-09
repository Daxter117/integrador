from fastapi import APIRouter
from database.db import connexion
from schemas.usuarios import Usuarios

rutausuarios = APIRouter()

# ======================================
#   OBTENER TODOS LOS USUARIOS
# ======================================
@rutausuarios.get("/usuarios")
def get_usuarios():
    consulta = "SELECT * FROM vista_usuarios;"
    try:
        cursor = connexion.cursor()
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        return resultado
    except Exception as err:
        print("Error:", err)
        return {"error": str(err)}


# ======================================
#   CREAR USUARIO
# ======================================
@rutausuarios.post("/crearusuarios")
def crear_usuario(usu: Usuarios):
    query = f"""
        CALL crear_usuario(
            '{usu.nombre}',
            '{usu.correo}',
            '{usu.contrasena}'
        );
    """
    try:
        cursor = connexion.cursor()
        cursor.execute(query)
        connexion.commit()
        return {"message": "Usuario creado correctamente"}
    except Exception as err:
        print("Error:", err)
        return {"error": str(err)}


# ======================================
#   ACTUALIZAR USUARIO
# ======================================
@rutausuarios.put("/usuarios")
def update_usuario(usu: Usuarios):
    query = f"""
        CALL actualizar_usuario(
            {usu.id_usuario},
            '{usu.nombre}',
            '{usu.correo}',
            '{usu.contrasena}'
        );
    """
    try:
        cursor = connexion.cursor()
        cursor.execute(query)
        connexion.commit()
        return {"message": "Usuario actualizado correctamente"}
    except Exception as err:
        print("Error:", err)
        return {"error": str(err)}


# ======================================
#   ELIMINAR USUARIO
# ======================================
@rutausuarios.delete("/usuarios")
def delete_usuario(usu: Usuarios):
    query = f"CALL eliminar_usuario({usu.id_usuario});"
    try:
        cursor = connexion.cursor()
        cursor.execute(query)
        connexion.commit()
        return {"message": "Usuario eliminado correctamente"}
    except Exception as err:
        print("Error:", err)
        return {"error": str(err)}

