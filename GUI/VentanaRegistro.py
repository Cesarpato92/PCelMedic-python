import tkinter as tk
from tkinter import messagebox
from Modelo.ModeloCliente import ModeloCliente
from Modelo.ModeloDispositivo import ModeloDispositivo
from Modelo.ModeloReparacion import ModeloReparacion
from Logica.LogicaCliente import LogicaCliente
from Logica.LogicaDispositivo import LogicaDispositivo
from Logica.LogicaReparacion import LogicaReparacion
from datetime import datetime


class VentanaRegistro(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller
        self.cliente = LogicaCliente()
        
        label = tk.Label(self, text="Registro de Clientes y Dispositivos", font=("Helvetica", 16))
        label.pack(pady=10, padx=10)

        # Configuración para que el frame se expanda dentro de su padre
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1) 
        
        # Contenedor primcipal
        contenedor = tk.Frame(self, bg="white")
        contenedor.pack(fill="both", expand=True, padx=20, pady=20)

        # Columna izquierda - Datos del cliente

        contenido_izquierda = tk.Frame(contenedor, bg="white")
        contenido_izquierda.pack(side="left", fill="both", expand=True, padx=(0, 10))

        tk.Label(contenido_izquierda, text="Datos del Cliente", font=("Helvetica", 14)).pack(pady=(0, 5), anchor="w")
        tk.Label(contenido_izquierda, text="Cedula:").pack(anchor="w")
        cedula_frame = tk.Frame(contenido_izquierda, bg="white")
        cedula_frame.pack(pady=5, anchor="w")
        self.entrada_cedula = tk.Entry(cedula_frame, width=20)
        self.entrada_cedula.pack(side="left")
        btn_buscar = tk.Button(cedula_frame, text="Buscar", command=self.buscar_cliente)
        btn_buscar.pack(side="left", padx=5)

        tk.Label(contenido_izquierda, text="Nombre", bg="white").pack(pady=(8, 0), anchor="w")
        self.entrada_nombre = tk.Entry(contenido_izquierda, width=30)
        self.entrada_nombre.pack(pady=3, anchor="w")

        tk.Label(contenido_izquierda, text="Email", bg="white").pack(pady=(8, 0), anchor="w")
        self.entrada_email = tk.Entry(contenido_izquierda, width=30)
        self.entrada_email.pack(pady=3, anchor="w")

        tk.Label(contenido_izquierda, text="Celular", bg="white").pack(pady=(8, 0), anchor="w")
        self.entrada_celular = tk.Entry(contenido_izquierda, width=30)
        self.entrada_celular.pack(pady=3, anchor="w")

        # Columna derecha: datos del equipo
        contenido_derecha = tk.Frame(contenedor, bg="white")
        contenido_derecha.pack(side="right", fill="both", expand=True, padx=(8, 0))

        tk.Label(contenido_derecha, text="Datos del equipo", font=("Helvetica", 14, "bold"), bg="#f0f0f0").pack(pady=(0, 5), anchor="w")
        tk.Label(contenido_derecha, text="Marca", bg="white").pack(pady=(5, 0), anchor="w")
        self.entrada_marca = tk.Entry(contenido_derecha, width=30)
        self.entrada_marca.pack(pady=3, anchor="w")

        tk.Label(contenido_derecha, text="Modelo", bg="white").pack(pady=(5, 0), anchor="w")
        self.entrada_modelo = tk.Entry(contenido_derecha, width=30)
        self.entrada_modelo.pack(pady=3, anchor="w")

        tk.Label(contenido_derecha, text="Tipo de reparación", bg="white").pack(pady=(5, 0), anchor="w")
        opciones_rep = ["Display", "Puerto de carga", "Corto", "Sonido", "Cuenta", "Bloqueo", "Otro"]
        self.var_tipo_rep = tk.StringVar(self)
        self.var_tipo_rep.set(opciones_rep[0]) # Opción por defecto
        self.entrada_tipo = tk.OptionMenu(contenido_derecha, self.var_tipo_rep, *opciones_rep)
        self.entrada_tipo.config(width=25) # Ajustar ancho del widget OptionMenu
        self.entrada_tipo.pack(pady=3, anchor="w")

        tk.Label(contenido_derecha, text="Tipo de contraseña", bg="#f0f0f0").pack(pady=(5, 0), anchor="w")
        opciones_contra = ["Sin contraseña", "Patrón", "Texto/Números"]
        self.var_tipo_contrasena = tk.StringVar(self)
        self.var_tipo_contrasena.set(opciones_contra[0]) # Opción por defecto

        
        # Asignamos la función de callback (on_tipo_contrasena_change) al evento 'write'
        self.var_tipo_contrasena.trace_add("write", self.on_tipo_contrasena_change)
        
        tk.Label(contenido_derecha, text="Contraseña del equipo", bg="white").pack(pady=(5, 0), anchor="w")
        self.entrada_contrasena = tk.Entry(contenido_derecha, width=30, show='*')
        self.entrada_contrasena.pack(pady=3, anchor="w")

        tk.Label(contenido_derecha, text="Precio de reparación", bg="white").pack(pady=(5, 0), anchor="w")
        self.entrada_precio = tk.Entry(contenido_derecha, width=30)
        self.entrada_precio.pack(pady=3, anchor="w")

       
        tk.Label(contenido_derecha, text="Comentarios", bg="white").pack(pady=(5, 0), anchor="w")
        self.entrada_comentarios = tk.Text(contenido_derecha, width=40, height=6)
        self.entrada_comentarios.pack(pady=3, anchor="w")

        # Botón de guardar centrado debajo de content_frame
        btn_frame = tk.Frame(self, bg="white")
        btn_frame.pack(fill="x", pady=10)
        Btn_guardar = tk.Button(btn_frame, text="Guardar", command=self.guardar)
        Btn_guardar.pack()

        self.on_tipo_contrasena_change()
    
    def guardar(self):
        """Guarda cliente, dispositivo y reparación en una transacción integrada.
        
        Flujo:
            1. Extrae datos de cliente del formulario
            2. Valida que todos los campos requeridos estén presentes
            3. Verifica si cliente existe (buscar) o crea uno nuevo (insertar)
            4. Extrae datos de dispositivo y construye objeto Dispositivo
            5. Guarda dispositivo y obtiene id_dispositivo
            6. Guarda reparación asociada con id_dispositivo
            7. Limpia todos los campos
            8. Proporciona retroalimentación mediante messagebox
        
        Validaciones:
            - Todos los campos del cliente son obligatorios
            - Cedula debe ser convertible a int
            - Tipo de reparación es requerido
        
        Propósito:
            - Crear un registro integrado de nuevo cliente + equipo + reparación
            - O actualizar cliente existente + crear nuevo equipo + reparación
        """
        # Extrae datos de cliente
        cedula = self.entrada_cedula.get().strip()
        nombre = self.entrada_nombre.get().strip()
        email = self.entrada_email.get().strip()
        celular = self.entrada_celular.get().strip()

        # Datos del dispositivo (leer antes de limpiar los widgets)
        marca = self.entrada_marca.get().strip()
        modelo = self.entrada_modelo.get().strip()
        tipo_rep = self.var_tipo_rep.get().strip() 
        tipo_contra = self.var_tipo_contrasena.get().strip()
        contra = self.entrada_contrasena.get().strip()  # Contraseña real del equipo
        comentarios_disp = (self.entrada_comentarios.get('1.0', tk.END) or "").strip()

        #Datos de la reparacion
        estado = "Pendiente"
        fecha_ingreso = datetime.now().date()
        costo_repuesto = 0
        precio_rep = self.entrada_precio.get().strip()
        comentarios_rep = ""

        # Validación básica
        if not (cedula and nombre and email and celular):
            messagebox.showwarning("Atención", "Rellene todos los datos del cliente")
            return

        # Decidir insertar o actualizar según exista el cliente
        try:
            existente = self.cliente.obtener_cliente_por_cedula(cedula)
            cliente_obt = ModeloCliente(
                _cedula = cedula,
                _nombre = nombre,
                _email = email,
                _celular = celular
            )

            if existente:
                # Actualizar cliente existente
                messagebox.showinfo("CLIENTE REGISTRADO EN LA BASE DE DATOS", f"Se actualizarán los datos del cliente {nombre}")
                actualizado = self.cliente.actualizar_cliente(cliente_obt)
                if actualizado:
                    messagebox.showinfo("Actualizado", f"Cliente {nombre} actualizado correctamente")
                else:
                    messagebox.showwarning("Aviso", "No se realizaron cambios al cliente")
            else:
                # Insertar nuevo cliente
                insertado = self.cliente.insertar(cliente_obt)
                if insertado:
                    messagebox.showinfo("Guardado", f"Usuario {nombre} guardado correctamente")
                else:
                    messagebox.showerror("Error", "Error al guardar el usuario")
                    return
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar cliente: {e}")
            return

        # Preparar comentarios del dispositivo: incluir modelo y precio si hay
        extra = []
        if modelo:
            extra.append(f"Modelo: {modelo}")
        if precio_rep:
            extra.append(f"Precio: {precio_rep}")
        if extra:
            comentarios_disp = (comentarios_disp + "\n" + " | ".join(extra)).strip()

        # Guardar dispositivo (usar la lógica de negocio)
        try:
            # Convertir cedula a int si es posible
           
            dispositivo_obj = ModeloDispositivo(
                _marca=marca or '',
                _tipo_reparacion=tipo_rep or '',
                _tipo_contraseña=tipo_contra or None,
                _contraseña=contra or None,
                _comentarios=comentarios_disp or None,
                _id_cliente=cedula
            )

            # id_disp = self.controller.Logica.Logica.agregar_dispositivo(dispositivo=dispositivo_obj)
            id_disp = LogicaDispositivo.agregar_dispositivo(dispositivo_obj)
            if id_disp:
                messagebox.showinfo("Dispositivo", f"Dispositivo guardado con id {id_disp}")

                # Guardar la reparación asociada al dispositivo
                try:
                    
                    reparacion_obj = ModeloReparacion(
                        _fecha_ingreso = fecha_ingreso,
                        _estado = estado,
                        _costo_repuesto = costo_repuesto,
                        _precio_reparacion = precio_rep,
                        _comentarios = comentarios_rep,
                        _id_dispositivo = id_disp
                    )
                    id_rep = LogicaReparacion.agregar_reparacion(reparacion_obj)
                    
                    if id_rep:
                        messagebox.showinfo("Reparación", f"Reparación registrada con id {id_rep}")
                        
                except Exception as e:
                    messagebox.showwarning("Aviso", f"Dispositivo guardado, pero no se pudo registrar la reparación: {e}")
        except Exception as e:
            messagebox.showwarning("Aviso", f"Cliente guardado, pero no se pudo guardar el dispositivo: {e}")

        # Limpiar todos los campos
        try:
            self.entrada_cedula.delete(0, tk.END)
            self.entrada_nombre.delete(0, tk.END)
            self.entrada_email.delete(0, tk.END)
            self.entrada_celular.delete(0, tk.END)

            self.entrada_marca.delete(0, tk.END)
            self.entrada_modelo.delete(0, tk.END)
            # self.entrada_tipo.set('')  # Combobox: usar set() en lugar de delete()
            # self.var_tipo_contrasena.set('')  # Limpiar tipo de contraseña
            self.entrada_contrasena.delete(0, tk.END)  # Limpiar contraseña real
            self.entrada_precio.delete(0, tk.END)
            self.entrada_comentarios.delete('1.0', tk.END)
        except Exception:
            pass

    # Habilitar o deshabilitar casilla de contraseña
    def on_tipo_contrasena_change(self, *args):
        """
        Deshabilita o habilita la casilla de contraseña según la opción seleccionada.
        """
        if self.var_tipo_contrasena.get() == "Sin contraseña":
            self.entrada_contrasena.config(state=tk.DISABLED)
            self.entrada_contrasena.delete(0, tk.END) # Limpia el campo
        else:
            self.entrada_contrasena.config(state=tk.NORMAL)

    def on_cedula(self):
        estado = self.entrada_cedula.cget("state")

        if estado == tk.NORMAL:
            self.entrada_cedula.config(state=tk.DISABLED)
        else: 
            self.entrada_cedula.config(state=tk.NORMAL)

    def buscar_cliente(self):
        cedula =self.entrada_cedula.get().strip()
        if not cedula:
            messagebox.showwarning("AVISO", "Ingrese una cedula para buscar")
            return
        
        resultado = None

        try: 
            resultado = self.cliente.obtener_cliente_por_cedula(cedula)
        except Exception as e:
            messagebox.showerror(f"ERROR", "Error al buscar cliente : {e}")
            return
        
        if not resultado:
            messagebox.showinfo("No encontrado", "El cliente no esta registrado en la base de datos")
            return
        #Rellenamos los campos del formulario
        try:
            ced = resultado.cedula
            nom = resultado.nombre
            email = resultado.email
            celular = resultado.celular

            self.entrada_cedula.delete(0, tk.END)
            self.entrada_cedula.insert(0, ced)
            
            self.entrada_nombre.delete(0,tk.END)
            self.entrada_nombre.insert(0, nom)

            self.entrada_email.delete(0, tk.END)
            self.entrada_email.insert(0, email)

            self.entrada_celular.delete(0, tk.END)
            self.entrada_celular.insert(0, celular)

        except Exception as e:
            messagebox.showerror("ERROR", f"Error al rellenar los campos: {e}")
            return
        
