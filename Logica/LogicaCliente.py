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
        if(self.validacion_datos()):
            return self.cliente_dao.agregar_cliente(modelo_cliente)

    def obtener_cliente_por_cedula(self, cedula):
        if self.validacionCedula(cedula) is True:
            return self.cliente_dao.obtener_cliente_por_cedula(cedula)
        else:
            return False

    def actualizar_cliente(self, modelo_cliente):
        self.cliente_dao.actualizar_cliente(modelo_cliente)

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
        # Verificamos que la cédula no esté vacía y contenga solo dígitos
        if not cedula or cedula.strip() == "" or not cedula.isdigit() and len(cedula)>20:
            messagebox.showerror(
                "Error", "La cédula no puede estar vacía y debe contener solo dígitos y maximo 20 digitos."
            )
            return False
        
        # Verificamos que la cédula tenga menos de 10 dígitos
        if len(cedula.strip()) < 10:
            messagebox.showerror("Error", "La cédula debe tener menos de 10 dígitos.")
            return False
        
        return True
