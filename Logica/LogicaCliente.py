from tkinter import messagebox
import DAO.ClienteDAO as cliente_dao


class LogicaCliente:
    # Inyectamos las dependencias dentro del constructor
    def __init__(self):
        self.cliente_dao = cliente_dao.ClienteDAO()

    """En los metodos de la logica simplemente llamamos a los metodos del DAO 
    correspondiente  en cada metodo realizamos las validaciones o reglas 
    de negocio necesarias antes o despues de llamar al DAO
    Verificamos que los datos sean correctos antes de llamar al DAO, etc."""

    def agregar_cliente(self, modelo_cliente, cursor = None):
        if self.validacion_datos(modelo_cliente):
            return self.cliente_dao.agregar_cliente(modelo_cliente, cursor)
        
        
    def obtener_cliente_por_cedula(self, cedula, cursor):
        if self.validacion_cedula(cedula):
            return self.cliente_dao.obtener_cliente_por_cedula(cedula, cursor)

    def verificacion_existencia_cliente(self, cedula):
        return self.cliente_dao.verificar_existencia_cliente(cedula)
    
    def actualizar_cliente(self, modelo_cliente):
        if self.validacion_datos(modelo_cliente):
            return self.cliente_dao.actualizar_cliente(modelo_cliente)
    
    def validacion_datos(self, modelo_cliente):
        # Validaciones básicas
        # cédula: debe existir, no estar vacía y contener solo dígitos
        validacion_ced = self.validacion_cedula(modelo_cliente.cedula)
        validacion_nombre = self.validacion_nombre(modelo_cliente.nombre)
        validacion_email = self.validacion_email(modelo_cliente.email)
        validacion_celular = self.validacion_celular(modelo_cliente.celular)
        if not validacion_ced:
            return False
        # nombre es obligatorio
        if not validacion_nombre:
            return False
        
        if not validacion_email:
            return False

        if not validacion_celular:
            return False
        
        return True
        
        
    def validacion_celular(self,celular):
        if celular and not celular.isdigit():
            messagebox.showerror("Error", "El número de celular debe contener solo dígitos.")
            return False
        
        if len(celular) < 10 or len(celular)> 15:
            messagebox.showerror("Error", "El número de celular debe tener entre 10 y 15 digitos como maximo.")
            return False
                
        return True
    def validacion_email(self,email):
        if email and "@" not in email:
            messagebox.showerror("Error", "El correo electrónico no es válido.")
            return False
        if len(email) > 100:
            messagebox.showerror("Error", "El correo electrónico es demasiado largo.")
            return False
        return True

    def validacion_nombre(self, nombre):
        if not nombre or nombre.strip() == "":
            messagebox.showerror("Error", "El nombre es obligatorio.")
            return False
        
        if len(nombre) >150:
            messagebox.showerror("Error", "El nombre no puede tener mas de 150 caracteres.")
            return False
        return True

    def validacion_cedula(self, cedula):
    # Verificamos que la cédula no esté vacía
        if not cedula or cedula.strip() == "":
            messagebox.showerror("Error", "La cédula no puede estar vacía.")
            return False
        
        # Verificamos que contenga solo dígitos
        if not cedula.isdigit():
            messagebox.showerror("Error", "La cédula debe contener solo dígitos.")
            return False
        
        # Verificamos que la cédula tenga máximo 20 dígitos (consistente con VARCHAR(20))
        if len(cedula.strip()) > 20:
            messagebox.showerror("Error", "La cédula debe tener máximo 20 dígitos.")
            return False
        
        return True

    def obtener_todos_clientes(self):
        return self.cliente_dao.obtener_todos_clientes()
