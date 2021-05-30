import psycopg2

HOST = "localhost"
PORT = 5432
USER = "root"
PASS = "root"
DATABASE = "photo"

conectar = psycopg2.connect(
    host=HOST,
    port=PORT,
    user=USER,
    password=PASS,
    database=DATABASE
)

conexion = conectar.cursor()
query = """SELECT * FROM FOTOS"""
#conexion.execute("SELECT * FROM FOTOS")
conexion.execute(query)

for i in conexion:
    print(i)

conexion.close()

