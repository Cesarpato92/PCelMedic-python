import tkinter as tk
from tkinter import messagebox, ttk
class VentanaGarantia(tk.Frame):
    def __init__(self, master, controller, **kwargs): 
        super().__init__(master, **kwargs) 
        self.controller = controller
        # Configuración para que el frame se expanda dentro de su padre
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1) 

        #  Contenedor Principal de Contenido 
        contenedor = ttk.Frame(self, padding="10")
        contenedor.grid(row=0, column=0, sticky="nsew")
        
        contenedor.columnconfigure(0, weight=1)
        contenedor.columnconfigure(1, weight=1)
        contenedor.columnconfigure(2, weight=1)

        ttk.Label(contenedor, text="Gestión de garantias", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=3, pady=10)

         # Sección de ID de Reparación y Búsqueda 
        contenedor_garantia = ttk.Frame(contenedor)
        contenedor_garantia.grid(row=1, column=0, columnspan=3, pady=10, sticky="w")
       
        frame_btn_izquierda = ttk.Frame(contenedor_garantia)
        frame_btn_izquierda.grid(row=0, column=0, sticky="w")
        ttk.Button(frame_btn_izquierda, text="Entrada Garantia", command=self.abrir_ventana_entrada).pack(side=tk.LEFT, padx=5, pady=5)
        
        frame_btn_derecha = ttk.Frame(contenedor_garantia)
        frame_btn_derecha.grid(row=0, column=2, sticky="e")
        ttk.Button(frame_btn_derecha, text="Entrega Garantia", command=self.abrir_ventana_entrega).pack(side=tk.RIGHT, padx=5, pady=5)
        
    def abrir_ventana_entrada(self):
        pass

    def abrir_ventana_entrega(self):
        pass