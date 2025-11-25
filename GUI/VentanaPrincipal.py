import tkinter as tk
from tkinter import messagebox, ttk

# Importar clases de GUI 
from GUI.VentanaRegistro import VentanaRegistro
from GUI.VentanaReparacion import VentanaReparacion
from GUI.VentanaGarantia import VentanaGarantia
from GUI.VentanaFactura import VentanaFactura
from GUI.VentanaFinanzas import VentanaFinanzas

class VentanaPrincipal(tk.Tk):
   
    def __init__(self):
        super().__init__()
        
        self.title("PCelMedic")
        self.geometry("900x700")
        self.state('zoomed') 
       
        self.resizable(True, True) 
        
        # Define un estilo para la navbar 
        style = ttk.Style()
        style.configure("Navbar.TFrame", background="#f0f0f0")
        style.configure("Navbar.TLabel", background="#f0f0f0", font=("Helvetica", 12, "bold"))

        # --- Configuración del Layout Principal 
        # Fila 0 para la navbar, Fila 1 para el contenido principal
        self.grid_rowconfigure(1, weight=1)       # La fila de contenido se expande verticalmente
        self.grid_columnconfigure(0, weight=1)    # La única columna se expande horizontalmente

        # Creamos la barra superior (navbar) usando grid
        self.crear_navbar()

        # Contenedor principal para los frames de contenido
        self.contenedor = tk.Frame(self, bg="white")
        # Ubicamos el contenedor en la Fila 1, Columna 0, expandiéndose en todas direcciones
        self.contenedor.grid(row=1, column=0, sticky="nsew")
        self.contenedor.grid_rowconfigure(0, weight=1)
        self.contenedor.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (VentanaRegistro, VentanaReparacion, VentanaGarantia, VentanaFactura, VentanaFinanzas):
            page_name = F.__name__
            # Usamos argumento posicional para el maestro, como se indicó en la solución anterior
            frame = F(self.contenedor, controller=self) 
            self.frames[page_name] = frame
            # Apilamos todos los frames en la misma celda del grid del contenedor
            frame.grid(row=0, column=0, sticky="nsew")
        
        # mostrar el frame inicial 
        self.mostrar_frame("VentanaRegistro")

    def crear_navbar(self):
        
        # Usamos el estilo definido
        navbar = ttk.Frame(self, height=50, style="Navbar.TFrame") 
        navbar.grid(row=0, column=0, sticky="ew")

        # Usamos el estilo definido para la etiqueta
        ttk.Label(navbar, text="PCelMedic", style="Navbar.TLabel").pack(side="left", padx=(8, 12))

        # Botones de los requerimientos (están bien con pack y ttk.Button)
        ttk.Button(navbar, text="Registro clientes", command=lambda: self.mostrar_frame("VentanaRegistro")).pack(side="left", padx=6, pady=8)
        ttk.Button(navbar, text="Registro reparaciones", command=lambda: self.mostrar_frame("VentanaReparacion")).pack(side="left", padx=6, pady=8)
        ttk.Button(navbar, text="Gestión garantías", command=lambda: self.mostrar_frame("VentanaGarantia")).pack(side="left", padx=6, pady=8)
        ttk.Button(navbar, text="Gestión facturas", command=lambda: self.mostrar_frame("VentanaFactura")).pack(side="left", padx=6, pady=8)
        ttk.Button(navbar, text="Finanzas", command=lambda: self.validacion_admin()).pack(side="left", padx=6, pady=8)

    def mostrar_frame(self, page_name):
        # Muestra el frame para le nombre de la pagina dado
        frame = self.frames.get(page_name)
        if frame:
            frame.tkraise()
        else:
            messagebox.showerror("Error de navegación", f"No se encontró el frame: {page_name}")

    def validacion_admin(self):
        
        # Creacion de la ventana de autenticacion
        login = tk.Toplevel(self) # Correcto, Toplevel es tk.
        login.title("Autenticación requerida")
        login.transient(self)
        login.grab_set()
        login.resizable(False, False)

        # Todos estos widgets ya son ttk, lo cual es correcto:
        ttk.Label(login, text="Usuario:").grid(row=0, column=0, padx=8, pady=8)
        user_var = tk.StringVar() # Usamos tk.StringVar o ttk.StringVar, ambos funcionan con ttk Entry
        ttk.Entry(login, textvariable=user_var).grid(row=0, column=1, padx=8, pady=8)

        ttk.Label(login, text="Contraseña:").grid(row=1, column=0, padx=8, pady=8)
        pwd_var = tk.StringVar()
        ttk.Entry(login, textvariable=pwd_var, show="*").grid(row=1, column=1, padx=8, pady=8)

        def on_ok():
            """Valida credenciales y abre VentanaFinanzas si son correctas."""
            user = user_var.get().strip()
            pwd = pwd_var.get()
            if user == "admin" and pwd == "admin123":
                login.destroy()
                self.mostrar_frame("VentanaFinanzas")
            else:
                messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos")
                pwd_var.set("")
        
        btn_ok = ttk.Button(login, text="Ingresar", command=on_ok)
        btn_ok.grid(row=2, column=0, padx=8, pady=10)

        def on_cancel():
            """Cierra el diálogo sin autenticar."""
            login.destroy()

        btn_ok = ttk.Button(login, text="Ingresar", command=on_ok)
        btn_ok.grid(row=2, column=0, padx=8, pady=10)
        btn_cancel = ttk.Button(login, text="Cancelar", command=on_cancel)
        btn_cancel.grid(row=2, column=1, padx=8, pady=10)

        # Centrar el diálogo en el centro de la pantalla
        try:
            login.update_idletasks()
            w = login.winfo_width()
            h = login.winfo_height()
            sw = login.winfo_screenwidth()
            sh = login.winfo_screenheight()
            x = (sw // 2) - (w // 2)
            y = (sh // 2) - (h // 2)
            login.geometry(f"{w}x{h}+{x}+{y}")
        except Exception:
            pass

        self.wait_window(login)
