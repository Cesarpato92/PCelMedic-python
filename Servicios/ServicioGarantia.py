from Config.UnitOfWork import UnitOfWork
from Logica.LogicaGarantia import LogicaGarantia

class ServicioGarantia:
    def __init__(self):
        self.uow_factory = UnitOfWork

    def registrar_entrada_garantia(self, garantia_obj):
        """
        Registra una nueva entrada de garantía en la base de datos.
        """
        try:
            with self.uow_factory() as uow:
                log_garantia = LogicaGarantia(uow.garantias)
                
                # Registramos la garantía usando el cursor de la transacción
                id_garantia = log_garantia.agregar_garantia(garantia_obj, uow.cursor)
                
                uow.commit()
                return True, id_garantia, "Garantía registrada con éxito"
        except Exception as e:
            return False, None, str(e)

    def procesar_salida_garantia(self, garantia_obj, estado_antiguo):
        """
        Actualiza el estado de una garantía (ej. de 'En Garantia' a 'Completada').
        """
        try:
            with self.uow_factory() as uow:
                log_garantia = LogicaGarantia(uow.garantias)
                
                # Actualizamos la garantía
                exito = log_garantia.actualizar_garantia(garantia_obj, estado_antiguo, uow.cursor)
                
                if exito:
                    uow.commit()
                    return True, "Garantía procesada con éxito"
                else:
                    return False, "No se pudo actualizar la garantía"
        except Exception as e:
            return False, str(e)

    def obtener_garantia_por_id(self, id_garantia):
        """
        Obtiene los detalles de una garantía.
        """
        try:
            with self.uow_factory() as uow:
                log_garantia = LogicaGarantia(uow.garantias)
                garantia = log_garantia.obtener_garantia_por_id(id_garantia, uow.cursor)
                return garantia
        except Exception:
            return None
