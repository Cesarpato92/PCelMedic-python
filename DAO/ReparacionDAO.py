import Logica.Conexion as conexion_bd
from Modelo.ModeloReparacion import ModeloReparacion
from tkinter import messagebox
import mysql.connector

class ReparacionDAO:

    def __init__(self):
        pass
    
    def agregar_reparacion(self, modelo_reparacion):
        conexion = None
        cursor = None
        id_reparacion = None
        try:
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()

            sql = """INSERT INTO reparacion (fecha_ingreso, estado, costo_repuesto, precio_reparacion, comentarios, id_dispositivo) 
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            valores = (modelo_reparacion.fecha_ingreso, modelo_reparacion.estado,
                       modelo_reparacion.costo_repuestos, modelo_reparacion.precio_reparacion,
                       modelo_reparacion.comentarios, modelo_reparacion.id_dispositivo)
            cursor.execute(sql, valores)
            conexion.commit()
            if cursor.rowcount > 0:
                id_reparacion = cursor.lastrowid  # Obtener el ID auto-generado
                
            else:
                messagebox.showwarning("Advertencia", "No se pudo agregar la reparación.")

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error SQL: {e}")
            if conexion:
                conexion.rollback()
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
        finally:
            if cursor:
                cursor.close()
        return id_reparacion

    
    def actualizar_estado_reparacion(self, modelo_reparacion):
        conexion = None
        cursor = None
        try:
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()

            sql = "UPDATE reparacion SET estado = %s WHERE id_reparacion = %s"
            valores = (modelo_reparacion.estado, modelo_reparacion.id_reparacion)
            cursor.execute(sql, valores)
            conexion.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Éxito", "Estado de la reparación actualizado exitosamente.")
            else:
                messagebox.showwarning("Advertencia", "No se pudo actualizar el estado de la reparación.")

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error SQL: {e}")
            if conexion:
                conexion.rollback()
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
        finally:
            if cursor:
                cursor.close()

    def obtener_reparacion_por_id(self, id_reparacion):
        conexion = None
        cursor = None
        reparacion_encontrada = None
        try:
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()

            sql = """SELECT id_reparacion, fecha_ingreso, estado, costo_repuesto, precio_reparacion, comentarios 
                     FROM reparacion WHERE id_reparacion = %s"""
            valores = (id_reparacion,)
            
            cursor.execute(sql, valores)

            resultado = cursor.fetchone()
            
            if resultado:
                reparacion_encontrada = ModeloReparacion()
                reparacion_encontrada.id_reparacion = resultado[0]
                reparacion_encontrada.fecha_ingreso = resultado[1]
                reparacion_encontrada.estado = resultado[2]
                reparacion_encontrada.costo_repuestos = resultado[3]
                reparacion_encontrada.precio_reparacion = resultado[4]
                reparacion_encontrada.comentarios = resultado[5]
                reparacion_encontrada.id_dispositivo = resultado[6]
            
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error SQL: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
        finally:
            if cursor:
                cursor.close()
            
        return reparacion_encontrada
    

