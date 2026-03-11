import tkinter as tk
from tkinter import messagebox, ttk
from Modelo.ModeloCliente import ModeloCliente
from Modelo.ModeloDispositivo import ModeloDispositivo
from Modelo.ModeloReparacion import ModeloReparacion

from Logica.LogicaCliente import LogicaCliente
from Logica.LogicaDispositivo import LogicaDispositivo
from Logica.LogicaReparacion import LogicaReparacion
from Logica.Conexion import Conexion

class VentanaReparacion(tk.Frame):
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs) 
        self.controller = controller

        # Inicializamos los objetos cliente, reparacion y dispositivo
        self.cliente =  LogicaCliente()
        self.dispositivo =  LogicaDispositivo()
        self.reparacion = LogicaReparacion()

        # Contenedor Principal de Contenido 
        contenedor = ttk.Frame(self, padding="10")
        contenedor.grid(row=0, column=0, sticky="nsew")
        
        # Configuraciones de expansión para el frame principal y el contenedor
        self.columnconfigure(0, weight=1) 
        self.rowconfigure(0, weight=1)
        contenedor.columnconfigure(0, weight=1)
        contenedor.columnconfigure(1, weight=1)
        contenedor.columnconfigure(2, weight=1)
                
        # El título abarca las 3 columnas 
        ttk.Label(contenedor, text="Gestión de reparaciones", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=3, pady=10)

        # Sección de ID de Reparación y Búsqueda 
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

        # Columna derecha: comentarios y estado (Fila 2, Columna 2)
        contenido_derecha_der = ttk.Frame(contenedor, padding="10", relief="groove")
        contenido_derecha_der.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)
        contenido_derecha_der.columnconfigure(0, weight=1)

        ttk.Label(contenido_derecha_der, text="Comentarios al recibir el equipo", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", pady=(5, 0))
        self.entrada_comentarios = tk.Text(contenido_derecha_der, height=6) 
        self.entrada_comentarios.grid(row=1, column=0, sticky="nsew", pady=3)

        ttk.Label(contenido_derecha_der, text="Estado").grid(row=2, column=0, sticky="w", pady=(5,0))
        self.entrada_estado = ttk.Entry(contenido_derecha_der)       
        self.entrada_estado.grid(row=3, column=0, sticky="w", pady=3)
        
        ttk.Label(contenido_derecha_der, text="Precio refaccion").grid(row=4, column=0, sticky="w", pady=(5,0))
        self.entrada_refaccion = ttk.Entry(contenido_derecha_der)
        self.entrada_refaccion.grid(row=5, column=0, sticky="w", pady=3)
       
        ttk.Label(contenido_derecha_der, text="Comentarios del tecnico").grid(row=6, column=0, sticky="w", pady=(5, 0))
        self.entrada_comentarios_tec = tk.Text(contenido_derecha_der, height=6) 
        self.entrada_comentarios_tec.grid(row=7, column=0, sticky="nsew", pady=3)
        
        ttk.Label(contenido_derecha_der, text="¿Equipo reparado?").grid(row=8, column=0, sticky="w", pady=(5, 0))
        opciones_rep = ["SI", "NO"]
        self.var_tipo_rep = tk.StringVar(self) 
        self.var_tipo_rep.set(opciones_rep) 
        self.var_tipo_rep.set(opciones_rep[0])

        self.entrada_tipo = ttk.Combobox(contenido_derecha_der, 
                                         textvariable=self.var_tipo_rep,
                                         values=opciones_rep,
                                         state="readonly",
                                         width=8)
        self.entrada_tipo.grid(row=9, column=0, sticky="w", pady=3)
        
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
        frame_btn_izquierda = ttk.Frame(footer_frame)
        frame_btn_izquierda.grid(row=0, column=0, sticky="w")        
        
        ttk.Button(frame_btn_izquierda, text="Limpiar", command=lambda: self.btn_limpiar()).grid(row=0, column=0, padx=5, pady=5)
        
        # Botones Centro 
        frame_btn_centro = ttk.Frame(footer_frame)
        frame_btn_centro.grid(row=0, column=1, sticky="nsew")
        
        frame_btn_centro.columnconfigure(0, weight=1)
        self.Btn_guardar = ttk.Button(frame_btn_centro, text="Guardar", command=lambda: self.btn_guardar())
        self.Btn_guardar.grid(row=0, column=0, sticky="ew", padx=5, pady=5) 
        
        # Botones Derecha 
        frame_btn_derecha = ttk.Frame(footer_frame)
        frame_btn_derecha.grid(row=0, column=2, sticky="e")        
       
        ttk.Button(frame_btn_derecha, text="Cancelar", command=lambda: self.cancelar_accion()).grid(row=0, column=2, padx=5, pady=5)

        self.deshabilitar_entradas()
        self.entrada_id_reparacion.focus()
        


    # Metodo de verificacion de id reparacion
    def verificar_id_reparacion(self):
        id_rep = self.entrada_id_reparacion.get().strip()
        if not id_rep:
            messagebox.showwarning("Atencion", "El campo de ID reparacion es obligatorio y no puede estar vacio")
            return False
        return True

    # Métodos de la clase 
    def btn_guardar(self):
        id_reparacion = self.entrada_id_reparacion.get().strip()
        comen_tec = self.entrada_comentarios_tec.get("1.0", tk.END).strip()
        costo_refaccion = self.entrada_refaccion.get().strip()

                            
        # Validaciones 
        if not comen_tec: 
            messagebox.showwarning("Advertencia", "El campo de comentarios es obligatorio y no puede estar vacío")
            return
                
        if not costo_refaccion:  
            messagebox.showwarning("Advertencia", "El campo de costo de repuestos es obligatorio y no puede estar vacío")
            return
            
        # Validar que el costo sea numérico
        try:
            costo_float = float(costo_refaccion)
            if costo_float < 0:
                messagebox.showwarning("Advertencia", "El costo de repuestos no puede ser negativo")
                return
        except ValueError:
                messagebox.showwarning("Advertencia", "El campo de costo de repuestos debe ser un número válido")
                return
        
        if self.var_tipo_rep.get() == "NO":
                messagebox.showwarning("Advertencia", "Debe seleccionar si el equipo fue reparado o no")
                return

        # Conectamos a la BD
        conexion = Conexion.get_conexion()
        # Verificamos que no haya una conexion en curso
        if not conexion.in_transaction:
            conexion.start_transaction()
        else:
            # Si ya hay una hacemos rollback para limpiar
            conexion.rollback()
            conexion.start_transaction()
        # iniciamos el cursor
        cursor = conexion.cursor()
       
        try:
            # Crear y configurar el objeto
            reparacion_obj = ModeloReparacion()
            reparacion_obj.id_reparacion = id_reparacion
            reparacion_obj.comentarios = comen_tec
            reparacion_obj.costo_repuestos = costo_float
            reparacion_obj.estado = "Completada"
                
            # Llamar al método de actualización
            resultado = self.reparacion.actualizar_estado_reparacion(reparacion_obj, cursor)
                
            if resultado:
                # Aceptamos la transaccion
                conexion.commit()
                messagebox.showinfo("Éxito", "Reparación actualizada exitosamente.")
                self.btn_limpiar()
                self.deshabilitar_entradas()
                
                    
        except Exception as e:
            conexion.rollback()
            messagebox.showerror("Error", f"No se pudo actualizar la reparación. Error: {str(e)}")
        finally:
            if cursor:
                cursor.close()

    def buscar_id_reparacion(self):
        if not self.verificar_id_reparacion():
            return

        id_rep = self.entrada_id_reparacion.get().strip()
        
        # Limpiar campos antes de buscar
        self.limpiar_campos()
        # Conectamos a la BD
        conexion = Conexion.get_conexion()
        # Verificamos que no haya una conexion en curso
        if not conexion.in_transaction:
            conexion.start_transaction()
        else:
            # Si ya hay una hacemos rollback para limpiar
            conexion.rollback()
            conexion.start_transaction()
        # iniciamos el cursor
        cursor = conexion.cursor()
        try:
            resultado_reparacion = self.reparacion.obtener_reparacion_por_id(id_rep, cursor)
            if not resultado_reparacion:
                messagebox.showinfo("No encontrado", f"La reparación con ID {id_rep} no se encuentra en la base de datos.")
                return

            # HABILITAR TEMPORALMENTE todos los campos para poder insertar
            self.habilitar_temporalmente()

            # Insertar datos de la reparación
            self.insertar_valor_seguro(self.entrada_ingreso, resultado_reparacion.fecha_ingreso)
            self.insertar_valor_seguro(self.entrada_estado, resultado_reparacion.estado)
            self.insertar_valor_seguro(self.entrada_precio, resultado_reparacion.precio_reparacion)
            
            id_disp = resultado_reparacion.id_dispositivo
            
            resultado_dispositivo = self.dispositivo.obtener_dispositivo_por_id(id_disp, cursor)
            if resultado_dispositivo:
                               
                # Insertar datos del dispositivo
                self.insertar_valor_seguro(self.entrada_marca, resultado_dispositivo.marca)
                self.insertar_valor_seguro(self.entrada_modelo, resultado_dispositivo.version)
                self.insertar_valor_seguro(self.entrada_tipo_rep, resultado_dispositivo.tipo_reparacion)
                self.insertar_valor_seguro(self.entrada_tipo_password, resultado_dispositivo.tipo_password)
                self.insertar_valor_seguro(self.entrada_password, resultado_dispositivo.password)
                
                # Para el campo Text (comentarios)
                self.insertar_texto_seguro(self.entrada_comentarios, resultado_dispositivo.comentarios)

                id_cliente = resultado_dispositivo.id_cliente
                resultado_cliente = self.cliente.obtener_cliente_por_cedula(id_cliente, cursor)

                if resultado_cliente:
                    # aceptamos la transaccion
                    conexion.commit()                 
                    # Insertar datos del cliente
                    self.insertar_valor_seguro(self.entrada_cedula, resultado_cliente.cedula)
                    self.insertar_valor_seguro(self.entrada_nombre, resultado_cliente.nombre)
                    self.insertar_valor_seguro(self.entrada_celular, resultado_cliente.celular)
                    self.insertar_valor_seguro(self.entrada_email, resultado_cliente.email)
                else:
                    messagebox.showwarning("Cliente no encontrado", f"No se encontró el cliente con cédula {id_cliente}.")
            else:
                messagebox.showwarning("Dispositivo no encontrado", f"No se encontró el dispositivo con ID {id_disp}.")
            
            # Restaurar el estado original de los campos (deshabilitar los que correspondan)
            self.habilitar_entrada()

        except Exception as e:
            conexion.rollback()
            messagebox.showerror("ERROR", f"Error al cargar los datos: {e}")
        finally:
            if cursor:
                cursor.close()

    def habilitar_temporalmente(self):
        """Habilita temporalmente todos los campos para poder insertar valores"""
        campos = [self.entrada_cedula,
            self.entrada_ingreso,
            self.entrada_marca,
            self.entrada_modelo,
            self.entrada_tipo_rep,
            self.entrada_tipo_password,
            self.entrada_password,
            self.entrada_nombre,
            self.entrada_celular,
            self.entrada_precio,
            self.entrada_email,
            self.entrada_estado,
            self.entrada_refaccion,
            self.entrada_comentarios,
            self.entrada_comentarios_tec
        ]
    
        for campo in campos:
            try:
                campo.config(state="normal")
            except:
                pass

    def insertar_valor_seguro(self, campo, valor):
        """Inserta valores de forma segura en campos Entry"""
        try:
            if valor is None:
                valor = ""
            campo.delete(0, tk.END)
            campo.insert(0, str(valor))
        except Exception as e:
            print(f"ERROR insertando en {campo}: {e}")

    def insertar_texto_seguro(self, campo_text, valor):
        """Inserta valores de forma segura en campos Text"""
        try:
            if valor is None:
                valor = ""
            campo_text.delete("1.0", tk.END)
            campo_text.insert("1.0", str(valor))
        except Exception as e:
            print(f"ERROR insertando texto: {e}")
    def btn_limpiar(self):
        self.entrada_id_reparacion.delete(0, tk.END)
        self.limpiar_campos()
    def limpiar_campos(self):
        """Limpia todos los campos de forma segura"""
        # Primero habilitar temporalmente
        self.habilitar_temporalmente()
    
        # Limpiar Entry widgets
        entries = [
            self.entrada_ingreso,
            self.entrada_marca,
            self.entrada_modelo,
            self.entrada_tipo_rep,
            self.entrada_tipo_password,
            self.entrada_password,
            self.entrada_nombre,
            self.entrada_celular,
            self.entrada_estado,
            self.entrada_precio,
            self.entrada_cedula,
            self.entrada_email,
            self.entrada_refaccion,
            self.entrada_ingreso
        ]
        
        for entry in entries:
            try:
                entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("ERROR", f"Error al limpiar los campos: {e}")
        
        # Limpiar Text widgets
        try:
            self.entrada_comentarios.delete("1.0", tk.END)
            self.entrada_comentarios_tec.delete("1.0", tk.END)
            self.deshabilitar_entradas()
            
        except Exception as e:
            messagebox.showerror("ERROR", f"Error al limpiar los campos: {e}")
        
        # Resetear Combobox
        try:
            self.entrada_tipo.set('SI')
        except:
            pass

    def habilitar_entrada(self):
        """Habilita los campos después de cargar los datos"""
        
        campos_habilitados = [
            self.entrada_refaccion,
            self.entrada_comentarios_tec,
            self.entrada_tipo
        ]
        
        for campo in campos_habilitados:
            try:
                campo.config(state="normal")
            except:
                pass
        
        # Deshabilitar los que no deben editarse
        campos_deshabilitados = [
            self.entrada_cedula,
            self.entrada_nombre,
            self.entrada_email,
            self.entrada_celular,
            self.entrada_marca,
            self.entrada_modelo,
            self.entrada_tipo_rep,
            self.entrada_tipo_password,
            self.entrada_password,
            self.entrada_precio,
            self.entrada_ingreso,
            self.entrada_comentarios,
            self.entrada_estado
        ]
        
        for campo in campos_deshabilitados:
            try:
                campo.config(state="disabled")
            except:
                pass
        
        self.Btn_guardar.config(state="normal")

    def cancelar_accion(self):
        self.limpiar_campos()
        self.entrada_id_reparacion.delete(0, tk.END)  # Limpiar ID aquí
        messagebox.showinfo("Cancelado", "Todos los campos han sido limpiados")

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