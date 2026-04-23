from Config.UnitOfWork import UnitOfWork
from Logica.LogicaFactura import LogicaFactura
from Logica.LogicaCliente import LogicaCliente

class ServicioFinanzas:
    def __init__(self):
        self.uow_factory = UnitOfWork

    def obtener_reporte_ventas_por_rango(self, fecha_inicio, fecha_fin):
        """
        Obtiene el desglose de ventas y costos de repuestos en un rango de fechas.
        """
        try:
            with self.uow_factory() as uow:
                # El DAO de facturas ya tiene el método necesario
                log_factura = LogicaFactura(uow.facturas)
                return log_factura.obtener_ventas_por_rango(fecha_inicio, fecha_fin, uow.cursor)
        except Exception as e:
            print(f"Error en ServicioFinanzas.obtener_reporte_ventas_por_rango: {e}")
            return []

    def obtener_lista_clientes_completa(self):
        """
        Obtiene todos los clientes registrados para exportación.
        """
        try:
            with self.uow_factory() as uow:
                log_cliente = LogicaCliente(uow.clientes)
                return log_cliente.obtener_todos_clientes(uow.cursor)
        except Exception as e:
            print(f"Error en ServicioFinanzas.obtener_lista_clientes_completa: {e}")
            return []
