import tkinter as tk
from tkinter import messagebox, ttk
# Importaciones de tu lógica y modelos
from Modelo.ModeloCliente import ModeloCliente
from Modelo.ModeloDispositivo import ModeloDispositivo
from Modelo.ModeloReparacion import ModeloReparacion
from Servicios.ServicioRegistro import ServicioRegistro
from Logica.GeneradorPDF import GeneradorPDF
from datetime import datetime
import os

from Utilidades.AbrirPDF import AbrirPDF

class VentanaRegistro(tk.Frame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs) 
        self.controller = controller
        # Inyección de dependencias
        self.servicio_registro = ServicioRegistro()

        # Configuración para que el frame se expanda dentro de su padre 
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1) 

        # Contenedor principal 
        contenedor = ttk.Frame(self, padding=10)
        contenedor.grid(row=0, column=0, sticky="nsew")
        contenedor.columnconfigure(0, weight=1) 
        contenedor.columnconfigure(1, weight=1) 

        label = ttk.Label(contenedor, text="Registro de Clientes y Dispositivos", font=("Helvetica", 16))
        label.grid(row=0, column=0, columnspan=2, pady=10)

        # Columna izquierda - Datos del cliente (Fila 1, Columna 0)
        contenido_izquierda = ttk.Frame(contenedor, padding=10, relief="groove")
        contenido_izquierda.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        contenido_izquierda.columnconfigure(0, weight=1) 

        ttk.Label(contenido_izquierda, text="Datos del Cliente", font=("Helvetica", 14)).grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        ttk.Label(contenido_izquierda, text="Cedula:").grid(row=1, column=0, sticky="w")
        cedula_frame = ttk.Frame(contenido_izquierda)
        cedula_frame.grid(row=2, column=0, sticky="ew", pady=5)
        cedula_frame.columnconfigure(0, weight=1) # 
        self.entrada_cedula = ttk.Entry(cedula_frame, width=20) 
        self.entrada_cedula.grid(row=0, column=0, sticky="ew") 
        btn_buscar = ttk.Button(cedula_frame, text="Buscar", command=self.buscar_cliente) 
        btn_buscar.grid(row=0, column=1, padx=5) 

        ttk.Label(contenido_izquierda, text="Nombre").grid(row=3, column=0, sticky="w", pady=(8, 0))
        self.entrada_nombre = ttk.Entry(contenido_izquierda) 
        self.entrada_nombre.grid(row=4, column=0, sticky="ew", pady=3)

        ttk.Label(contenido_izquierda, text="Email").grid(row=5, column=0, sticky="w", pady=(8, 0))
        self.entrada_email = ttk.Entry(contenido_izquierda) 
        self.entrada_email.grid(row=6, column=0, sticky="ew", pady=3)

        ttk.Label(contenido_izquierda, text="Celular").grid(row=7, column=0, sticky="w", pady=(8, 0))
        self.entrada_celular = ttk.Entry(contenido_izquierda) 
        self.entrada_celular.grid(row=8, column=0, sticky="ew", pady=3)

        # Columna derecha - Datos del equipo (Fila 1, Columna 1)
        contenido_derecha = ttk.Frame(contenedor, padding=10, relief="groove")
        contenido_derecha.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        contenido_derecha.columnconfigure(0, weight=1) 

        ttk.Label(contenido_derecha, text="Datos del equipo", font=("Helvetica", 14, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        ttk.Label(contenido_derecha, text="Marca").grid(row=1, column=0, sticky="w", pady=(5, 0))
        opciones_marca = ["Samsung", "Apple", "Xiaomi", "Huawei", "Oppo", "Motorola", "Honor", 
        "Realme", "Vivo", "Google", "OnePlus", "Nokia", "Sony", "ZTE", "Poco", "Tecno", "Otro"]
        self.combobox_marca = ttk.Combobox(contenido_derecha, 
        values=opciones_marca, state="readonly")
        self.combobox_marca.grid(row=2, column=0, sticky="w", pady=3)
        self.combobox_marca.current(0)

        ttk.Label(contenido_derecha, text="Modelo").grid(row=3, column=0, sticky="w", pady=(5, 0))
        self.entrada_modelo = ttk.Entry(contenido_derecha) 
        self.entrada_modelo.grid(row=4, column=0, sticky="w", pady=3)

        ttk.Label(contenido_derecha, text="Tipo de reparación").grid(row=5, column=0, sticky="w", pady=(5, 0))
        opciones_rep = ["Display", "Puerto de carga", "Corto", "Sonido", "Cuenta", "Bloqueo", "Otro"]
        
        self.var_tipo_rep = tk.StringVar(self)
        self.var_tipo_rep.set(opciones_rep[0]) 

        self.entrada_tipo = ttk.Combobox(contenido_derecha, 
        textvariable=self.var_tipo_rep, 
        values=opciones_rep, 
        state="readonly", 
        width=20) 

        
        self.entrada_tipo.grid(row=6, column=0, sticky="w", pady=3) 

        ttk.Label(contenido_derecha, text="Tipo de contraseña").grid(row=7, column=0, sticky="w", pady=(5, 0))
        opciones_contra = ["Sin contraseña", "Patrón", "Texto/Números","PIN"]
        
        self.var_tipo_contrasena = tk.StringVar(self)
        self.var_tipo_contrasena.set(opciones_contra[0]) 
        
        
        self.var_tipo_contrasena.trace_add("write", self.on_tipo_contrasena_change)

      
        self.menu_contrasena = ttk.Combobox(contenido_derecha, 
                                            textvariable=self.var_tipo_contrasena, 
                                            values=opciones_contra,
                                            state="readonly", 
                                            width=20) 

        self.menu_contrasena.grid(row=8, column=0, sticky="w", pady=3) 

        ttk.Label(contenido_derecha, text="Contraseña del equipo").grid(row=9, column=0, sticky="w", pady=(5, 0))
        self.entrada_contrasena = ttk.Entry(contenido_derecha) 
        self.entrada_contrasena.grid(row=10, column=0, sticky="w", pady=3)

        ttk.Label(contenido_derecha, text="Precio de reparación").grid(row=11, column=0, sticky="w", pady=(5, 0))
        self.entrada_precio = ttk.Entry(contenido_derecha) 
        self.entrada_precio.grid(row=12, column=0, sticky="w", pady=3)
       
        ttk.Label(contenido_derecha, text="Comentarios").grid(row=13, column=0, sticky="w", pady=(5, 0))
        self.entrada_comentarios = tk.Text(contenido_derecha, height=6) 
        self.entrada_comentarios.grid(row=14, column=0, sticky="nsew", pady=3)

        # Habilitar expansión vertical del Text widget
        contenido_derecha.rowconfigure(14, weight=1)
        
        # creacion de frame del medio (footer)
        inferior_frame = ttk.Frame(contenedor, padding="10", relief="raised")
        inferior_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=(20, 0))
        
        # Configuramos el footer con 3 columnas que se expanden proporcionalmente
        inferior_frame.columnconfigure(0, weight=1)
        inferior_frame.columnconfigure(1, weight=1)
        inferior_frame.columnconfigure(2, weight=1)

      
        frame_btn = ttk.Frame(inferior_frame)
        frame_btn.grid(row=0, column=2, sticky="e")
        ttk.Button(frame_btn, text="Guardar Registro", command=self.guardar).grid(row=0, column=0, padx=5, pady=5) 
        ttk.Button(frame_btn, text="Limpiar Campos", command=self.limpiar_campos).grid(row=0, column=1, padx=5, pady=5)
        
       
        self.on_tipo_contrasena_change()
        self.entrada_cedula.focus()
    
    # Métodos de la clase 
    def on_tipo_contrasena_change(self, *args):
        if self.var_tipo_contrasena.get() == "Sin contraseña":
            self.entrada_contrasena.config(state=tk.DISABLED)
            self.entrada_contrasena.delete(0, tk.END)
        else:
            self.entrada_contrasena.config(state=tk.NORMAL)
            
    def limpiar_campos(self):
        # Función para limpiar todos los campos del formulario
        self.entrada_cedula.config(state=tk.NORMAL)
        self.entrada_cedula.delete(0, tk.END)
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_email.delete(0, tk.END)
        self.entrada_celular.delete(0, tk.END)
        self.combobox_marca.delete(0, tk.END)
        self.entrada_modelo.delete(0, tk.END)
        self.entrada_precio.delete(0, tk.END)
        self.entrada_comentarios.delete('1.0', tk.END)
        self.entrada_contrasena.delete(0, tk.END)
        # Restablecer OptionMenus a la opción por defecto
        opciones_rep = ["Display", "Puerto de carga", "Corto", "Sonido", "Cuenta", "Bloqueo", "Otro"]
        opciones_contra = ["Sin contraseña", "Patrón", "Contraseña", "PIN"]
        opciones_marca = ["Samsung", "Apple", "Xiaomi", "Huawei", "Oppo", "Motorola", "Honor", "Realme", "Vivo", "Google", "OnePlus", "Nokia", "Sony", "ZTE", "Poco", "Tecno"]
        self.var_tipo_rep.set(opciones_rep[0])
        self.var_tipo_contrasena.set(opciones_contra[0])
        self.var_marca.set(opciones_marca[0])
        self.combobox_marca.current(0)
        self.on_tipo_contrasena_change() # Llama para asegurar que la contraseña se deshabilita o habilita correctamente
    

    
    def guardar(self):
        # Extrae datos de cliente
        cedula = self.entrada_cedula.get().strip()
        nombre = self.entrada_nombre.get().strip()
        email = self.entrada_email.get().strip()
        celular = self.entrada_celular.get().strip()

        # Datos del dispositivo 
        marca = self.combobox_marca.get().strip()
        version = self.entrada_modelo.get().strip() 
        tipo_rep = self.var_tipo_rep.get().strip() 
        tipo_contra = self.var_tipo_contrasena.get().strip()
        contra = self.entrada_contrasena.get().strip()
        comentarios_disp = (self.entrada_comentarios.get('1.0', tk.END) or "").strip()

        # Datos de la reparacion
        precio_rep = self.entrada_precio.get().strip()

        # VALIDACIONES BÁSICAS 
        if not (cedula and nombre and email and celular and marca and version and tipo_rep and precio_rep):
            messagebox.showwarning("Atención", "Por favor, complete todos los campos obligatorios.")
            return

        try:
            precio_float = float(precio_rep)
        except ValueError:
            messagebox.showwarning("Atención", "El precio de reparación debe ser un número válido")
            return

        # 2. PREPARACIÓN DE MODELOS
        cliente_obj = ModeloCliente()
        cliente_obj.cedula, cliente_obj.nombre = cedula, nombre
        cliente_obj.email, cliente_obj.celular = email, celular
        
        dispositivo_obj = ModeloDispositivo()
        dispositivo_obj.marca, dispositivo_obj.version = marca, version
        dispositivo_obj.tipo_reparacion, dispositivo_obj.tipo_password = tipo_rep, tipo_contra
        dispositivo_obj.password, dispositivo_obj.comentarios = contra or None, comentarios_disp
        
        reparacion_obj = ModeloReparacion()
        reparacion_obj.fecha_ingreso = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        reparacion_obj.estado, reparacion_obj.precio_reparacion = "En proceso", precio_float
        reparacion_obj.costo_repuestos, reparacion_obj.comentarios = 0, ""

        # 3. EJECUCIÓN A TRAVÉS DEL SERVICIO (SRP/SOLID)
        exito, id_rep, mensaje = self.servicio_registro.registrar_ingreso_completo(cliente_obj, dispositivo_obj, reparacion_obj)

        if exito:
            # 4. GENERACIÓN DE REPORTES (Post-proceso)
            try:
                generador = GeneradorPDF()
                ruta_pdf = generador.generar_reporte_reparacion(cliente_obj, dispositivo_obj, reparacion_obj)
                messagebox.showinfo("Éxito", f"Registro {id_rep} guardado correctamente.")
                if os.path.exists(ruta_pdf):
                    AbrirPDF.open_file(ruta_pdf)
            except Exception as e_pdf:
                messagebox.showwarning("Aviso", f"Guardado con éxito, pero falló el PDF: {e_pdf}")
            
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", f"No se pudo completar el registro: {mensaje}")

    def limpiar_campos(self):
        # Función para limpiar todos los campos del formulario
        self.entrada_cedula.config(state=tk.NORMAL)
        self.entrada_cedula.delete(0, tk.END)
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_email.delete(0, tk.END)
        self.entrada_celular.delete(0, tk.END)
        self.combobox_marca.set("") 
        self.entrada_modelo.delete(0, tk.END)
        self.entrada_precio.delete(0, tk.END)
        self.entrada_comentarios.delete('1.0', tk.END)
        self.entrada_contrasena.delete(0, tk.END)
        opciones_rep = ["Display", "Puerto de carga", "Corto", "Sonido", "Cuenta", "Bloqueo", "Otro"]
        opciones_contra = ["Sin contraseña", "Patrón", "Texto/Números","PIN"] 
        
        self.var_tipo_rep.set(opciones_rep[0])
        self.var_tipo_contrasena.set(opciones_contra[0])
        self.combobox_marca.current(0) 
        self.on_tipo_contrasena_change()
    
    # Habilitar o deshabilitar casilla de contraseña
    def on_cedula(self):
        estado = self.entrada_cedula.cget("state")
        if estado == tk.NORMAL:
            self.entrada_cedula.config(state=tk.DISABLED)
        else: 
            self.entrada_cedula.config(state=tk.NORMAL)

    def buscar_cliente(self):
        cedula =self.entrada_cedula.get().strip()
        if not cedula:
            messagebox.showwarning("AVISO", "Ingrese una cedula para buscar")
            return
            
        try: 
            # Para la búsqueda usamos el servicio que ya gestiona el UnitOfWork internamente
            resultado = self.servicio_registro.buscar_cliente(cedula)
            if resultado:
                
                # Rellenamos los campos del formulario
                self.entrada_nombre.delete(0,tk.END)
                self.entrada_nombre.insert(0, resultado.nombre)
                self.entrada_email.delete(0, tk.END)
                self.entrada_email.insert(0, resultado.email)
                self.entrada_celular.delete(0, tk.END)
                self.entrada_celular.insert(0, resultado.celular)
                
                # Deshabilitar campos de cliente si ya existe
                self.entrada_cedula.config(state=tk.DISABLED)

                messagebox.showinfo("Éxito", "Cliente encontrado y datos cargados")

            else:
                messagebox.showinfo("No encontrado", "El cliente no está registrado en la base de datos")
        
        except Exception as e:
            messagebox.showerror("ERROR", f"Error al buscar cliente : {e}")
            return