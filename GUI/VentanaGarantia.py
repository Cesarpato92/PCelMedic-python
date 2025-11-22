import tkinter as tk
from tkinter import messagebox, ttk
class VentanaGarantia(tk.Frame):
    def __init(self, parent, controller):
        super().__init__(parent, padding=10) 
        self.controller = controller