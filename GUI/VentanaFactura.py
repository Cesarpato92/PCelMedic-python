import tkinter as tk
from tkinter import messagebox, ttk

from datetime import datetime
from Utilidades.AbrirPDF import AbrirPDF
from Servicios.ServicioFacturacion import ServicioFacturacion
from Servicios.ServicioReparacion import ServicioReparacion
import os




class VentanaFactura(tk.Frame):
    def __init__(self, master, controller, **kwargs): 
        super().__init__(master, **kwargs) 
        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1) 

        # Inicializamos los servicios (SOLID)
        self.servicio_facturacion = ServicioFacturacion()
        self.servicio_reparacion = ServicioReparacion()
        self.generador_pdf = GeneradorPDF()

        self.reparacion_model = None
        self.cliente_model = None
        self.dispositivo_model = None

        # --- Contenedor Principal de Contenido (usa self como padre) ---
        contenedor = ttk.Frame(self, padding="10")
        contenedor.grid(row=0, column=0, sticky="n") 
        
        # --- Etiquetas y Entradas ---
        # Buscador
        frame_busqueda = ttk.Frame(contenedor)
        frame_busqueda.grid(row=1, column=0, columnspan=2, pady=10, sticky="w")
        ttk.Label(frame_busqueda, text="ID reparacion:").pack(side=tk.LEFT, padx=5)
        self.entrada_id_reparacion = ttk.Entry(frame_busqueda, width=20)
        self.entrada_id_reparacion.pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_busqueda, text="Buscar", command=self.buscar_reparacion).pack(side=tk.LEFT, padx=5)

        # Informacion de factura
        frame_factura = ttk.LabelFrame(contenedor, text="Detalles de facturacion", padding="10")
        frame_factura.grid(row=2, column=0, columnspan=2, pady=10, sticky="w")

        # Campos de solo lectura
        ttk.Label(frame_factura, text="Cliente: ").grid(row=0, column=1, sticky="w", pady=5)
        self.entrada_cliente = ttk.Label(frame_factura, width=20)
        self.entrada_cliente.grid(row=0, column=2, sticky="w", pady=5)
        ttk.Label(frame_factura, text="ID Dispositivo: ").grid(row=0, column=3, sticky="w", pady=5)
        self.entrada_id_dispositivo = ttk.Label(frame_factura, width=20)
        self.entrada_id_dispositivo.grid(row=0, column=4, sticky="w", pady=5)
        ttk.Label(frame_factura, text="Fecha de inicio de reparacion: ").grid(row=1, column=1, sticky="w", pady=5)
        self.entrada_fecha_inicio = ttk.Label(frame_factura, width=20)
        self.entrada_fecha_inicio.grid(row=1, column=2, sticky="w", pady=5)
        ttk.Label(frame_factura, text="Dispositivo: ").grid(row=2, column=1, sticky="w", pady=5)
        self.entrada_dispositivo = ttk.Label(frame_factura, width=20)
        self.entrada_dispositivo.grid(row=2, column=2, sticky="w", pady=5)
        ttk.Label(frame_factura, text="Estado: ").grid(row=2, column=3, sticky="w", pady=5)
        self.entrada_estado = ttk.Label(frame_factura, width=20, foreground="blue", font=("Helvetica", 12, "bold"))
        self.entrada_estado.grid(row=2, column=4, sticky="w", pady=5)
        ttk.Label(frame_factura, text="Tipo de reparacion: ").grid(row=3, column=1, sticky="w", pady=5)
        self.entrada_tipo_reparacion = ttk.Label(frame_factura, width=20)
        self.entrada_tipo_reparacion.grid(row=3, column=2, sticky="w", pady=5)
        ttk.Label(frame_factura, text="Observaciones del tecnico: ").grid(row=4, column=1, sticky="nw", pady=2)
        self.txt_observaciones_entrada = tk.Text(frame_factura, height=4, width=50, state="disabled")
        self.txt_observaciones_entrada.grid(row=4, column=2, sticky="w", pady=2)
        ttk.Label(frame_factura, text="Total: ", font=("Helvetica", 14, "bold")).grid(row=5, column=3, sticky="w", pady=5)
        self.entrada_total = ttk.Label(frame_factura, width=20, foreground="red", font=("Helvetica", 16, "bold"))
        self.entrada_total.grid(row=5, column=4, sticky="w", pady=5)
        ttk.Button(frame_factura, text="Generar", command=self.generar_factura).grid(row=6, column=2, columnspan=2, pady=10)
        ttk.Button(frame_factura, text="Limpiar", command=self.limpiar_campos).grid(row=7, column=2, columnspan=2, pady=10)

    def generar_factura(self):
        if self.entrada_id_reparacion.get() == "":
            messagebox.showwarning("Atención", "Debe ingresar un ID de reparación")
            return
        if self.reparacion_model is None:
            messagebox.showwarning("Atención", "No se encontró la reparación")
            return
        
        if self.cliente_model is None or self.dispositivo_model is None:
             messagebox.showwarning("Atención", "Faltan datos del cliente o dispositivo")
             return

        if self.entrada_estado.cget("text") != "Completada":
            messagebox.showwarning("Atención", "La reparación no ha sido completada, no se puede generar la factura")
            self.limpiar_campos()
            return

        try:
            # Validamos si ya existe una factura para esta reparación
            factura = self.servicio_facturacion.obtener_factura_por_reparacion(self.reparacion_model.id_reparacion)

            if factura:
                respuesta = messagebox.askyesno("Factura existente", "Ya se generó una factura para esta reparación. ¿Desea abrir una copia del archivo PDF?")
                if respuesta:
                    nombre_archivo = f"Factura_{factura.id_factura}-{self.cliente_model.cedula}.pdf"
                    ruta = os.path.join("Reportes", nombre_archivo)
                    if os.path.exists(ruta):
                        AbrirPDF.open_file(ruta)
                    else:
                        messagebox.showwarning("Archivo no encontrado", f"No se encontró el archivo: {nombre_archivo}")
                return
            
            # Crear modelo de factura
            factura_model = ModeloFactura()
            factura_model.id_reparacion = self.reparacion_model.id_reparacion
            factura_model.fecha = datetime.now()
            
            try:
                if isinstance(self.reparacion_model.precio_reparacion, str):
                    precio_limpio = ''.join(c for c in self.reparacion_model.precio_reparacion if c.isdigit() or c == '.')
                    factura_model.total = float(precio_limpio)
                else:
                    factura_model.total = float(self.reparacion_model.precio_reparacion)
            except ValueError:
                factura_model.total = 0.0
            
            # Clonar el objeto reparación para actualizar su estado a 'Entregada'
            reparacion_entregada = self.reparacion_model
            estado_antiguo = self.reparacion_model.estado
            reparacion_entregada.estado = "Entregada"
            
            # Ejecutar a través del servicio
            exito, mensaje = self.servicio_facturacion.registrar_pago_y_entrega(factura_model, reparacion_entregada, estado_antiguo)
            
            if exito:
                # El servicio ya hizo commit. Ahora generamos el PDF.
                # Necesitamos el ID de la factura generada. El servicio podría devolverlo, 
                # pero para no cambiar la firma del servicio de nuevo, lo buscamos.
                factura_nueva = self.servicio_facturacion.obtener_factura_por_reparacion(self.reparacion_model.id_reparacion)
                if factura_nueva:
                    ruta = self.generador_pdf.generar_factura(self.cliente_model, self.dispositivo_model, self.reparacion_model, factura_nueva.id_factura)
                    if os.path.exists(ruta):
                        AbrirPDF.open_file(ruta)
                
                messagebox.showinfo("Éxito", mensaje)
                self.limpiar_campos()
            else:
                messagebox.showerror("Error", mensaje)
                
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")
            
    def buscar_reparacion(self):
        id_reparacion = self.entrada_id_reparacion.get().strip()
        if not id_reparacion:
            messagebox.showwarning("Atencion", "Ingrese un ID de reparacion")
            return
        try:
            # Usar el servicio de reparación para obtener todos los datos
            reparacion, dispositivo, cliente = self.servicio_reparacion.obtener_datos_completos(id_reparacion)
            
            if not reparacion:
                messagebox.showinfo("No encontrado", "No se encontró la reparación")
                return
            
            # Guardar los datos para el reporte
            self.reparacion_model = reparacion
            self.cliente_model = cliente
            self.dispositivo_model = dispositivo
            
            # Actualizar los campos de la interfaz
            self.entrada_cliente.config(text=f"{cliente.nombre}, Cedula: {cliente.cedula}")
            self.entrada_fecha_inicio.config(text=f"{reparacion.fecha_ingreso}")
            self.entrada_id_dispositivo.config(text=f"{dispositivo.id_dispositivo}")
            self.entrada_dispositivo.config(text=f"{dispositivo.marca} {dispositivo.version}")
            self.entrada_estado.config(text=f"{reparacion.estado}")
            self.entrada_total.config(text=f"{reparacion.precio_reparacion}")
            self.entrada_tipo_reparacion.config(text=f"{dispositivo.tipo_reparacion}")
            self.txt_observaciones_entrada.config(state="normal")
            self.txt_observaciones_entrada.delete(1.0, tk.END)
            
            comentarios = reparacion.comentarios if reparacion.comentarios is not None else "SIN COMENTARIOS ESCRITOS POR EL TECNICO AUN"
            self.txt_observaciones_entrada.insert("1.0", str(comentarios))
            self.txt_observaciones_entrada.config(state="disabled")

        except Exception as e:
            messagebox.showerror(f"Error al buscar la reparacion {id_reparacion}", str(e))

    def limpiar_campos(self):
        self.entrada_id_reparacion.delete(0, tk.END)
        self.entrada_cliente.config(text="")
        self.entrada_fecha_inicio.config(text="")
        self.entrada_id_dispositivo.config(text="")
        self.entrada_dispositivo.config(text="")
        self.entrada_estado.config(text="")
        self.entrada_tipo_reparacion.config(text="")
        self.txt_observaciones_entrada.config(state="normal")
        self.txt_observaciones_entrada.delete(1.0, tk.END)
        self.txt_observaciones_entrada.config(state="disabled")
        self.entrada_total.config(text="")
        