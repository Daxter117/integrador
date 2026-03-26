import psycopg2

try:
    connexion = psycopg2.connect(
        
        host="dpg-d6o7li450q8c73amejdg-a.virginia-postgres.render.com",
        database="oxigarden_pv2x",
        user="usuarios",
        password="5e4DiAATcMg3P0JZ7MlHVvzrKrytrmOy",
        port=5432,
        sslmode="require"
    )
    print("Conexión exitosa a Render PostgreSQL")
    
    connexion.close()

except Exception as err:
    print("------ Error:", err)
