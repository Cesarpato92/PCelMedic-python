from Config.UnitOfWork import UnitOfWork
from Logica.LogicaCliente import LogicaCliente
from Logica.LogicaDispositivo import LogicaDispositivo
from Logica.LogicaReparacion import LogicaReparacion

class ServicioRegistro:
    def __init__(self):
        # El servicio se encarga de instanciar las lógicas con los DAOs correctos
        # (Idealmente esto lo haría un contenedor de IoC, pero en Python manual es aceptable)
        self.uow_factory = UnitOfWork

    def registrar_ingreso_completo(self, cliente_obj, dispositivo_obj, reparacion_obj):
        """
        Orquesta el registro de un cliente, su dispositivo y la reparación inicial
        dentro de una única transacción.
        """
        id_reparacion = None
        
        try:
            with self.uow_factory() as uow:
                # Inyectamos los DAOs del UoW en las lógicas para esta transacción
                log_cliente = LogicaCliente(uow.clientes)
                log_dispositivo = LogicaDispositivo(uow.dispositivos)
                log_reparacion = LogicaReparacion(uow.reparaciones)

                # 1. Registrar/Actualizar Cliente
                exito_cli, msg_cli = log_cliente.agregar_cliente(cliente_obj, uow.cursor)
                if not exito_cli:
                    raise ValueError(f"Error en Cliente: {msg_cli}")

                # 2. Registrar Dispositivo
                dispositivo_obj.id_cliente = cliente_obj.cedula
                id_disp = log_dispositivo.agregar_dispositivo(dispositivo_obj, uow.cursor)
                dispositivo_obj.id_dispositivo = id_disp

                # 3. Registrar Reparación
                reparacion_obj.id_dispositivo = id_disp
                id_reparacion = log_reparacion.agregar_reparacion(reparacion_obj, uow.cursor)
                reparacion_obj.id_reparacion = id_reparacion

                # Si todo sale bien, commit
                uow.commit()
                return True, id_reparacion, "Registro completado con éxito"

        except Exception as e:
            return False, None, str(e)

    def buscar_cliente(self, cedula):
        """
        Busca un cliente por su cédula para autocompletar en la GUI.
        """
        try:
            with self.uow_factory() as uow:
                log_cliente = LogicaCliente(uow.clientes)
                return log_cliente.obtener_cliente_por_cedula(cedula, uow.cursor)
        except Exception:
            return None
