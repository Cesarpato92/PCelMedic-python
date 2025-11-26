import tkinter as tk
from tkinter import messagebox, ttk
from Modelo.ModeloCliente import ModeloCliente
from Modelo.ModeloDispositivo import ModeloDispositivo
from Modelo.ModeloReparacion import ModeloReparacion

from Logica.LogicaCliente import LogicaCliente
from Logica.LogicaDispositivo import LogicaDispositivo
from Logica.LogicaReparacion import LogicaReparacion

class VentanaReparacion(tk.Frame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs) 
        self.controller = controller

        # Contenedor Principal de Contenido 
        contenedor = ttk.Frame(self, padding="10")
        contenedor.grid(row=0, column=0, sticky="nsew")
        
        # Configuraciones de expansión para el frame principal y el contenedor
        self.columnconfigure(0, weight=1) 
        self.rowconfigure(0, weight=1)
        contenedor.columnconfigure(0, weight=1)
        contenedor.columnconfigure(1, weight=1)
        contenedor.columnconfigure(2, weight=1)
                
        # El título abarca las 3 columnas 
        ttk.Label(contenedor, text="Gestión de reparaciones", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=3, pady=10)

        # Sección de ID de Reparación y Búsqueda 
        contenedor_id_reparacion = ttk.Frame(contenedor)
        contenedor_id_reparacion.grid(row=1, column=0, columnspan=3, pady=10, sticky="w")
        
        ttk.Label(contenedor_id_reparacion, text="ID Reparacion:").grid(row=0, column=0, sticky="w")
                
        id_rep_frame = ttk.Frame(contenedor_id_reparacion)
        id_rep_frame.grid(row=0, column=1, pady=5, sticky="w", padx=10)
        id_rep_frame.columnconfigure(0, weight=1) 
        
        self.entrada_id_reparacion = ttk.Entry(id_rep_frame, width=20)
        self.entrada_id_reparacion.grid(row=0, column=0, sticky="ew")
        
        ttk.Button(id_rep_frame, text="Buscar", command=self.buscar_id_reparacion).grid(row=0, column=1, padx=5)

        # Columna izquierda - Datos del cliente 
        contenido_izquierda = ttk.Frame(contenedor, padding="10", relief="groove")
        contenido_izquierda.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        contenido_izquierda.columnconfigure(0, weight=1)

        ttk.Label(contenido_izquierda, text="Datos del Cliente", font=("Helvetica", 14, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        ttk.Label(contenido_izquierda, text="Cedula:").grid(row=1, column=0, sticky="w")
        cedula_frame = ttk.Frame(contenido_izquierda)
        cedula_frame.grid(row=2, column=0, sticky="ew", pady=5)
        cedula_frame.columnconfigure(0, weight=1)

        self.entrada_cedula = ttk.Entry(cedula_frame, width=20) 
        self.entrada_cedula.grid(row=0, column=0, sticky="ew") 
        btn_buscar_cliente = ttk.Button(cedula_frame, text="Buscar Cliente", command=self.buscar_dispositivo)
        btn_buscar_cliente.grid(row=0, column=1, padx=5) 
        
        ttk.Label(contenido_izquierda, text="Nombre").grid(row=3, column=0, sticky="w", pady=(8, 0)) 
        self.entrada_nombre = ttk.Entry(contenido_izquierda) 
        self.entrada_nombre.grid(row=4, column=0, sticky="ew", pady=3)

        ttk.Label(contenido_izquierda, text="Email").grid(row=5, column=0, sticky="w", pady=(8, 0)) 
        self.entrada_email = ttk.Entry(contenido_izquierda) 
        self.entrada_email.grid(row=6, column=0, sticky="ew", pady=3)

        ttk.Label(contenido_izquierda, text="Celular").grid(row=7, column=0, sticky="w", pady=(8, 0))
        self.entrada_celular = ttk.Entry(contenido_izquierda) 
        self.entrada_celular.grid(row=8, column=0, sticky="ew", pady=3)

        # Columna central: datos del equipo (Fila 2, Columna 1)
        contenido_centro = ttk.Frame(contenedor, padding="10", relief="groove")
        contenido_centro.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
        contenido_centro.columnconfigure(0, weight=1)

        ttk.Label(contenido_centro, text="Datos del equipo", font=("Helvetica", 14, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 5))
        ttk.Label(contenido_centro, text="Marca").grid(row=1, column=0, sticky="w", pady=(5, 0))
        self.entrada_marca = ttk.Entry(contenido_centro) 
        self.entrada_marca.grid(row=2, column=0, sticky="ew", pady=3)
        ttk.Label(contenido_centro, text="Modelo").grid(row=3, column=0, sticky="w", pady=(5, 0))
        self.entrada_modelo = ttk.Entry(contenido_centro) 
        self.entrada_modelo.grid(row=4, column=0, sticky="ew", pady=3)
        ttk.Label(contenido_centro, text="Tipo de reparación").grid(row=5, column=0, sticky="w", pady=(5, 0))
        self.entrada_tipo_rep = ttk.Entry(contenido_centro) 
        self.entrada_tipo_rep.grid(row=6, column=0, sticky="ew", pady=3)
        ttk.Label(contenido_centro, text="Tipo de contraseña").grid(row=7, column=0, sticky="w", pady=(5, 0))
        self.entrada_tipo_password = ttk.Entry(contenido_centro) 
        self.entrada_tipo_password.grid(row=8, column=0, sticky="ew", pady=3)
        ttk.Label(contenido_centro, text="Contraseña del equipo").grid(row=9, column=0, sticky="w", pady=(5, 0))
        self.entrada_password = ttk.Entry(contenido_centro, show='*') 
        self.entrada_password.grid(row=10, column=0, sticky="ew", pady=3)
        ttk.Label(contenido_centro, text="Precio de reparación").grid(row=11, column=0, sticky="w", pady=(5, 0))
        self.entrada_precio = ttk.Entry(contenido_centro) 
        self.entrada_precio.grid(row=12, column=0, sticky="ew", pady=3)

        # Columna derecha: comentarios y estado (Fila 2, Columna 2)
        contenido_derecha_der = ttk.Frame(contenedor, padding="10", relief="groove")
        contenido_derecha_der.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)
        contenido_derecha_der.columnconfigure(0, weight=1)

        ttk.Label(contenido_derecha_der, text="Comentarios al recibir el equipo", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", pady=(5, 0))
        self.entrada_comentarios = tk.Text(contenido_derecha_der, height=6) 
        self.entrada_comentarios.grid(row=1, column=0, sticky="nsew", pady=3)

        ttk.Label(contenido_derecha_der, text="Estado").grid(row=2, column=0, sticky="w", pady=(5,0))
        self.entrada_estado = ttk.Entry(contenido_derecha_der)       
        self.entrada_estado.grid(row=3, column=0, sticky="w", pady=3)
        
        ttk.Label(contenido_derecha_der, text="Precio refaccion").grid(row=4, column=0, sticky="w", pady=(5,0))
        self.entrada_refaccion = ttk.Entry(contenido_derecha_der)
        self.entrada_refaccion.grid(row=5, column=0, sticky="w", pady=3)
       
        ttk.Label(contenido_derecha_der, text="Comentarios del tecnico").grid(row=6, column=0, sticky="w", pady=(5, 0))
        self.entrada_comentarios_tec = tk.Text(contenido_derecha_der, height=6) 
        self.entrada_comentarios_tec.grid(row=7, column=0, sticky="nsew", pady=3)
        
        ttk.Label(contenido_derecha_der, text="¿Equipo reparado?").grid(row=8, column=0, sticky="w", pady=(5, 0))
        opciones_rep = ["SI", "NO"]
        self.var_tipo_rep = tk.StringVar(self) 
        self.var_tipo_rep.set(opciones_rep) 
        self.var_tipo_rep.set(opciones_rep[0])

        self.entrada_tipo = ttk.Combobox(contenido_derecha_der, 
                                         textvariable=self.var_tipo_rep,
                                         values=opciones_rep,
                                         state="readonly",
                                         width=8)
        self.entrada_tipo.grid(row=9, column=0, sticky="w", pady=3)
        
        contenido_derecha_der.rowconfigure(1, weight=1) 
        contenido_derecha_der.rowconfigure(7, weight=1) 


        # Footer: Contenedor para los botones 
        footer_frame = ttk.Frame(contenedor, padding="10", relief="raised")
        footer_frame.grid(row=3, column=0, columnspan=3, sticky="nsew", pady=(20, 0))
        
        # Configuramos el footer con 3 columnas que se expanden proporcionalmente
        footer_frame.columnconfigure(0, weight=1)
        footer_frame.columnconfigure(1, weight=1)
        footer_frame.columnconfigure(2, weight=1)
        
        # Botones Izquierda 
        frame_btn_izquierda = ttk.Frame(footer_frame)
        frame_btn_izquierda.grid(row=0, column=0, sticky="w")        
        
        ttk.Button(frame_btn_izquierda, text="Boton Izq 1").grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(frame_btn_izquierda, text="Boton Izq 2").grid(row=0, column=1, padx=5, pady=5)        
        
        # Botones Centro 
        frame_btn_centro = ttk.Frame(footer_frame)
        frame_btn_centro.grid(row=0, column=1, sticky="nsew")
        
        frame_btn_centro.columnconfigure(0, weight=1)
        self.Btn_guardar = ttk.Button(frame_btn_centro, text="Guardar", command=self.guardar)
        self.Btn_guardar.grid(row=0, column=0, sticky="ew", padx=5, pady=5) 
        
        # Botones Derecha 
        frame_btn_derecha = ttk.Frame(footer_frame)
        frame_btn_derecha.grid(row=0, column=2, sticky="e")        
       
        ttk.Button(frame_btn_derecha, text="Boton Der 1").grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame_btn_derecha, text="Cancelar", command=self.cancelar_accion).grid(row=0, column=2, padx=5, pady=5)

        self.deshabilitar_entradas()

    # Metodo de verificacion de id reparacion

    def verificar_id_reparacion(self):
        pass
    # Métodos de la clase 
    def guardar(self):
       pass

    def buscar_dispositivo(self):
        messagebox.showinfo("Buscar Cliente", f"Buscando...", parent=self.parent)

    def buscar_id_reparacion(self):
        messagebox.showinfo("Buscar ID", f"Buscando...", parent=self.parent)
        
    def cancelar_accion(self):
       
        self.parent.destroy() # Cierra la ventana principal

    def deshabilitar_entradas(self):
        self.entrada_cedula.config(state="disabled") 
        self.entrada_nombre.config(state="disabled") 
        self.entrada_email.config(state="disabled") 
        self.entrada_celular.config(state="disabled") 
        self.entrada_modelo.config(state="disabled") 
        self.entrada_marca.config(state="disabled") 
        self.entrada_tipo_rep.config(state="disabled") 
        self.entrada_tipo_password.config(state="disabled") 
        self.entrada_password.config(state="disabled") 
        self.entrada_precio.config(state="disabled") 
        self.entrada_comentarios.config(state="disabled") 
        self.entrada_estado.config(state="disabled") 
        
    
    def habilitar_entrada(self):
        self.Btn_guardar.config(state="normal")