import tkinter as tk
from tkinter import messagebox, ttk
class VentanaGarantia(tk.Frame):
    def __init(self, parent, controller):
        super().__init__(parent, bg="white") 
        self.controller = controller

        # Configuración para que el frame se expanda dentro de su padre
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1) 

        # --- Contenedor Principal de Contenido (usa self como padre) ---
        contenedor = ttk.Frame(self, padding="10")
        contenedor.grid(row=0, column=0, sticky="nsew")
        
        # Configurar columnas de main_frame para que se expandan proporcionalmente
        contenedor.columnconfigure(0, weight=1)
        contenedor.columnconfigure(1, weight=1)
        contenedor.columnconfigure(2, weight=1)

        # El título abarca las 3 columnas
        tk.Label(contenedor, text="Gestión de garantias", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=3, pady=10)

         # Sección de ID de Reparación y Búsqueda 
        
        contenedor_garantia = ttk.Frame(contenedor)
        contenedor_garantia.grid(row=1, column=0, columnspan=3, pady=10, sticky="w")
        #--------------------------------
        #-----------------------------
        #-------------------------
        # En la garantia solo van botones de entrada y salida para mostrar las ventanas de la 
        # Entrada garantia y Salida Garantia
        frame_btn_izquierda = ttk.Frame(contenedor_garantia)
        frame_btn_izquierda.grid(row=0, column=0, sticky="w")
        tk.Button(frame_btn_izquierda, text="Entrada Garantia", command=self.abrir_ventana_entrada).pack(side=tk.LEFT, padx=5, pady=5)
        
        frame_btn_derecha = ttk.Frame(contenedor_garantia)
        frame_btn_derecha.grid(row=0, column=2, sticky="e")
        tk.Button(frame_btn_derecha, text="Entrega Garantia", command=self.abrir_ventana_entrega).pack(side=tk.RIGHT, padx=5, pady=5)
        
    def abrir_ventana_entrada(self):
        pass

    def abrir_ventana_entrega(self):
        pass