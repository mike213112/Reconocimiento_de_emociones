import mysql.connector

# host = 'localhost'
pri = 172
seg = 18
ter = 0
cua = 2

host = str(pri) + "." + str(seg) + "." + str(ter) + "." + str(cua)

connectar = mysql.connector.connect(
    host=host,
    port=3306, 
    user='root',
    passwd='root',
    auth_plugin='mysql_native_password'
)
print('todo bien')
