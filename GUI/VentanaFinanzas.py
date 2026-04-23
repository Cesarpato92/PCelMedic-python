import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from tkcalendar import DateEntry
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Logica.LogicaFactura import LogicaFactura
from Logica.LogicaCliente import LogicaCliente
from Config.UnitOfWork import UnitOfWork
from DAO.ClienteDAO import ClienteDAO
from DAO.FacturasDAO import FacturasDAO
from openpyxl import Workbook
import datetime

class VentanaFinanzas(tk.Frame):

    def __init__(self, master, controller, **kwargs): 
        
        super().__init__(master, **kwargs) 
        self.controller = controller
        self.logica_factura = LogicaFactura(FacturasDAO())
        self.logica_cliente = LogicaCliente(ClienteDAO())
        
        # Iniciamos en None para el grafico en Matplotlib
        self.fig = None
        self.ax = None
        self.canvas_grafico = None

        # Config grid principal
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # --- Canvas y Scrollbar ---
        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Centrar contenido: Configurar peso en el frame desplazable
        self.scrollable_frame.columnconfigure(0, weight=1)

        # Ajustar el ancho del frame interno al ancho del canvas para que el grid funcione
        def _on_canvas_configure(event):
            self.canvas.itemconfig(self.canvas_window, width=event.width)
        
        self.canvas.bind("<Configure>", _on_canvas_configure)
        
        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

        self.canvas.bind_all("<MouseWheel>", _on_mousewheel)

        parent_frame = self.scrollable_frame

        # Frame Controles - Sin sticky="ew" para que se centre en la columna 0
        self.frame_controles = tk.Frame(parent_frame, bg='plum')
        self.frame_controles.grid(row=0, column=0, padx=10, pady=10)

        # Configurar columnas para centrar
        self.frame_controles.columnconfigure(0, weight=1)
        self.frame_controles.columnconfigure(1, weight=1)
        self.frame_controles.columnconfigure(2, weight=1)
        self.frame_controles.columnconfigure(3, weight=1)

        # Fecha Inicio
        tk.Label(self.frame_controles, text="Fecha Inicio:", bg='plum').grid(row=0, column=0, padx=5, pady=(5,0))
        self.entry_fecha_inicio = DateEntry(self.frame_controles, width=12, background='darkblue',
                                            foreground='white', borderwidth=2, date_pattern='y-mm-dd')
        self.entry_fecha_inicio.grid(row=1, column=0, padx=5, pady=(0,5))

        # Fecha Fin
        tk.Label(self.frame_controles, text="Fecha Fin:", bg='plum').grid(row=0, column=1, padx=5, pady=(5,0))
        self.entry_fecha_fin = DateEntry(self.frame_controles, width=12, background='darkblue',
                                         foreground='white', borderwidth=2, date_pattern='y-mm-dd')
        self.entry_fecha_fin.grid(row=1, column=1, padx=5, pady=(0,5))

        
        try:
            hoy = datetime.date.today()
            inicio_mes = hoy.replace(day=1)
            self.entry_fecha_inicio.set_date(inicio_mes)
            self.entry_fecha_fin.set_date(hoy)
        except Exception:
            pass 
        
        self.btn_generar = ttk.Button(self.frame_controles, text="Generar Gráfico", command=self.generar_grafico)
        self.btn_generar.grid(row=0, column=2, rowspan=2, padx=10, pady=10)
        
        # Botón Exportar Excel
        self.btn_exportar = ttk.Button(self.frame_controles, text="Exportar Clientes (Excel)", command=self.exportar_excel)
        self.btn_exportar.grid(row=0, column=3, rowspan=2, padx=10, pady=10)
        # Boton limpiar
        self.btn_limpiar = ttk.Button(self.frame_controles, text="Limpiar Gráfico", command=self.limpiar_grafico)
        self.btn_limpiar.grid(row=0, column=4, rowspan=2, padx=10, pady=10)
        # Frame Gráfico 
        self.frame_grafico = tk.Frame(parent_frame)
        self.frame_grafico.grid(row=1, column=0, pady=10) 
        self.canvas_grafico = None 
        
        # Frame Datos - Sin sticky="nsew" para que se centre
        self.frame_datos = tk.Frame(parent_frame)
        self.frame_datos.grid(row=2, column=0, padx=10, pady=10)

    def generar_grafico(self):
        fecha_inicio = self.entry_fecha_inicio.get()
        fecha_fin = self.entry_fecha_fin.get()

        if not fecha_inicio or not fecha_fin:
            messagebox.showwarning("Campos vacíos", "Por favor ingrese ambas fechas.")
            return

        # Limpiar gráfico 
        if self.canvas_grafico:
            self.canvas_grafico.get_tk_widget().destroy()
            self.canvas_grafico = None
            
        # Limpiar datos anteriores
        for widget in self.frame_datos.winfo_children():
            widget.destroy()
        try:
            with UnitOfWork() as uow:
                # Obtener datos
                datos = self.logica_factura.obtener_ventas_por_rango(fecha_inicio, fecha_fin, uow.cursor)

                if not datos:
                    messagebox.showinfo("Info", "No se encontraron datos en el rango seleccionado.")
                    return
               

        except Exception as e:
            messagebox.showwarning("Aviso", f"Ocurrió un error al generar el gráfico: {e}")

        #mostrar formato sin hora
        def formato_fecha(d):
            if hasattr(d, 'strftime'):
                return d.strftime('%Y-%m-%d')
            return str(d).split()[0] 

        dias = [formato_fecha(x[0]) for x in datos]
        ventas = [x[1] if x[1] else 0 for x in datos]
        repuestos = [x[2] if x[2] else 0 for x in datos]

        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        
        # Configurar indices para barras agrupadas
        import numpy as np
        x = np.arange(len(dias))
        width = 0.35

        ax.bar(x - width/2, ventas, width, label='Ventas', color='#4CAF50') # Verde
        ax.bar(x + width/2, repuestos, width, label='Repuestos', color='red') # Rojo

        ax.set_title(f"Finanzas ({fecha_inicio} a {fecha_fin})")
        ax.set_ylabel("Monto ($)")
        ax.set_xlabel("Fecha")
        ax.set_xticks(x)
        ax.set_xticklabels(dias)
        ax.legend()
        
        ax.tick_params(axis='x', rotation=45)
        
        fig.tight_layout()

        self.canvas_grafico = FigureCanvasTkAgg(fig, master=self.frame_grafico)
        self.canvas_grafico.draw()
        self.canvas_grafico.get_tk_widget().pack(side=tk.TOP, padx=10, pady=10)
 
        tk.Label(self.frame_datos, text="Detalle de Movimientos:", font=("Arial", 10, "bold")).pack(anchor="center", pady=(10, 5))
  
        frame_lista = tk.Frame(self.frame_datos)
        frame_lista.pack(anchor="center")
        
        # Headers
        tk.Label(frame_lista, text=f"{'Fecha':<12} | {'Ventas':>12} | {'Repuestos':>12}", font=("Consolas", 9, "bold")).pack(anchor="w")

        for dia, venta, repuesto in datos:
            v = venta if venta else 0
            r = repuesto if repuesto else 0
            d_str = formato_fecha(dia)
            lbl = tk.Label(frame_lista, text=f"{d_str:<12} | ${v:>11,.0f} | ${r:>11,.0f}", font=("Consolas", 9))
            lbl.pack(anchor="w")

    def exportar_excel(self):
        try:
            with UnitOfWork() as uow:
                clientes = self.logica_cliente.obtener_todos_clientes(uow.cursor)
                if not clientes:
                    messagebox.showinfo("Cero datos", "No hay clientes registrados para exportar.")
                    return
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener clientes: {e}")
            return

        filename = filedialog.asksaveasfilename(defaultextension=".xlsx", 
                                                filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                                                title="Guardar archivo de clientes")
        if not filename:
            return

        try:
            wb = Workbook()
            ws = wb.active
            ws.title = "Clientes"
            
            ws.append(["Nombre", "Email", "Celular"])
            
            for cliente in clientes:
                ws.append([cliente[0], cliente[1], cliente[2]])
                
            wb.save(filename)
            messagebox.showinfo("Éxito", f"Archivo exportado correctamente en:\n{filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar Excel: {e}")


    def limpiar_grafico(self):
        try:
            # Limpiar el canvas del gráfico
            if hasattr(self, 'canvas_grafico') and self.canvas_grafico:
                self.canvas_grafico.get_tk_widget().destroy()
                self.canvas_grafico = None
            
            # Limpiar la figura
            if hasattr(self, 'fig') and self.fig:
                self.fig.clear()
                import matplotlib.pyplot as plt
                plt.close(self.fig)
                self.fig = None
                self.ax = None
            
            # Limpiar detalles de movimiento
            if hasattr(self, 'frame_datos'):
                # Destruir todos los widgets
                for widget in self.frame_datos.winfo_children():
                    widget.destroy()
            
            # Actualizacion interfaz
            self.update_idletasks()
        except Exception as e:
            messagebox.ERROR("Error", f"Error al limpiar grafico {e}")