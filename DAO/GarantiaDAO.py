import Logica.Conexion as conexion_bd
from tkinter import messagebox
import mysql.connector
from Modelo.ModeloGarantia import ModeloGarantia

class GarantiaDAO:
    def __init__(self):
        pass
    
    def agregar_garantia(self, modelo_garantia):
        #La conexion se gestionara internamente y se cerrara de forma automatica
        conexion = None
        cursor = None
        try:
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()
            # debemos verificar si la carantia existe


            sql = "INSERT INTO garantia (estado, observaciones, fecha_inicio, id_reparacion) " \
            "VALUES (%s, %s, %s, %s)"
            valores = (modelo_garantia.estado, modelo_garantia.observaciones, modelo_garantia.fecha_inicio, modelo_garantia.id_reparacion)
            cursor.execute(sql, valores)
            conexion.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Exito", "Garantia agregada exitosamente")
                return modelo_garantia.id_garantia # Retorna el Id de la garantia
            else: 
                messagebox.showwarning("Advertencia", "No se pudo agregar la garantia")
                return None
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error SQL: {e}")
            if conexion:
                conexion.rollback()
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
        finally:
            if cursor:
                cursor.close()
        return None
    
    def obtener_garantia_por_id(self, id_garantia):
        conexion = None
        cursor = None
        garantia_encontrada = None

        try:
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()

            sql = "SELECT estado, observaciones, fecha_inicio, id_reparacion WHERE id_garantia = %s"
            # ingresamos el id de la garantia al objeto
            valores = (id_garantia)

            cursor.execute(sql, valores)

            # Se obtiene el primer resultado
            resultado = cursor.fetchone()

            if resultado:
                garantia_encontrada = ModeloGarantia()
                garantia_encontrada.estado = resultado[0]
                garantia_encontrada.observaciones = resultado[1]
                garantia_encontrada.fecha_inicio = resultado[2]
                garantia_encontrada.id_reparacion = resultado[3]
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error SQL: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
        finally:
            if cursor:
                cursor.close()
        return garantia_encontrada