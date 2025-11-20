import tkinter as tk
from tkinter import messagebox

# Importar clases de GUI
from GUI.VentanaRegistro import VentanaRegistro
from GUI.VentanaFinanzas import VentanaFinanzas
from GUI.VentanaFactura import VentanaFactura
from GUI.VentanaReparacion import VentanaReparacion
from GUI.VentanaGarantia import VentanaGarantia

from Logica.LogicaCliente import LogicaCliente
from Logica.LogicaDispositivo import LogicaDispositivo
from Logica.LogicaReparacion import LogicaReparacion
from Logica.LogicaFactura import LogicaFactura
from Logica.LogicaGarantia import LogicaGarantia


class VentanaPrincipal(tk.Tk):
   
    
    def __init__(self):
       
        super().__init__()
        
        # Inicializar Lógicas (capa de negocio) con inyección de DAO
        self.cliente_logica = LogicaCliente()
        self.dispositivo_logica = LogicaDispositivo()
        self.reparacion_logica = LogicaReparacion()
        self.factura_logica = LogicaFactura()
        self.garantia_logica =  LogicaGarantia()
              
        
        # Crear fachada de lógica para compatibilidad
        class LogicaFacade:
           # Fachada que expone métodos de negocio a GUI.
            """
            Propósito:
                - Simplificar acceso a métodos de lógica desde GUI
                - Evitar que GUI conozca detalles de instancias específicas
                - Proporcionar interfaz consistente para todos los frames
            
            Métodos:
                - guardarDispositivo(): Delega a dispositivo_logic
                - guardarReparacion(): Delega a reparacion_logic
                - obtener_datos_grafica(): Delega a factura_logic
           """
            def __init__(self, app):
                self.app = app
            # --------------------------------------------------------------------
            # --------------------------------------------------------------------
            def guardarDispositivo(self, *args, **kwargs):
                # Guarda un dispositivo.
                return self.app.dispositivo_logica.agregar_dispositivo(*args, **kwargs)
            
            def guardarReparacion(self, *args, **kwargs):
                # Guarda una reparación.
                return self.app.reparacion_logica.agregar_reparacion(*args, **kwargs)
            
            def obtener_datos_grafica(self, *args, **kwargs):
                # Obtiene datos de facturas para gráfico.
                return self.app.factura_logica.obtener_datos_grafica(*args, **kwargs)
        
        self.logica = LogicaFacade(self)
        self.title("PCelMedic")
        self.geometry("900x700")

        # Creamos la barra superior primero y luego los frames
        self.frames = {}
        self.create_sidebar()

        # Contenedor principal para los frames de contenido
        contenedor = tk.Frame(self)
        contenedor.pack(side="top", fill="both", expand=True)
        contenedor.grid_rowconfigure(0, weight=1)
        contenedor.grid_columnconfigure(0, weight=1)

        # importamos y registramos las clases de los frames
        for F in (VentanaRegistro, VentanaReparacion, VentanaGarantia, VentanaFactura, VentanaFinanzas):
            page_name = F.__name__
            frame = F(parent=contenedor, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        # mostrar el frame inicial 
        self.mostrar_frame("VentanaRegistro")

    def create_sidebar(self):
        """Crea la barra superior (toolbar) con botones de navegación.
        
        Componentes:
            - Etiqueta "PCelMedic" a la izquierda
            - Botones: Clientes, Reparaciones, Garantías, Facturas, Finanzas
            - Botón "Finanzas" requiere autenticación (admin/admin123)
        
        Propósito:
            - Permitir navegación entre secciones
            - Mostrar vista general de funcionalidades
            - Restringir acceso a gráficos mediante login
        """
        # Creamos una barra superior (toolbar) con los botones en fila
        toolbar = tk.Frame(self, bg="#f0f0f0")
        toolbar.pack(side="top", fill="x")

        # Título pequeño a la izquierda
        tk.Label(toolbar, text="PCelMedic", font=("Helvetica", 12, "bold"), bg="#f0f0f0").pack(side="left", padx=(8, 12))

        # Botones de los requerimientos
        btn_clientes = tk.Button(toolbar, text="Registro clientes", command=lambda: self.mostrar_frame("VentanaRegistro"))
        btn_clientes.pack(side="left", padx=6, pady=8)
        btn_reparacion = tk.Button(toolbar, text="Registro reparaciones", command=lambda: self.mostrar_frame("VentanaReparacion"))
        btn_reparacion.pack(side="left", padx=6, pady=8)
        btn_garantias = tk.Button(toolbar, text="Gestión garantías", command=lambda: self.mostrar_frame("VentanaGarantia"))
        btn_garantias.pack(side="left", padx=6, pady=8)
        btn_facturas = tk.Button(toolbar, text="Gestión facturas", command=lambda: self.mostrar_frame("VentanaFactura"))
        btn_facturas.pack(side="left", padx=6, pady=8)
        btn_graficos = tk.Button(toolbar, text="Finanzas", command=lambda: self.validacion_admin())
        btn_graficos.pack(side="left", padx=6, pady=8)

        # Relleno para empujar el contenido principal hacia abajo si fuera necesario
        spacer = tk.Frame(toolbar, bg="#f0f0f0")
        spacer.pack(side="left", expand=True, fill="x")

    def mostrar_frame(self, page_name):
        """Muestra el frame (página) indicado en primer plano.
        
        Args:
            page_name (str): Nombre de la clase del frame (ej: "VentanaDatos", "VentanaGrafico")
        
        Propósito:
            - Cambiar entre diferentes secciones de la aplicación
            - Usar tkraise() para traer el frame al frente (sin recrear)
            - Ejecutar lógica especial para frames (ej: actualizar gráficos, recargar datos)
        
        Flujo especial por frame:
            - VentanaGrafico: Obtiene datos de gráficos automáticamente
            - VentanaReparacion: Carga lista de reparaciones vigentes
            - VentanaFactura: Carga lista de facturas existentes
            - VentanaGarantia: Carga lista de garantías vigentes
            - VentanaDatos: Frame principal de registro
        
        Ejemplo:
            app.mostrar_frame("VentanaGrafico")  # Muestra la ventana de gráficos
        """
        frame = self.frames.get(page_name)
        if frame is None:
            # Si no existe la clave, evitar KeyError y loggear simple
            print(f"Advertencia: no existe el frame '{page_name}'")
            return
        frame.tkraise()
        
        # Lógica especial para cada frame
        if page_name == "VentanaRegistro":
            # Actualizar gráficos cuando se muestre por primera vez
            try:
                datos = self.logica.obtener_datos_grafica()
                if datos:
                    frame.actualizar_graficos(datos)
            except Exception as e:
                print(f"Advertencia: No se pudo actualizar ventana: {e}")
        
        elif page_name == "VentanaReparacion":
            # Recargar reparaciones cuando se abre el frame
            try:
                if hasattr(frame, 'listar_todas'):
                    frame.listar_todas()
            except Exception as e:
                print(f"Advertencia: No se pudo cargar reparaciones: {e}")
        
        elif page_name == "VentanaFactura":
            # Recargar facturas cuando se abre el frame
            try:
                if hasattr(frame, 'listar_todas'):
                    frame.listar_todas()
            except Exception as e:
                print(f"Advertencia: No se pudo cargar facturas: {e}")
        
        elif page_name == "VentanaGarantia":
            # Recargar garantías cuando se abre el frame
            try:
                if hasattr(frame, 'listar_garantias'):
                    frame.listar_garantias()
            except Exception as e:
                print(f"Advertencia: No se pudo cargar garantías: {e}")
        elif page_name == "VentanaFinanzas":
            # Recargar garantías cuando se abre el frame
            try:
                if hasattr(frame, 'listar_finanzas'):
                    frame.listar_finanzas()
            except Exception as e:
                print(f"Advertencia: No se pudo cargar garantías: {e}")

    def validacion_admin(self):
        """Abre un diálogo modal para validar credenciales admin antes de mostrar gráficos.
        
        Propósito:
            - Restringir acceso al módulo de finanzas (gráficos)
            - Requerir autenticación básica (usuario/contraseña)
            - Mostrar VentanaGrafico solo si credenciales son correctas
        
        Credenciales:
            - Usuario: "admin"
            - Contraseña: "admin123"
        
        Flujo:
            1. Crear diálogo modal (Toplevel)
            2. Campos de entrada para usuario y contraseña
            3. Si credenciales correctas: cerrar diálogo + mostrar VentanaFinanzas
            4. Si incorrectas: mostrar error + limpiar campo contraseña
        """
        # Crear diálogo modal
        login = tk.Toplevel(self)
        login.title("Autenticación requerida")
        login.transient(self)
        login.grab_set()
        login.resizable(False, False)

        tk.Label(login, text="Usuario:").grid(row=0, column=0, padx=8, pady=8)
        user_var = tk.StringVar()
        tk.Entry(login, textvariable=user_var).grid(row=0, column=1, padx=8, pady=8)

        tk.Label(login, text="Contraseña:").grid(row=1, column=0, padx=8, pady=8)
        pwd_var = tk.StringVar()
        tk.Entry(login, textvariable=pwd_var, show="*").grid(row=1, column=1, padx=8, pady=8)

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

        def on_cancel():
            """Cierra el diálogo sin autenticar."""
            login.destroy()

        btn_ok = tk.Button(login, text="Ingresar", command=on_ok)
        btn_ok.grid(row=2, column=0, padx=8, pady=10)
        btn_cancel = tk.Button(login, text="Cancelar", command=on_cancel)
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
            # Si algo falla al centrar, no bloqueamos la ventana
            pass

        # Esperar a que se cierre el diálogo (modal)
        self.wait_window(login)


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()