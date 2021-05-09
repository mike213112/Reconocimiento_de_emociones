import mysql.connector

connector = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'root',
    auth_plugin = 'mysql_native_password',
    database = 'pictures'
)

print('funciona')