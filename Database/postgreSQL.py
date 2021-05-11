import psycopg2

HOST = "ec2-18-214-140-149.compute-1.amazonaws.com"
PORT = 5432
USER = "mwgpcemadskikj"
PASS = "18ec13d5cf0d982c808ae00cd493d21e3cc58bf9dc47fed9f56c669861dba146"
DATABASE = "d4t49ricrd6qa1"

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

