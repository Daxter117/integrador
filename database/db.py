import psycopg2

try:
    connexion = psycopg2.connect(
        host="dpg-d4r3h449c44c73bmjkm0-a.virginia-postgres.render.com",
        database="oxigarden",
        user="usuarios",
        password="G5a5PgUQlhB8TfP6VGkt3MEPmJwwvxnf",
        port=5432,
        sslmode="require"
    )
    print("Conexión exitosa a Render PostgreSQL")
except Exception as err:
    print("------ Error:", err)
