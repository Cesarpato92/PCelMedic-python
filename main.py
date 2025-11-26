"""
Script principal para ejecutar PCelMedic.
Debe ejecutarse desde la raíz del proyecto.
"""
import sys
import os
from tkinter import messagebox
# Esto ayuda a garantizar que el directorio actual este en la ruta de Python si es necesario
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importar la clase principal desde el paquete GUI
from GUI.VentanaPrincipal import VentanaPrincipal

if __name__ == "__main__":
    messagebox.showinfo("PCELMEDIC", "Bienvenido al Sistema de Gestion de Información ")
    # Crear e iniciar la aplicacion
    app = VentanaPrincipal()
    app.mainloop()