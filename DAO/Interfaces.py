from abc import ABC, abstractmethod

class IClienteDAO(ABC):
    @abstractmethod
    def agregar_cliente(self, modelo_cliente, cursor):
        pass

    @abstractmethod
    def obtener_cliente_por_cedula(self, cedula, cursor):
        pass

    @abstractmethod
    def obtener_todos_clientes(self, cursor=None):
        pass

class IDispositivoDAO(ABC):
    @abstractmethod
    def agregar_dispositivo(self, modelo_dispositivo, cursor):
        pass

    @abstractmethod
    def obtener_dispositivo_por_id(self, id_dispositivo, cursor):
        pass

class IReparacionDAO(ABC):
    @abstractmethod
    def agregar_reparacion(self, modelo_reparacion, cursor):
        pass

    @abstractmethod
    def actualizar_estado_reparacion(self, modelo_reparacion, cursor):
        pass

    @abstractmethod
    def obtener_reparacion_por_id(self, id_reparacion, cursor):
        pass

class IGarantiaDAO(ABC):
    @abstractmethod
    def agregar_garantia(self, modelo_garantia, cursor):
        pass

    @abstractmethod
    def obtener_garantia_por_id(self, id_garantia, cursor):
        pass

    @abstractmethod
    def actualizar_garantia(self, modelo_garantia, cursor):
        pass

class IFacturaDAO(ABC):
    @abstractmethod
    def agregar_factura(self, modelo_factura, cursor):
        pass

    @abstractmethod
    def obtener_factura_por_id_reparacion(self, id_reparacion, cursor):
        pass
    
    @abstractmethod
    def obtener_ventas_por_rango(self, fecha_inicio, fecha_fin, cursor):
        pass
