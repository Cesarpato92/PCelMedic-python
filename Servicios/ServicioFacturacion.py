from Config.UnitOfWork import UnitOfWork
from Logica.LogicaFactura import LogicaFactura
from Logica.LogicaReparacion import LogicaReparacion

class ServicioFacturacion:
    def __init__(self):
        self.uow_factory = UnitOfWork

    def registrar_pago_y_entrega(self, factura_obj, reparacion_obj, estado_antiguo_rep):
        """
        Orquesta la creación de la factura y la actualización de la reparación a 'Entregada'
        dentro de una transacción atómica.
        """
        try:
            with self.uow_factory() as uow:
                log_factura = LogicaFactura(uow.facturas)
                log_reparacion = LogicaReparacion(uow.reparaciones)
                
                # 1. Registrar la factura
                id_factura = log_factura.agregar_factura(factura_obj, uow.cursor)
                if not id_factura:
                    raise ValueError("Error al registrar la factura en la base de datos.")
                
                # 2. Actualizar el estado de la reparación
                exito_rep = log_reparacion.actualizar_estado_reparacion(reparacion_obj, estado_antiguo_rep, uow.cursor)
                if not exito_rep:
                    raise ValueError("Error al actualizar el estado de la reparación a 'Entregada'.")
                
                uow.commit()
                return True, "Pago y entrega registrados correctamente"
        except Exception as e:
            # El UoW hace rollback automáticamente al salir del bloque 'with' si hay excepción
            return False, str(e)

    def obtener_factura_por_reparacion(self, id_reparacion):
        """
        Busca una factura asociada a una reparación específica.
        """
        try:
            with self.uow_factory() as uow:
                log_factura = LogicaFactura(uow.facturas)
                return log_factura.obtener_factura_por_id_reparacion(id_reparacion, uow.cursor)
        except Exception:
            return None

    def obtener_reporte_ventas(self, fecha_inicio, fecha_fin):
        """
        Obtiene el listado de ventas en un rango de fechas.
        """
        try:
            with self.uow_factory() as uow:
                log_factura = LogicaFactura(uow.facturas)
                return log_factura.obtener_ventas_por_rango(fecha_inicio, fecha_fin, uow.cursor)
        except Exception:
            return []
