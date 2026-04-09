import os
import sys
import subprocess
from tkinter import messagebox

class AbrirPDF:
    @staticmethod
    def open_file(path):
        try:
            if os.name == "nt":
                os.startfile(path)
                return
            
            if sys.platform == "darwin":
                subprocess.Popen(["open", path])
                return
            
            # Detectar si estamos dentro de Docker
            if os.path.exists("/.dockerenv"):
                # Estamos dentro de Docker, mostrar mensaje con la ruta
                messagebox.showinfo(
                    "PDF Generado", 
                    f"El PDF se ha guardado correctamente.\n\n"
                    f"Ubicación dentro del contenedor: {path}\n\n"
                    f"Puede encontrar el archivo en la carpeta 'Reportes/' de su proyecto.\n"
                    f"Ruta en Windows: C:\\Users\\parce\\PycharmProjects\\PCelMedic python\\Reportes\\\n\n"
                    f"Abra la carpeta manualmente o use el acceso directo."
                )
                return 
            
            # Si no es Windows, ni macOS, ni Docker (Linux nativo)
            subprocess.Popen(["xdg-open", path])
            
        except FileNotFoundError:
            messagebox.showwarning(
                "Aviso", 
                f"No se encontró la utilidad necesaria para abrir archivos.\n\n"
                f"El PDF se ha guardado en: {path}\n\n"
                f"Puede abrirlo manualmente desde la carpeta 'Reportes/'."
            )
        except Exception as e:
            messagebox.showwarning(
                "Aviso", 
                f"El PDF se generó correctamente, pero no se pudo abrir automáticamente.\n\n"
                f"Ubicación: {path}\n"
                f"Carpeta: Reportes/\n\n"
                f"Error: {e}"
            )