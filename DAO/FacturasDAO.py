import Logica.Conexion as conexion_bd
from tkinter import messagebox
import mysql.connector
from Modelo.ModeloFactura import ModeloFactura

class FacturasDAO:
    def __init__(self):
        pass

    def agregar_factura(self, modelo_factura):
        
        conexion = None
        cursor = None
        id_factura = None
        
        try:
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()
            sql = "INSERT INTO factura (fecha, total, id_reparacion) VALUES (%s,%s,%s)"
            valores = (modelo_factura.fecha, modelo_factura.total, modelo_factura.id_reparacion)
            cursor.execute(sql,valores)
            conexion.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Exito", "Factura agregada correctamente")
                id_factura = cursor.lastrowid
                
            else:
                messagebox.showwarning("Advertencia", "No se pudo agregar la factura")
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
        return id_factura
    
    # Obtiene la informacion de la factura
    def obtener_factura_por_id(self, id_factura):
        conexion = None
        cursor = None
        factura_encontrada = None
        try:
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()

            sql = "SELECT fecha, total, id_reparacion WHERE id_factura = %s"
            valores = (id_factura)
            cursor.execute(sql, valores)

            # Obtiene el primer resultado
            resultado = cursor.fetchone()

            if resultado:
                factura_encontrada = ModeloFactura()
                factura_encontrada.fecha = resultado[0]
                factura_encontrada.total = resultado[1]
                factura_encontrada.id_reparacion = resultado[2]
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error SQL: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
        finally:
            if cursor:
                cursor.close()
        return factura_encontrada


    def obtener_factura_por_id_reparacion(self, id_reparacion):
        conexion = None
        cursor = None
        factura_encontrada = None
        try:
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()

            sql = "SELECT fecha, total, id_reparacion FROM factura WHERE id_reparacion = %s"
            valores = (id_reparacion,)
            cursor.execute(sql, valores)

            # Obtiene el primer resultado
            resultado = cursor.fetchone()

            if resultado:
                factura_encontrada = ModeloFactura()
                factura_encontrada.fecha = resultado[0]
                factura_encontrada.total = resultado[1]
                factura_encontrada.id_reparacion = resultado[2]
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error SQL: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
        finally:
            if cursor:
                cursor.close()
        return factura_encontrada

    def obtener_ventas_por_rango(self, fecha_inicio, fecha_fin):
        conexion = None
        cursor = None
        resultados = []
        try:
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()

            # Agrupa por fecha (sin hora si es datetime) y suma los totales
            sql = """
                SELECT DATE(fecha) as dia, SUM(total) as total_dia
                FROM factura
                WHERE DATE(fecha) BETWEEN %s AND %s
                GROUP BY dia
                    ORDER BY dia
            """
            valores = (fecha_inicio, fecha_fin)
            cursor.execute(sql, valores)

            resultados = cursor.fetchall()
            
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error SQL: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
        finally:
            if cursor:
                cursor.close()
        return resultados


        