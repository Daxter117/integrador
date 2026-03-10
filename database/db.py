import psycopg2

try:
    connexion = psycopg2.connect(
        # El Hostname externo de tu captura
        host="dpg-d6o7li450q8c73amejdg-a.virginia-postgres.render.com",
        # El nombre de la Database de tu captura
        database="oxigarden_pv2x",
        # El Username de tu captura
        user="usuarios",
        # El Password nuevo de tu captura
        password="5e4DiAATcMg3P0JZ7MlHVvzrKrytrmOy",
        port=5432,
        sslmode="require"
    )
    print("Conexión exitosa a Render PostgreSQL")
except Exception as err:
    print("------ Error:", err)
