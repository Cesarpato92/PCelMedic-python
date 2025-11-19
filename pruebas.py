from tkinter import messagebox
from Modelo.ModeloCliente import ModeloCliente 
from Logica.LogicaCliente import LogicaCliente
from Modelo.ModeloDispositivo import ModeloDispositivo
from Logica.LogicaDispositivo import LogicaDispositivo
from Logica.LogicaReparacion import LogicaReparacion
from Modelo.ModeloReparacion import ModeloReparacion


#Prueba: Flujo completo cliente -> dispositivo -> reparación con cédula como FK

cliente = ModeloCliente()
cliente.cedula = "5555555555"
cliente.nombre = "sadwewew"
cliente.email = "ijasdoias@ikaskd.sd"
cliente.celular = "3109389023"

# Agregar cliente y obtener su cédula
logica_cliente = LogicaCliente()
cedula_cliente = logica_cliente.agregar_cliente(cliente)

if cedula_cliente:
    # Agregar dispositivo asociado al cliente
    dispositivo = ModeloDispositivo()
    dispositivo.marca = "Samsung"
    dispositivo.tipo_reparacion = "se enciende pero no carga el sistema"
    dispositivo.tipo_password = "PIN"
    dispositivo.password = "1234"
    dispositivo.comentarios = "El cliente dice que se le mojó"
    dispositivo.id_cliente = cedula_cliente  # Usar la cédula del cliente como FK
    
    logica_dispositivo = LogicaDispositivo()
    id_dispositivo = logica_dispositivo.agregar_dispositivo(dispositivo)
    # Agregar reparación asociada al dispositivo
    if id_dispositivo:
        reparacion = ModeloReparacion()
        reparacion.fecha_ingreso = "2024-06-01"
        reparacion.estado = "En Proceso"
        reparacion.costo_repuesto = 0
        reparacion.precio_reparacion = 150.0
        reparacion.comentarios = "Reparación inicial"
        # Usar el ID del dispositivo insertado
        reparacion.id_dispositivo = id_dispositivo
        
        logica_reparacion = LogicaReparacion()
        id_reparacion = logica_reparacion.agregar_reparacion(reparacion)
        # Verificar si la reparación se agregó correctamente
        if id_reparacion:
            messagebox.showinfo("Éxito", f"Flujo completo exitoso. Reparación ID: {id_reparacion}")
        else:
            messagebox.showerror("Error", "No se pudo agregar la reparación.")
    else:
        messagebox.showerror("Error", "No se pudo agregar el dispositivo.")
else:
    messagebox.showerror("Error", "No se pudo agregar el cliente.")
"""# El flujo nos ayuda a verificar la integridad referencial y la correcta inserción de datos en las tablas relacionadas."""
