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

            sql = "SELECT id_garantia, estado, observaciones, fecha_inicio, fecha_fin, id_reparacion, precio_insumos FROM garantia WHERE id_garantia = %s"
            valores = (id_garantia,)

            cursor.execute(sql, valores)

            resultado = cursor.fetchone()

            if resultado:
                garantia_encontrada = ModeloGarantia()
                garantia_encontrada.id_garantia = resultado[0]
                garantia_encontrada.estado = resultado[1]
                garantia_encontrada.observaciones = resultado[2]
                garantia_encontrada.fecha_inicio = resultado[3]
                garantia_encontrada.fecha_fin = resultado[4]
                garantia_encontrada.id_reparacion = resultado[5]
                garantia_encontrada.precio_insumos = resultado[6]
                
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error SQL: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
        finally:
            if cursor:
                cursor.close()
        return garantia_encontrada

    def actualizar_garantia(self, modelo_garantia):
        conexion = None
        cursor = None
        try:
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()

            sql = "UPDATE garantia SET estado = %s, observaciones = %s, fecha_fin = %s, precio_insumos = %s WHERE id_garantia = %s"
            valores = (modelo_garantia.estado, modelo_garantia.observaciones, modelo_garantia.fecha_fin, modelo_garantia.precio_insumos, modelo_garantia.id_garantia)
            
            cursor.execute(sql, valores)
            conexion.commit()
            
            if cursor.rowcount > 0:
                messagebox.showinfo("Éxito", "Garantía actualizada exitosamente")
                return True
            else:
                messagebox.showwarning("Advertencia", "No se encontró la garantía para actualizar")
                return False
                
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error SQL: {e}")
            if conexion:
                conexion.rollback()
            return False
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
            return False
        finally:
            if cursor:
                cursor.close()