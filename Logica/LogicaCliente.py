from Utilidades.Validador import Validador
import DAO.ClienteDAO as cliente_dao

class LogicaCliente:
    def __init__(self):
        self.cliente_dao = cliente_dao.ClienteDAO()

    def agregar_cliente(self, modelo_cliente, cursor=None):
        valido, mensaje = self.validacion_datos(modelo_cliente)
        if valido:
            return True, self.cliente_dao.agregar_cliente(modelo_cliente, cursor)
        return False, mensaje
        
    def obtener_cliente_por_cedula(self, cedula, cursor=None):
        valido, mensaje = self.validacion_cedula(cedula)
        if valido:
            return self.cliente_dao.obtener_cliente_por_cedula(cedula, cursor)
        raise ValueError(mensaje)

    def verificacion_existencia_cliente(self, cedula):
        return self.cliente_dao.verificar_existencia_cliente(cedula)
    
    def actualizar_cliente(self, modelo_cliente):
        valido, mensaje = self.validacion_datos(modelo_cliente)
        if valido:
            return True, self.cliente_dao.actualizar_cliente(modelo_cliente)
        return False, mensaje
    
    def validacion_datos(self, modelo_cliente):
        res, msg = self.validacion_cedula(modelo_cliente.cedula)
        if not res: return False, msg
        
        res, msg = Validador.validar_nombre(modelo_cliente.nombre)
        if not res: return False, msg
        
        res, msg = Validador.validar_email(modelo_cliente.email)
        if not res: return False, msg
        
        res, msg = Validador.validar_celular(modelo_cliente.celular)
        if not res: return False, msg
        
        return True, ""
        
    def validacion_cedula(self, cedula):
        return Validador.validar_cedula(cedula)

    def obtener_todos_clientes(self, cursor=None):
        return self.cliente_dao.obtener_todos_clientes(cursor)
