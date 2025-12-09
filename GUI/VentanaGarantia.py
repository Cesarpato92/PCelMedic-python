import tkinter as tk
from tkinter import messagebox, ttk
from GUI.VentanaEntradaGarantia import VentanaEntradaGarantia
from GUI.VentanaSalidaGarantia import VentanaSalidaGarantia
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

        # Título
        ttk.Label(contenedor, text="Gestion de garantias", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=3, pady=10)

        # Navbar (Botones)
        frame_navbar = ttk.Frame(contenedor)
        frame_navbar.grid(row=1, column=0, columnspan=3, pady=5, sticky="ew")
        
        # Centrar botones en el navbar
        frame_navbar.columnconfigure(0, weight=1)
        frame_navbar.columnconfigure(1, weight=1)

        ttk.Button(frame_navbar, text="Registro de Garantia", command=self.abrir_ventana_entrada).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ttk.Button(frame_navbar, text="Entrega de Garantia", command=self.abrir_ventana_entrega).grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Contenedor de Vistas (Donde cambian las pantallas)
        self.contenedor_vistas = ttk.Frame(contenedor)
        self.contenedor_vistas.grid(row=2, column=0, columnspan=3, sticky="nsew")
        self.contenedor_vistas.columnconfigure(0, weight=1)
        self.contenedor_vistas.rowconfigure(0, weight=1)
        
        # Asegurar que el contenedor principal expanda la fila del contenido
        contenedor.rowconfigure(2, weight=1)

        self.frames = {}
        for F in (VentanaEntradaGarantia, VentanaSalidaGarantia):
            page_name = F.__name__
            frame = F(self.contenedor_vistas, controller=self) 
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.mostrar_frame("VentanaEntradaGarantia")
        
    def abrir_ventana_entrada(self):
        self.mostrar_frame("VentanaEntradaGarantia")

    def abrir_ventana_entrega(self):
        self.mostrar_frame("VentanaSalidaGarantia")

    def mostrar_frame(self, page_name):
        # Muestra el frame para le nombre de la pagina dado
        frame = self.frames.get(page_name)
        if frame:
            frame.tkraise()
        else:
            messagebox.showerror("Error de navegación", f"No se encontró el frame: {page_name}")
