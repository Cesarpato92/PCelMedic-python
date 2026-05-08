from DAO.Interfaces import IClienteDAO
import mysql.connector
from Config.Conexion import Conexion
from Modelo.ModeloCliente import ModeloCliente

class ClienteDAO(IClienteDAO):

    def __init__(self):
        pass
    
    def agregar_cliente(self, modelo_cliente, cursor):
        
        chequeo_sql= "SELECT COUNT(*) FROM cliente WHERE cedula = %s"
        cursor.execute(chequeo_sql, (modelo_cliente.cedula,))
        resultado = cursor.fetchone()
        
        
        if (resultado and resultado[0] >0):
            sql = 'UPDATE cliente SET nombre = %s, email = %s, celular = %s WHERE cedula = %s'
            valores = (modelo_cliente.nombre, 
                       modelo_cliente.email, 
                       modelo_cliente.celular, 
                       modelo_cliente.cedula)
        else:
            sql = "INSERT INTO cliente (cedula, nombre, email, celular) VALUES (%s, %s, %s, %s)"
            valores = (modelo_cliente.cedula, 
                   modelo_cliente.nombre, 
                   modelo_cliente.email, 
                   modelo_cliente.celular)      
        cursor.execute(sql, valores)

    def obtener_cliente_por_cedula(self, cedula, cursor):
       
        cliente_encontrado = None
       

        sql = "SELECT nombre, email, celular FROM cliente WHERE cedula = %s"
        #Ingresar primero la cedula al objeto modelo_cliente antes de llamar a este metodo
        valores = (cedula,)
            
        cursor.execute(sql, valores)

        #se obtiene el primer resultado
        resultado = cursor.fetchone()
            
        if resultado:
            #Si encuentra el cliente, se crea un objeto ModeloCliente con los datos
            nombre, email, celular = resultado
            cliente_encontrado = ModeloCliente()
            cliente_encontrado.cedula = cedula
            cliente_encontrado.nombre = nombre
            cliente_encontrado.email = email
            cliente_encontrado.celular = celular
            
        return cliente_encontrado
        
 
    def obtener_todos_clientes(self, cursor=None):
        # si se pasa un cursor, se usa ese cursor, si no, se crea uno nuevo
        if cursor:
            sql = "SELECT nombre, email, celular FROM cliente"
            cursor.execute(sql)
            return cursor.fetchall()
        # si no se pasa un cursor, se crea uno nuevo
        conexion = None
        local_cursor = None
        clientes = []
        try:
            conexion = Conexion.get_conexion()
            local_cursor = conexion.cursor()
            sql = "SELECT nombre, email, celular FROM cliente"
            local_cursor.execute(sql)
            clientes = local_cursor.fetchall()
        except mysql.connector.Error as e:
            raise Exception(f"Error SQL: {e}")
        except Exception as e:
            raise Exception(f"Error inesperado: {e}")
        finally:
            if local_cursor:
                local_cursor.close()
        return clientes