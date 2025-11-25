import tkinter as tk
from tkinter import messagebox, ttk

class VentanaFinanzas(tk.Frame):

    def __init__(self, master, controller, **kwargs): 
        # Pasamos 'master' como argumento posicional al super constructor
        super().__init__(master, **kwargs) 
        self.controller = controller
        label = tk.Label(self, text="Página de Finanzas (GRID)", bg='plum', font=("Helvetica", 16))
        label.grid(row=0, column=0, pady=20, padx=20)

