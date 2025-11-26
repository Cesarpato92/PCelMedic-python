import Logica.Conexion as conexion_bd
from tkinter import messagebox
import mysql.connector
from Modelo.ModeloCliente import ModeloCliente

class ClienteDAO:

    def __init__(self):
        pass
    
    def agregar_cliente(self, modelo_cliente):
        # La conexion se gestionara internamente y se cerrara automaticamente
        conexion = None
        cursor = None
        try:
           
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()
            if self.verificar_existencia_cliente(modelo_cliente.cedula):
                messagebox.showwarning("Advertencia", "Se actualizaran los datos del cliente existente.")
                self.actualizar_cliente(modelo_cliente)
                return None
            sql = "INSERT INTO cliente (cedula, nombre, email, celular) VALUES (%s, %s, %s, %s)"
            valores = (modelo_cliente.cedula, modelo_cliente.nombre, modelo_cliente.email, modelo_cliente.celular)
            cursor.execute(sql, valores)
            conexion.commit()
            if cursor.rowcount > 0:
                return modelo_cliente.cedula  # Retornar la cedula
            else:
                messagebox.showwarning("Advertencia", "No se pudo agregar el cliente.")
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
            


    def obtener_cliente_por_cedula(self, cedula):
        conexion = None
        cursor = None
        cliente_encontrado = None
        try:
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()

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
                cliente_encontrado.nombre = nombre
                cliente_encontrado.email = email
                cliente_encontrado.celular = celular
               
            
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error SQL: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
        finally:
            if cursor:
                cursor.close()
            
        return cliente_encontrado
        
    def actualizar_cliente(self, modelo_cliente):
        conexion = None
        cursor = None
        try:
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()

            sql = "UPDATE cliente SET nombre = %s, email = %s, celular = %s WHERE cedula = %s"
            valores = (modelo_cliente.nombre, modelo_cliente.email, modelo_cliente.celular, str(modelo_cliente.cedula))
            cursor.execute(sql, valores)
            conexion.commit()
            
            if cursor.rowcount > 0:
                messagebox.showinfo("Éxito", "Cliente actualizado exitosamente.")
            else:
                messagebox.showinfo("Aviso", "Para actualizar un cliente, debe modificar al menos un dato.")
                
           

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error SQL: {e}")
            if conexion:
                conexion.rollback()
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
        finally:
            if cursor:
                cursor.close()
        return True
           

    def verificar_existencia_cliente(self, cedula):
        conexion = None
        cursor = None
        existe = False
        try:
            conexion = conexion_bd.Conexion.get_conexion()
            cursor = conexion.cursor()

            sql = "SELECT COUNT(*) FROM cliente WHERE cedula = %s"
            valores = (str(cedula),)
            cursor.execute(sql, valores)

            resultado = cursor.fetchone()
            if resultado and resultado[0] > 0:
                existe = True
            

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error SQL: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
        finally:
            if cursor:
                cursor.close()
        return existe