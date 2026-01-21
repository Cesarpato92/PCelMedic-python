import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Logica.LogicaFactura import LogicaFactura
import datetime

class VentanaFinanzas(tk.Frame):

    def __init__(self, master, controller, **kwargs): 
        # Pasamos 'master' como argumento posicional al super constructor
        super().__init__(master, **kwargs) 
        self.controller = controller
        self.logica_factura = LogicaFactura()
        
        # Config grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1) # weight para que expande el gráfico infinitamente

        # --- Frame Controles ---
        self.frame_controles = tk.Frame(self, bg='plum')
        self.frame_controles.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        # Configurar columnas para centrar
        self.frame_controles.columnconfigure(0, weight=1)
        self.frame_controles.columnconfigure(1, weight=1)
        self.frame_controles.columnconfigure(2, weight=1)

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

        # Valores por defecto
        try:
            hoy = datetime.date.today()
            inicio_mes = hoy.replace(day=1)
            self.entry_fecha_inicio.set_date(inicio_mes)
            self.entry_fecha_fin.set_date(hoy)
        except Exception:
            pass 

        # Botón
        self.btn_generar = ttk.Button(self.frame_controles, text="Generar Gráfico", command=self.generar_grafico)
        self.btn_generar.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

        # --- Frame Gráfico ---
        self.frame_grafico = tk.Frame(self)
        self.frame_grafico.grid(row=1, column=0, pady=10) # sticky removido para centrar y no estirar
        self.canvas = None
        
        # --- Frame Datos ---
        self.frame_datos = tk.Frame(self)
        self.frame_datos.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

    def generar_grafico(self):
        fecha_inicio = self.entry_fecha_inicio.get()
        fecha_fin = self.entry_fecha_fin.get()

        if not fecha_inicio or not fecha_fin:
            messagebox.showwarning("Campos vacíos", "Por favor ingrese ambas fechas.")
            return

        # Limpiar gráfico anterior si existe
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None
            
        # Limpiar datos anteriores
        for widget in self.frame_datos.winfo_children():
            widget.destroy()

        # Obtener datos
        datos = self.logica_factura.obtener_ventas_por_rango(fecha_inicio, fecha_fin)

        if not datos:
            messagebox.showinfo("Info", "No se encontraron datos en el rango seleccionado.")
            return

        # Procesar datos
        # datos es una lista de tuplas [(dia, total), ...]
        dias = [str(x[0]) for x in datos]
        montos = [x[1] for x in datos]

        # Crear figura más pequeña
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        
        ax.bar(dias, montos, color='#4CAF50')
        ax.set_title(f"Ventas por Día ({fecha_inicio} a {fecha_fin})")
        ax.set_ylabel("Total Ventas")
        ax.set_xlabel("Fecha")
        ax.tick_params(axis='x', rotation=45)
        
        fig.tight_layout()

        # Dibujar en Canvas (sin expandir para respetar tamaño definido)
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame_grafico)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, padx=10, pady=10)
        
        # Generar Labels con datos
        tk.Label(self.frame_datos, text="Detalle de Ventas:", font=("Arial", 10, "bold")).pack(anchor="center", pady=(10, 5))
        
        # Frame scrollable o lista simple? Lista simple centrada por ahora
        frame_lista = tk.Frame(self.frame_datos)
        frame_lista.pack(anchor="center")
        
        for dia, total in datos:
            lbl = tk.Label(frame_lista, text=f"Fecha: {dia}  |  Total: ${total:,.0f}")
            lbl.pack(anchor="w")
