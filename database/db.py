import psycopg2

try:
    connexion = psycopg2.connect(
        # Hostname actualizado de tu última captura
        host="dpg-d6o7li450q8c73amejdg-a.virginia-postgres.render.com",
        # Base de datos actualizada
        database="oxigarden_pv2x",
        user="usuarios",
        # Contraseña actualizada
        password="5e4DiAATcMg3P0JZ7MlHVvzrKrytrmOy",
        port=5432,
        sslmode="require"
    )
    print("Conexión exitosa a Render PostgreSQL")
    
    # Opcional: Cerrar la conexión
    connexion.close()

except Exception as err:
    print("------ Error:", err)
