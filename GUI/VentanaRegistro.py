import tkinter as tk
from tkinter import messagebox, ttk
# Importaciones de tu lógica y modelos
from Modelo.ModeloCliente import ModeloCliente
from Modelo.ModeloDispositivo import ModeloDispositivo
from Modelo.ModeloReparacion import ModeloReparacion
from Logica.LogicaCliente import LogicaCliente
from Logica.LogicaDispositivo import LogicaDispositivo
from Logica.LogicaReparacion import LogicaReparacion
from datetime import datetime


class VentanaRegistro(tk.Frame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs) 
        self.controller = controller
        

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
        self.entrada_marca = ttk.Entry(contenido_derecha)
        self.entrada_marca.grid(row=2, column=0, sticky="ew", pady=3)

        ttk.Label(contenido_derecha, text="Modelo").grid(row=3, column=0, sticky="w", pady=(5, 0))
        self.entrada_modelo = ttk.Entry(contenido_derecha) 
        self.entrada_modelo.grid(row=4, column=0, sticky="ew", pady=3)

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
        opciones_contra = ["Sin contraseña", "Patrón", "Texto/Números"]
        
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
        self.entrada_contrasena.grid(row=10, column=0, sticky="ew", pady=3)

        ttk.Label(contenido_derecha, text="Precio de reparación").grid(row=11, column=0, sticky="w", pady=(5, 0))
        self.entrada_precio = ttk.Entry(contenido_derecha) 
        self.entrada_precio.grid(row=12, column=0, sticky="ew", pady=3)
       
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

        # Botones Izquierda 
        frame_btn_izquierda = ttk.Frame(inferior_frame)
        frame_btn_izquierda.grid(row=0, column=0, sticky="w")
        ttk.Button(frame_btn_izquierda, text="Limpiar Campos", command=self.limpiar_campos).grid(row=0, column=0, padx=5, pady=5)
        
        # Botones Centro 
        frame_btn_centro = ttk.Frame(inferior_frame)
        frame_btn_centro.grid(row=0, column=1, sticky="nsew")
        frame_btn_centro.columnconfigure(0, weight=1) 
        Btn_guardar = ttk.Button(frame_btn_centro, text="Guardar Registro", command=self.guardar)
        Btn_guardar.grid(row=0, column=1, sticky="w", padx=5, pady=5) 

       
        self.on_tipo_contrasena_change()
    
    # Métodos de la clase 
    def on_tipo_contrasena_change(self, *args):
        if self.var_tipo_contrasena.get() == "Sin contraseña":
            self.entrada_contrasena.config(state=tk.DISABLED)
            self.entrada_contrasena.delete(0, tk.END)
        else:
            self.entrada_contrasena.config(state=tk.NORMAL)
            self.entrada_contrasena.config(show='*')

    def limpiar_campos(self):
        # Función para limpiar todos los campos del formulario
        self.entrada_cedula.delete(0, tk.END)
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_email.delete(0, tk.END)
        self.entrada_celular.delete(0, tk.END)
        self.entrada_marca.delete(0, tk.END)
        self.entrada_modelo.delete(0, tk.END)
        self.entrada_precio.delete(0, tk.END)
        self.entrada_comentarios.delete('1.0', tk.END)
        # Restablecer OptionMenus a la opción por defecto
        opciones_rep = ["Display", "Puerto de carga", "Corto", "Sonido", "Cuenta", "Bloqueo", "Otro"]
        opciones_contra = ["Sin contraseña", "Patrón", "Texto/Números"]
        self.var_tipo_rep.set(opciones_rep[0])
        self.var_tipo_contrasena.set(opciones_contra[0])
        self.on_tipo_contrasena_change() # Llama para asegurar que la contraseña se deshabilita/habilita correctamente
        self.entrada_cedula.config(state=tk.NORMAL)

    def guardar(self):
        # Extrae datos de cliente
        cedula = self.entrada_cedula.get().strip()
        nombre = self.entrada_nombre.get().strip()
        email = self.entrada_email.get().strip()
        celular = self.entrada_celular.get().strip()

        # Datos del dispositivo 
        marca = self.entrada_marca.get().strip()
        modelo = self.entrada_modelo.get().strip()
        tipo_rep = self.var_tipo_rep.get().strip() 
        tipo_contra = self.var_tipo_contrasena.get().strip()
        contra = self.entrada_contrasena.get().strip()
        comentarios_disp = (self.entrada_comentarios.get('1.0', tk.END) or "").strip()

        # Datos de la reparacion
        estado = "Pendiente".upper()
        fecha_ingreso = datetime.now().date()
        costo_repuesto = 0
        precio_rep = self.entrada_precio.get().strip()
        comentarios_rep = ""

        # Validación básica
        if not (cedula and nombre and email and celular):
            messagebox.showwarning("Atención", "Rellene todos los datos del cliente")
            return

        # Decidir insertar o actualizar según exista el cliente
        try:
            existente = self.cliente.obtener_cliente_por_cedula(cedula)
            cliente_obj = ModeloCliente()
            cliente_obj.cedula = cedula
            cliente_obj.nombre = nombre
            cliente_obj.email = email
            cliente_obj.celular = celular

            if existente:
                messagebox.showinfo("CLIENTE REGISTRADO", f"Se actualizarán los datos del cliente {nombre}")
                actualizado = self.cliente.actualizar_cliente(cliente_obj)
                if not actualizado:
                    messagebox.showwarning("Aviso", "No se realizaron cambios al cliente")
            else:
                insertado = self.cliente.insertar_cliente(cliente_obj) 
                if not insertado:
                    messagebox.showerror("Error", "Error al guardar el usuario")
                    return
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar/actualizar cliente: {e}")
            return

        
        extra = []
        if modelo:
            extra.append(f"Modelo: {modelo}")
       
        if extra:
            comentarios_disp = (comentarios_disp + "\n" + " | ".join(extra)).strip()

        # Guardar dispositivo y reparación
        try:
            dispositivo_obj = ModeloDispositivo()
            dispositivo_obj.id_cliente=cedula
            dispositivo_obj.marca=marca
            dispositivo_obj.modelo=modelo
            dispositivo_obj.tipo_reparacion=tipo_rep
            dispositivo_obj.tipo_contrasena=tipo_contra
            dispositivo_obj.contrasena=contra or None
            dispositivo_obj.comentarios=comentarios_disp or None
            

            id_disp = LogicaDispositivo.agregar_dispositivo(dispositivo_obj)
            
            if id_disp:
                # Guardar la reparación asociada al dispositivo
                reparacion_obj = ModeloReparacion()
                reparacion_obj.id_dispositivo = id_disp,
                reparacion_obj.fecha_ingreso = fecha_ingreso,
                reparacion_obj.estado = estado,
                reparacion_obj.costo_repuesto = costo_repuesto,
                reparacion_obj.precio_reparacion = float(precio_rep), # Convertimos a float
                reparacion_obj.comentarios_tecnicos = comentarios_rep 
                id_rep = LogicaReparacion.agregar_reparacion(reparacion_obj)
                
                if id_rep:
                    messagebox.showinfo("Registro Exitoso", f"Reparación registrada con ID {id_rep}.")
                    self.limpiar_campos()
                        
        except Exception as e:
            messagebox.showwarning("Aviso", f"Ocurrió un error al guardar el dispositivo o la reparación: {e}")

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
        
        resultado = None
        try: 
            resultado = self.cliente.obtener_cliente_por_cedula(cedula)
        except Exception as e:
            messagebox.showerror("ERROR", f"Error al buscar cliente : {e}")
            return
        
        if not resultado:
            messagebox.showinfo("No encontrado", "El cliente no esta registrado en la base de datos")
            return
            
        # Rellenamos los campos del formulario
        try:
            self.entrada_nombre.delete(0,tk.END)
            self.entrada_nombre.insert(0, resultado.nombre)
            self.entrada_email.delete(0, tk.END)
            self.entrada_email.insert(0, resultado.email)
            self.entrada_celular.delete(0, tk.END)
            self.entrada_celular.insert(0, resultado.celular)
            
            # Deshabilitar campos de cliente si ya existe?
            self.entrada_cedula.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("ERROR", f"Error al rellenar los campos: {e}")
            return
