import tkinter as tk
from tkinter import messagebox
from Modelo.ModeloCliente import ModeloCliente
from Modelo.ModeloDispositivo import ModeloDispositivo
from Modelo.ModeloReparacion import ModeloReparacion

from Logica.LogicaCliente import LogicaCliente
from Logica.LogicaDispositivo import LogicaDispositivo
from Logica.LogicaReparacion import LogicaReparacion

class VentanaReparacion(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller
        self.cliente = LogicaCliente()
        self.dispostivo = LogicaDispositivo()
        self.reparacion = LogicaReparacion()

        label = tk.Label(self, text="Gestion de reparaciones", font=("Helvetica", 16))

        # Contenedor principal
        contenedor = tk.Frame(self, bg="white")
        contenedor.pack(fill="both", expand=True, padx=20, pady=20)
        
        #contenedor subPrincipal
        subcontenedor = tk.Frame(contenedor, bg="#f0f0f0")
        subcontenedor.pack(fill="both", expand=True, padx=10, pady=10)

        # contenedor izquierda datos cliente
       # Columna izquierda - Datos del cliente

        contenido_izquierda = tk.Frame(subcontenedor, bg="white")
        contenido_izquierda.pack(side="left", fill="both", expand=True, padx=(0, 10))

        tk.Label(contenido_izquierda, text="Datos del Cliente", font=("Helvetica", 14)).pack(pady=(0, 5), anchor="w")
        tk.Label(contenido_izquierda, text="Cedula:").pack(anchor="w")
        cedula_frame = tk.Frame(contenido_izquierda, bg="white")
        cedula_frame.pack(pady=5, anchor="w")
        self.entrada_cedula = tk.Entry(cedula_frame, width=20)
        self.entrada_cedula.pack(side="left")
        
        tk.Label(contenido_izquierda, text="Nombre", bg="white").pack(pady=(8, 0), anchor="w")
        self.entrada_nombre = tk.Entry(contenido_izquierda, width=30)
        self.entrada_nombre.pack(pady=3, anchor="w")

        tk.Label(contenido_izquierda, text="Email", bg="white").pack(pady=(8, 0), anchor="w")
        self.entrada_email = tk.Entry(contenido_izquierda, width=30)
        self.entrada_email.pack(pady=3, anchor="w")

        tk.Label(contenido_izquierda, text="Celular", bg="white").pack(pady=(8, 0), anchor="w")
        self.entrada_celular = tk.Entry(contenido_izquierda, width=30)
        self.entrada_celular.pack(pady=3, anchor="w")

        # Columna derecha: datos del equipo
        contenido_derecha = tk.Frame(subcontenedor, bg="white")
        contenido_derecha.pack(side="right", fill="both", expand=True, padx=(8, 0))

        tk.Label(contenido_derecha, text="Datos del equipo", font=("Helvetica", 14, "bold"), bg="#f0f0f0").pack(pady=(0, 5), anchor="w")
        tk.Label(contenido_derecha, text="Marca", bg="white").pack(pady=(5, 0), anchor="w")
        self.entrada_marca = tk.Entry(contenido_derecha, width=30)
        self.entrada_marca.pack(pady=3, anchor="w")

        tk.Label(contenido_derecha, text="Modelo", bg="white").pack(pady=(5, 0), anchor="w")
        self.entrada_modelo = tk.Entry(contenido_derecha, width=30)
        self.entrada_modelo.pack(pady=3, anchor="w")

        tk.Label(contenido_derecha, text="Tipo de reparación", bg="white").pack(pady=(5, 0), anchor="w")
        self.entrada_tipo_rep = tk.Entry(contenido_derecha, width=30)
        self.entrada_tipo_rep.pack(pady=3, anchor="w")

        tk.Label(contenido_derecha, text="Tipo de contraseña", bg="#f0f0f0").pack(pady=(5, 0), anchor="w")
        self.entrada_tipo_password = tk.Entry(contenido_derecha, width=30)
        self.entrada_tipo_password.pack(pady=3, anchor="w")
        
        tk.Label(contenido_derecha, text="Contraseña del equipo", bg="white").pack(pady=(5, 0), anchor="w")
        self.entrada_password = tk.Entry(contenido_derecha, width=30, show='*')
        self.entrada_password.pack(pady=3, anchor="w")

        tk.Label(contenido_derecha, text="Precio de reparación", bg="white").pack(pady=(5, 0), anchor="w")
        self.entrada_precio = tk.Entry(contenido_derecha, width=30)
        self.entrada_precio.pack(pady=3, anchor="w")

       
        tk.Label(contenido_derecha, text="Comentarios", bg="white").pack(pady=(5, 0), anchor="w")
        self.entrada_comentarios = tk.Text(contenido_derecha, width=40, height=6)
        self.entrada_comentarios.pack(pady=3, anchor="w")



    
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