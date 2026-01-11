import tkinter
from tkinter import messagebox, ttk
from datetime import datetime 
import os
from Modelo.ModeloGarantia import ModeloGarantia
from Logica.LogicaCliente import LogicaCliente
from Logica.LogicaDispositivo import LogicaDispositivo
from Logica.LogicaReparacion import LogicaReparacion
from Logica.LogicaGarantia import LogicaGarantia
from Logica.GeneradorPDF import GeneradorPDF

class VentanaEntradaGarantia(tkinter.Frame):

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        # Inicializamos los objetos de cliente, reparacion, dispositivo y garantia
        self.cliente = LogicaCliente()
        self.reparacion = LogicaReparacion()
        self.dispositivo = LogicaDispositivo()
        self.garantia = LogicaGarantia()
        self.generador_pdf = GeneradorPDF()
        
        # Objetos para almacenar los modelos actuales
        self.cliente_obj = None
        self.dispositivo_obj = None
        self.reparacion_obj = None

        # Contenedor principal del frame
        contenedor = ttk.Frame(self, padding="10")
        contenedor.grid(row=0, column=0, sticky="nsew")

        #Configuraciones de expacion para el frame principal y el contenedor
        self.columnconfigure(0, weight=1) 
        self.rowconfigure(0, weight=1)
        contenedor.columnconfigure(0, weight=1, uniform="equal_columns")
        contenedor.columnconfigure(1, weight=1, uniform="equal_columns")
        contenedor.columnconfigure(2, weight=1, uniform="equal_columns")

        # El título abarca las 3 columnas 
        ttk.Label(contenedor, text="Registro", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=3, pady=10)

        # Seccion de busqueda de ID de reparacion 
        contenedor_id_reparacion = ttk.Frame(contenedor)
        contenedor_id_reparacion.grid(row=1, column=0, columnspan=3, pady=10, sticky="w")
        
        ttk.Label(contenedor_id_reparacion, text="ID Reparacion:").grid(row=0, column=0, sticky="w")
                
        id_rep_frame = ttk.Frame(contenedor_id_reparacion)
        id_rep_frame.grid(row=0, column=1, pady=5, sticky="w", padx=10)
        id_rep_frame.columnconfigure(0, weight=1) 
        
        self.entrada_id_reparacion = ttk.Entry(id_rep_frame, width=20)
        self.entrada_id_reparacion.grid(row=0, column=0, sticky="ew")
        
        ttk.Button(id_rep_frame, text="Buscar", command=self.buscar_id_reparacion).grid(row=0, column=1, padx=5)

        
        # Columna izquierda - Datos del cliente 
        contenido_izquierda = ttk.Frame(contenedor, padding="10", relief="groove")
        contenido_izquierda.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        contenido_izquierda.columnconfigure(0, weight=1)

        ttk.Label(contenido_izquierda, text="Datos del Cliente", font=("Helvetica", 14, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        ttk.Label(contenido_izquierda, text="Cedula:").grid(row=1, column=0, sticky="w")
        cedula_frame = ttk.Frame(contenido_izquierda)
        cedula_frame.grid(row=2, column=0, sticky="ew", pady=5)
        cedula_frame.columnconfigure(0, weight=1)

        self.entrada_cedula = ttk.Entry(cedula_frame, width=20) 
        self.entrada_cedula.grid(row=0, column=0, sticky="ew") 
               
        ttk.Label(contenido_izquierda, text="Nombre").grid(row=3, column=0, sticky="w", pady=(8, 0)) 
        self.entrada_nombre = ttk.Entry(contenido_izquierda) 
        self.entrada_nombre.grid(row=4, column=0, sticky="ew", pady=3)

        ttk.Label(contenido_izquierda, text="Email").grid(row=5, column=0, sticky="w", pady=(8, 0)) 
        self.entrada_email = ttk.Entry(contenido_izquierda) 
        self.entrada_email.grid(row=6, column=0, sticky="ew", pady=3)

        ttk.Label(contenido_izquierda, text="Celular").grid(row=7, column=0, sticky="w", pady=(8, 0))
        self.entrada_celular = ttk.Entry(contenido_izquierda) 
        self.entrada_celular.grid(row=8, column=0, sticky="ew", pady=3)

        # Columna central: datos del equipo (Fila 2, Columna 1)
        contenido_centro = ttk.Frame(contenedor, padding="10", relief="groove")
        contenido_centro.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
        contenido_centro.columnconfigure(0, weight=1)

        ttk.Label(contenido_centro, text="Datos del equipo", font=("Helvetica", 14, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 5))

        ttk.Label(contenido_centro, text="Marca").grid(row=1, column=0, sticky="w", pady=(5, 0))
        self.entrada_marca = ttk.Entry(contenido_centro) 
        self.entrada_marca.grid(row=2, column=0, sticky="ew", pady=3)

        ttk.Label(contenido_centro, text="Modelo").grid(row=3, column=0, sticky="w", pady=(5, 0))
        self.entrada_modelo = ttk.Entry(contenido_centro) 
        self.entrada_modelo.grid(row=4, column=0, sticky="ew", pady=3)

        ttk.Label(contenido_centro, text="Tipo de reparación").grid(row=5, column=0, sticky="w", pady=(5, 0))
        self.entrada_tipo_rep = ttk.Entry(contenido_centro) 
        self.entrada_tipo_rep.grid(row=6, column=0, sticky="ew", pady=3)

        ttk.Label(contenido_centro, text="Tipo de contraseña").grid(row=7, column=0, sticky="w", pady=(5, 0))
        self.entrada_tipo_password = ttk.Entry(contenido_centro) 
        self.entrada_tipo_password.grid(row=8, column=0, sticky="ew", pady=3)

        ttk.Label(contenido_centro, text="Contraseña del equipo").grid(row=9, column=0, sticky="w", pady=(5, 0))
        self.entrada_password = ttk.Entry(contenido_centro) 
        self.entrada_password.grid(row=10, column=0, sticky="ew", pady=3)

        
        ttk.Label(contenido_centro, text="Precio de reparación").grid(row=11, column=0, sticky="w", pady=(5, 0))
        self.entrada_precio = ttk.Entry(contenido_centro) 
        self.entrada_precio.grid(row=12, column=0, sticky="ew", pady=3)

       
        ttk.Label(contenido_centro, text="Fecha ingreso").grid(row=13, column=0, sticky="w", pady=(5, 0))
        self.entrada_ingreso = ttk.Entry(contenido_centro) 
        self.entrada_ingreso.grid(row=14, column=0, sticky="ew", pady=3)
        
        ttk.Label(contenido_centro, text="Comentarios de ingreso", font=("Helvetica", 12, "bold")).grid(row=15, column=0, sticky="w", pady=(5, 0))
        self.entrada_comentarios = tkinter.Text(contenido_centro, height=6) 
        self.entrada_comentarios.grid(row=16, column=0, sticky="nsew", pady=3)

        # Columna derecha: comentarios y estado (Fila 2, Columna 2)
        contenido_derecha_der = ttk.Frame(contenedor, padding="10", relief="groove")
        contenido_derecha_der.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)
        contenido_derecha_der.columnconfigure(0, weight=1)

        ttk.Label(contenido_derecha_der, text="Comentarios de tecnico de reparacion", font=("Helvetica", 12, "bold")).grid(row=0, column=0, sticky="w", pady=(5, 0))
        self.entrada_comentarios_tec = tkinter.Text(contenido_derecha_der, height=6) 
        self.entrada_comentarios_tec.grid(row=1, column=0, sticky="nsew", pady=3)

        ttk.Label(contenido_derecha_der, text="Estado").grid(row=2, column=0, sticky="w", pady=(5,0))
        self.entrada_estado = ttk.Entry(contenido_derecha_der)       
        self.entrada_estado.grid(row=3, column=0, sticky="w", pady=3)
        
        ttk.Label(contenido_derecha_der, text="¿Equipo reparado?").grid(row=4, column=0, sticky="w", pady=(5, 0))
        opciones_rep = ["SI", "NO"]
        self.var_tipo_rep = tkinter.StringVar(self) 
        self.var_tipo_rep.set(opciones_rep[0]) # Set initial value to "SI"

        self.entrada_tipo = ttk.Combobox(contenido_derecha_der, 
                                         textvariable=self.var_tipo_rep,
                                         values=opciones_rep,
                                         state="readonly",
                                         width=8)
        self.entrada_tipo.grid(row=5, column=0, sticky="w", pady=3)
       
        ttk.Label(contenido_derecha_der, text="Precio refaccion").grid(row=6, column=0, sticky="w", pady=(5,0))
        self.entrada_refaccion = ttk.Entry(contenido_derecha_der)
        self.entrada_refaccion.grid(row=7, column=0, sticky="w", pady=3)
       
        ttk.Label(contenido_derecha_der, text="Comentarios de garantia", font=("Helvetica", 14, "bold")).grid(row=8, column=0, sticky="w", pady=(5, 0))
        self.entrada_comentarios_gar = tkinter.Text(contenido_derecha_der, height=6) 
        self.entrada_comentarios_gar.grid(row=9, column=0, sticky="nsew", pady=3)
        
        
        
        contenido_derecha_der.rowconfigure(1, weight=1) 
        contenido_derecha_der.rowconfigure(7, weight=1) 


        # Footer: Contenedor para los botones 
        footer_frame = ttk.Frame(contenedor, padding="10", relief="raised")
        footer_frame.grid(row=3, column=0, columnspan=3, sticky="nsew", pady=(20, 0))
        
        # Configuramos el footer con 3 columnas que se expanden proporcionalmente
        footer_frame.columnconfigure(0, weight=1)
        footer_frame.columnconfigure(1, weight=1)
        footer_frame.columnconfigure(2, weight=1)
        
        # Botones Izquierda 
        #frame_btn_izquierda = ttk.Frame(footer_frame)
        #frame_btn_izquierda.grid(row=0, column=0, sticky="w")        
        
       # ttk.Button(frame_btn_izquierda, text="Limpiar", command=lambda: self.btn_limpiar()).grid(row=0, column=0, padx=5, pady=5)
        
        # Botones Centro 
        frame_btn_centro = ttk.Frame(footer_frame)
        frame_btn_centro.grid(row=0, column=1, sticky="nsew")
        
        frame_btn_centro.columnconfigure(0, weight=1)
        self.Btn_guardar = ttk.Button(frame_btn_centro, text="Insertar", command=lambda: self.btn_guardar())
        self.Btn_guardar.grid(row=0, column=0, sticky="ew", padx=5, pady=5) 
        
        # Botones Derecha 

        frame_btn_derecha = ttk.Frame(footer_frame)
        frame_btn_derecha.grid(row=0, column=2, sticky="e")        
       
        ttk.Button(frame_btn_derecha, text="Cancelar", command=lambda: self.btn_cancelar()).grid(row=0, column=2, padx=5, pady=5)

        self.deshabilitar_entradas()
        self.entrada_id_reparacion.focus()


    # Metodo de verificacion de id reparacion
    def verificar_id_reparacion(self):
        id_rep = self.entrada_id_reparacion.get().strip()
        if not id_rep:
            messagebox.showwarning("Atencion", "El campo de ID reparacion es obligatorio y no puede estar vacio")
            return False
        return True
    
    def buscar_id_reparacion(self):
        if not self.verificar_id_reparacion():
            return

        id_rep = self.entrada_id_reparacion.get().strip()
        
        try:
            reparacion_obj = self.reparacion.obtener_reparacion_por_id(id_rep)
            
            if not reparacion_obj:
                messagebox.showinfo("No encontrado", "No se encontró ninguna reparación con ese ID")
                return

            # Obtener dispositivo
            dispositivo_obj = self.dispositivo.obtener_dispositivo_por_id(reparacion_obj.id_dispositivo)
            if not dispositivo_obj:
                messagebox.showerror("Error", "No se encontró el dispositivo asociado a la reparación")
                return

            # Obtener cliente
            cliente_obj = self.cliente.obtener_cliente_por_cedula(dispositivo_obj.id_cliente)
            if not cliente_obj:
                messagebox.showerror("Error", "No se encontró el cliente asociado al dispositivo")
                return

            # Llenar campos
            self.btn_limpiar(mantener_id=True)
            
            # Guardar objetos en variables de instancia para uso posterior (PDF)
            self.cliente_obj = cliente_obj
            self.dispositivo_obj = dispositivo_obj
            self.reparacion_obj = reparacion_obj
            
            # Cliente
            self.entrada_cedula.config(state="normal")
            self.entrada_cedula.insert(0, cliente_obj.cedula)
            self.entrada_cedula.config(state="disabled")
            
            self.entrada_nombre.config(state="normal")
            self.entrada_nombre.insert(0, cliente_obj.nombre)
            self.entrada_nombre.config(state="disabled")
            
            self.entrada_email.config(state="normal")
            self.entrada_email.insert(0, cliente_obj.email)
            self.entrada_email.config(state="disabled")
            
            self.entrada_celular.config(state="normal")
            self.entrada_celular.insert(0, cliente_obj.celular)
            self.entrada_celular.config(state="disabled")

            # Dispositivo
            self.entrada_marca.config(state="normal")
            self.entrada_marca.insert(0, dispositivo_obj.marca)
            self.entrada_marca.config(state="disabled")
            
            self.entrada_modelo.config(state="normal")
            self.entrada_modelo.insert(0, dispositivo_obj.version)
            self.entrada_modelo.config(state="disabled")
            
            self.entrada_tipo_rep.config(state="normal")
            self.entrada_tipo_rep.insert(0, dispositivo_obj.tipo_reparacion)
            self.entrada_tipo_rep.config(state="disabled")
            
            self.entrada_tipo_password.config(state="normal")
            self.entrada_tipo_password.insert(0, dispositivo_obj.tipo_password)
            self.entrada_tipo_password.config(state="disabled")
            
            self.entrada_password.config(state="normal")
            self.entrada_password.insert(0, dispositivo_obj.password or "N/A")
            self.entrada_password.config(state="disabled")

            self.entrada_comentarios.config(state="normal")
            self.entrada_comentarios.insert("1.0", dispositivo_obj.comentarios)
            self.entrada_comentarios.config(state="disabled")

            # Reparacion
            self.entrada_precio.config(state="normal")
            self.entrada_precio.insert(0, reparacion_obj.precio_reparacion)
            self.entrada_precio.config(state="disabled")
            
            self.entrada_ingreso.config(state="normal")
            self.entrada_ingreso.insert(0, reparacion_obj.fecha_ingreso)
            self.entrada_ingreso.config(state="disabled")
            
            self.entrada_comentarios_tec.config(state="normal")
            self.entrada_comentarios_tec.insert("1.0", reparacion_obj.comentarios)
            self.entrada_comentarios_tec.config(state="disabled")
            
            self.entrada_estado.config(state="normal")
            self.entrada_estado.insert(0, reparacion_obj.estado)
            self.entrada_estado.config(state="disabled")
            
            self.entrada_refaccion.config(state="normal")
            self.entrada_refaccion.insert(0, reparacion_obj.costo_repuestos)
            self.entrada_refaccion.config(state="disabled")
            
            self.entrada_tipo.config(state="disabled")
            
            # Habilitar campos de entrada de garantía
            self.entrada_comentarios_gar.config(state="normal")
            self.Btn_guardar.config(state="normal")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar: {e}")

    def btn_guardar(self):
        id_rep = self.entrada_id_reparacion.get().strip()
        if not id_rep:
            messagebox.showwarning("Atención", "Debe buscar una reparación primero")
            return

        comentarios_gar = self.entrada_comentarios_gar.get("1.0", "end-1c").strip()
        equipo_reparado = self.var_tipo_rep.get()

        if not comentarios_gar:
            messagebox.showwarning("Atención", "Debe ingresar comentarios de la garantia")
            return

        try:
            modelo_garantia = ModeloGarantia()
            modelo_garantia.id_reparacion = id_rep
            modelo_garantia.fecha_inicio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            modelo_garantia.observaciones = comentarios_gar
            modelo_garantia.estado = "En Garantia" if equipo_reparado == "SI" else "Rechazada"
            
                        
            id_garantia = self.garantia.agregar_garantia(modelo_garantia)
            
            if id_garantia:
                modelo_garantia.id_garantia = id_garantia
                messagebox.showinfo("Éxito", f"Garantía registrada con ID: {id_garantia}")
                
                # Verificar asegurarnos que tenemos los objetos necesarios
                if self.cliente_obj and self.dispositivo_obj and self.reparacion_obj:
                    ruta = self.generador_pdf.generar_reporte_garantia(self.cliente_obj, self.dispositivo_obj, self.reparacion_obj, modelo_garantia)
                    os.startfile(ruta)
                else:
                    print("Error: Objetos de datos faltantes para generar PDF")
                
                self.btn_limpiar()

            else:
                messagebox.showerror("Error", "No se pudo registrar la garantía, error ocurrido")

        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar garantía: {e}")

    def btn_limpiar(self, mantener_id=False):
        if not mantener_id:
            self.entrada_id_reparacion.delete(0, "end")
            self.cliente_obj = None
            self.dispositivo_obj = None
            self.reparacion_obj = None
        
        campos_entry = [
            self.entrada_cedula, self.entrada_nombre, self.entrada_email, self.entrada_celular,
            self.entrada_marca, self.entrada_modelo, self.entrada_tipo_rep, self.entrada_tipo_password,
            self.entrada_password, self.entrada_precio, self.entrada_ingreso, self.entrada_estado,
            self.entrada_refaccion
        ]
        
        for campo in campos_entry:
            campo.config(state="normal")
            campo.delete(0, "end")
            campo.config(state="disabled")
            
        self.entrada_comentarios.config(state="normal")
        self.entrada_comentarios.delete("1.0", "end")
        self.entrada_comentarios.config(state="disabled")
        
        self.entrada_comentarios_tec.config(state="normal") 
        self.entrada_comentarios_tec.delete("1.0", "end")
        self.entrada_comentarios_tec.config(state="disabled") 

        self.entrada_comentarios_gar.config(state="normal") 
        self.entrada_comentarios_gar.delete("1.0", "end")
        self.entrada_comentarios_gar.config(state="disabled") 

        self.var_tipo_rep.set("SI")
        self.entrada_tipo.config(state="disabled") 
        self.Btn_guardar.config(state="disabled") 
        
    def btn_cancelar(self):
        self.btn_limpiar()
        

    def deshabilitar_entradas(self):
        self.entrada_cedula.config(state="disabled") 
        self.entrada_nombre.config(state="disabled") 
        self.entrada_email.config(state="disabled") 
        self.entrada_celular.config(state="disabled") 
        self.entrada_modelo.config(state="disabled") 
        self.entrada_marca.config(state="disabled") 
        self.entrada_tipo_rep.config(state="disabled") 
        self.entrada_tipo_password.config(state="disabled") 
        self.entrada_password.config(state="disabled") 
        self.entrada_precio.config(state="disabled") 
        self.entrada_comentarios.config(state="disabled") 
        self.entrada_estado.config(state="disabled")
        self.entrada_ingreso.config(state="disabled")
        self.entrada_refaccion.config(state="disabled")
        self.entrada_comentarios_tec.config(state="disabled") 
        self.entrada_tipo.config(state="disabled") 
        self.Btn_guardar.config(state="disabled") 