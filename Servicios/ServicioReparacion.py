from Config.UnitOfWork import UnitOfWork
from Logica.LogicaReparacion import LogicaReparacion

class ServicioReparacion:
    def __init__(self):
        self.uow_factory = UnitOfWork

    def actualizar_detalle_reparacion(self, reparacion_obj, estado_antiguo):
        """
        Actualiza los detalles de una reparación (estado, comentarios técnicos, costos de repuestos).
        """
        try:
            with self.uow_factory() as uow:
                log_reparacion = LogicaReparacion(uow.reparaciones)
                
                exito = log_reparacion.actualizar_estado_reparacion(reparacion_obj, estado_antiguo, uow.cursor)
                
                if exito:
                    uow.commit()
                    return True, "Reparación actualizada correctamente"
                else:
                    return False, "No se pudo actualizar la reparación"
        except Exception as e:
            return False, str(e)

    def obtener_reparacion_por_id(self, id_reparacion):
        """
        Consulta una reparación específica por su ID.
        """
        try:
            with self.uow_factory() as uow:
                log_reparacion = LogicaReparacion(uow.reparaciones)
                return log_reparacion.obtener_reparacion_por_id(id_reparacion, uow.cursor)
        except Exception:
            return None

    def obtener_datos_completos(self, id_reparacion):
        """
        Obtiene toda la información relacionada (reparación, dispositivo y cliente).
        Especialmente útil para las vistas de detalle o actualizaciones en la GUI.
        """
        try:
            with self.uow_factory() as uow:
                from Logica.LogicaDispositivo import LogicaDispositivo
                from Logica.LogicaCliente import LogicaCliente
                
                log_rep = LogicaReparacion(uow.reparaciones)
                log_dis = LogicaDispositivo(uow.dispositivos)
                log_cli = LogicaCliente(uow.clientes)
                
                reparacion = log_rep.obtener_reparacion_por_id(id_reparacion, uow.cursor)
                if not reparacion: return None, None, None
                
                dispositivo = log_dis.obtener_dispositivo_por_id(reparacion.id_dispositivo, uow.cursor)
                cliente = log_cli.obtener_cliente_por_cedula(dispositivo.id_cliente, uow.cursor)
                
                return reparacion, dispositivo, cliente
        except Exception:
            return None, None, None

    