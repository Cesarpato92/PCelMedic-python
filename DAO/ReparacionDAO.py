import Logica.Conexion as conexion_bd
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
                       modelo_reparacion.costo_repuesto, modelo_reparacion.precio_reparacion,
                       modelo_reparacion.comentarios, modelo_reparacion.id_dispositivo)
            cursor.execute(sql, valores)
            conexion.commit()
            if cursor.rowcount > 0:
                id_reparacion = cursor.lastrowid  # Obtener el ID auto-generado
                messagebox.showinfo("Éxito", "Reparación agregada exitosamente.")
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

    def obtener_reparacion_por_id(self, modelo_reparacion):
        conexion = None
        cursor = None
        reparacion_encontrada = None
        try:
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()

            sql = """SELECT id_reparacion, fecha_ingreso, estado, costo_repuesto, precio_reparacion, comentarios 
                     FROM reparacion WHERE id_dispositivo = %s"""
            valores = (modelo_reparacion.id_dispositivo,)
            
            cursor.execute(sql, valores)

            resultado = cursor.fetchone()
            
            if resultado:
                id_reparacion, fecha_ingreso, estado, costo_repuesto, precio_reparacion, comentarios = resultado
                reparacion_encontrada = modelo_reparacion.__class__()  # Crear una nueva instancia del mismo tipo
                reparacion_encontrada.id_reparacion = id_reparacion
                reparacion_encontrada.fecha_ingreso = fecha_ingreso
                reparacion_encontrada.estado = estado
                reparacion_encontrada.costo_repuesto = costo_repuesto
                reparacion_encontrada.precio_reparacion = precio_reparacion
                reparacion_encontrada.comentarios = comentarios
                reparacion_encontrada.id_dispositivo = modelo_reparacion.id_dispositivo
            
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error SQL: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
        finally:
            if cursor:
                cursor.close()
            
        return reparacion_encontrada
    

