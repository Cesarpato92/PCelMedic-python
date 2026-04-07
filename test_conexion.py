from Utilidades.Conexion import Conexion

# Test the connection
conn = Conexion.get_conexion()
if conn:
    print("Connection successful")
    Conexion.desconectar()
else:
    print("Connection failed")