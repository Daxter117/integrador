from fastapi import APIRouter
from database.db import connexion
from schemas.usuarios import Usuarios

rutausuarios = APIRouter()

# ======================================
#   OBTENER TODOS LOS USUARIOS
# ======================================
@rutausuarios.get("/getusuarios")
def get_usuarios():
    try:
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM vista_usuarios;")
        return cursor.fetchall()
    except Exception as err:
        return {"error": str(err)}


# ======================================
#   CREAR USUARIO
# ======================================
@rutausuarios.post("/crearusuario")
def crear_usuario(usu: Usuarios):
    query = f"""
        SELECT crear_usuario(
            '{usu.nombre}',
            '{usu.correo}',
            '{usu.contrasena}',
            '{usu.direccion}'
        );
    """
    try:
        cursor = connexion.cursor()
        cursor.execute(query)
        connexion.commit()
        return {"message": "Usuario creado correctamente"}
    except Exception as err:
        return {"error": str(err)}


# ======================================
#   ACTUALIZAR USUARIO
# ======================================
@rutausuarios.put("/actualizarusuario")
def actualizar_usuario(usu: Usuarios):
    query = f"""
        SELECT actualizar_usuario(
            {usu.id_usuario},
            '{usu.nombre}',
            '{usu.correo}',
            '{usu.contrasena}',
            '{usu.direccion}'
        );
    """
    try:
        cursor = connexion.cursor()
        cursor.execute(query)
        connexion.commit()
        return {"message": "Usuario actualizado correctamente"}
    except Exception as err:
        return {"error": str(err)}


# ======================================
#   ELIMINAR USUARIO
# ======================================
@rutausuarios.delete("/eliminarusuario")
def eliminar_usuario(usu: Usuarios):
    query = f"SELECT eliminar_usuario({usu.id_usuario});"
    try:
        cursor = connexion.cursor()
        cursor.execute(query)
        connexion.commit()
        return {"message": "Usuario eliminado correctamente"}
    except Exception as err:
        return {"error": str(err)}
