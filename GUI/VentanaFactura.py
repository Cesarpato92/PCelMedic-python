import tkinter as tk
from tkinter import messagebox, ttk

class VentanaFactura(tk.Frame):
    def __init__(self, master, controller, **kwargs): 
        # Pasamos 'master' como argumento posicional al super constructor
        super().__init__(master, **kwargs) 
        self.controller = controller

        # Configuración para que el frame se expanda dentro de su padre
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1) 

        # --- Contenedor Principal de Contenido (usa self como padre) ---
        contenedor = ttk.Frame(self, padding="10")
        contenedor.grid(row=0, column=0, sticky="nsew")

        
