import Logica.Conexion as conexion_bd
from tkinter import messagebox
import mysql.connector
from Modelo.ModeloDispositivo import ModeloDispositivo

class DispositivoDAO:

    def __init__(self):
        pass
    
    def agregar_dispositivo(self, modelo_dispositivo):
        conexion = None
        cursor = None
        id_dispositivo = None
        try:
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()

            sql = """INSERT INTO dispositivo (marca, tipo_reparacion, tipo_contraseña, contraseña, comentarios, id_cliente, version ) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            valores = (modelo_dispositivo.marca, modelo_dispositivo.tipo_reparacion,
                       modelo_dispositivo.tipo_password, modelo_dispositivo.password,
                       modelo_dispositivo.comentarios, modelo_dispositivo.id_cliente,
                       modelo_dispositivo.version)
            cursor.execute(sql, valores)
            conexion.commit()
            if cursor.rowcount > 0:
                id_dispositivo = cursor.lastrowid  # Obtener el ID auto-generado
                
            else:
                messagebox.showwarning("Advertencia", "No se pudo agregar el dispositivo.")

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error SQL: {e}")
            if conexion:
                conexion.rollback()
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
        finally:
            if cursor:
                cursor.close()
        return id_dispositivo

    def obtener_dispositivo_por_id(self, id_dispositivo):
        conexion = None
        cursor = None
        dispositivo_encontrado = None
        try:
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()

            sql = "SELECT marca, tipo_reparacion, tipo_contraseña, contraseña, comentarios, id_cliente, version FROM dispositivo WHERE id_dispositivo = %s"
            #Ingresar primero el id_dispositivo al objeto modelo_dispositivo antes de llamar a este metodo
            valores = (id_dispositivo,)
            
            cursor.execute(sql, valores)

            #se obtiene el primer resultado
            resultado = cursor.fetchone()
            if resultado:
                dispositivo_encontrado = ModeloDispositivo()
                dispositivo_encontrado.id_dispositivo = resultado[0]  
                dispositivo_encontrado.marca = resultado[1]
                dispositivo_encontrado.tipo_reparacion = resultado[2]
                dispositivo_encontrado.tipo_password = resultado[3]
                dispositivo_encontrado.password = resultado[4]
                dispositivo_encontrado.comentarios = resultado[5]
                dispositivo_encontrado.id_cliente = resultado[6]
                dispositivo_encontrado.version = resultado[7]
                    

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error SQL: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
        finally:
            if cursor:
                cursor.close()
        return dispositivo_encontrado