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

    def agregar_cliente(self, modelo_cliente):
        if self.validacion_datos(modelo_cliente):
            return self.cliente_dao.agregar_cliente(modelo_cliente)
        else:
            return None 
        
    def obtener_cliente_por_cedula(self, cedula):
        if self.validacion_cedula(cedula):
            return self.cliente_dao.obtener_cliente_por_cedula(cedula)
        else:
            return False
        
    def verificacion_existencia_cliente(self, cedula):
        return self.cliente_dao.verificar_existencia_cliente(cedula)
    
    def actualizar_cliente(self, modelo_cliente):
        if self.validacion_datos(modelo_cliente):
            return self.cliente_dao.actualizar_cliente(modelo_cliente)
        else:
            return None

    def validacion_datos(self, modelo_cliente):
         # Validaciones básicas
        # cédula: debe existir, no estar vacía y contener solo dígitos
        validacion_ced = self.validacion_cedula(modelo_cliente.cedula)
        if not validacion_ced:
            return False
        # nombre es obligatorio
        if not modelo_cliente.nombre or modelo_cliente.nombre.strip() == "":
            messagebox.showerror("Error", "El nombre es obligatorio.")
            return False
        if modelo_cliente.celular and not modelo_cliente.celular.isdigit():
            messagebox.showerror(
                "Error", "El número de celular debe contener solo dígitos."
            )
            return False
        if modelo_cliente.celular and len(modelo_cliente.celular) < 10:
            messagebox.showerror(
                "Error", "El número de celular debe tener al menos 10 dígitos."
            )
            return False
        if modelo_cliente.email and "@" not in modelo_cliente.email:
            messagebox.showerror("Error", "El correo electrónico no es válido.")
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
        
        # Validación de 10 dígitos para la cedula
        if len(cedula.strip()) > 20:
            messagebox.showerror("Error", "El cambo cedula no puede tener mas de 20 digitos")
            return False
        
        return True

    def obtener_todos_clientes(self):
        return self.cliente_dao.obtener_todos_clientes()
