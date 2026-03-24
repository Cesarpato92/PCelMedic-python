import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

from Logica.LogicaCliente import LogicaCliente
from Logica.LogicaDispositivo import LogicaDispositivo
from Logica.LogicaReparacion import LogicaReparacion
from Logica.LogicaGarantia import LogicaGarantia
from Logica.GeneradorPDF import GeneradorPDF
from Utilidades.TransaccionConexion import TransaccionConexion
import os


class VentanaSalidaGarantia(tk.Frame):
    
    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = controller
        
        self.garantia = LogicaGarantia()
        self.reparacion = LogicaReparacion()
        self.dispositivo = LogicaDispositivo()
        self.cliente = LogicaCliente()
        self.GeneradorPDF = GeneradorPDF()
        
        # Objetos de modelo para el reporte
        self.cliente_model = None
        self.dispositivo_model = None
        self.reparacion_model = None
        self.garantia_actual = None
        
        # Configuración del grid principal
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        # Contenedor principal
        contenedor = ttk.Frame(self, padding="10")
        contenedor.grid(row=0, column=0, sticky="nsew")
        contenedor.columnconfigure(0, weight=1)
        contenedor.columnconfigure(1, weight=1)
        
        
        # Buscador
        frame_busqueda = ttk.Frame(contenedor)
        frame_busqueda.grid(row=1, column=0, columnspan=2, pady=10, sticky="w")
        
        ttk.Label(frame_busqueda, text="ID Garantía:").pack(side=tk.LEFT, padx=5)
        self.entrada_id_garantia = ttk.Entry(frame_busqueda, width=20)
        self.entrada_id_garantia.pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_busqueda, text="Buscar", command=self.buscar_garantia).pack(side=tk.LEFT, padx=5)
        
        # Información de la Garantía
        frame_info = ttk.LabelFrame(contenedor, text="Detalles de la Garantía", padding="10")
        frame_info.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=5)
        frame_info.columnconfigure(1, weight=1)
        
        # Campos de solo lectura
        ttk.Label(frame_info, text="Cliente:").grid(row=0, column=0, sticky="w", pady=2)
        self.lbl_cliente = ttk.Label(frame_info, text="---", font=("Helvetica", 10, "bold"))
        self.lbl_cliente.grid(row=0, column=1, sticky="w", pady=2)
        
        ttk.Label(frame_info, text="Dispositivo:").grid(row=1, column=0, sticky="w", pady=2)
        self.lbl_dispositivo = ttk.Label(frame_info, text="---")
        self.lbl_dispositivo.grid(row=1, column=1, sticky="w", pady=2)
        
        ttk.Label(frame_info, text="Fecha Inicio:").grid(row=2, column=0, sticky="w", pady=2)
        self.lbl_fecha_inicio = ttk.Label(frame_info, text="---")
        self.lbl_fecha_inicio.grid(row=2, column=1, sticky="w", pady=2)
        
        ttk.Label(frame_info, text="Estado Actual:").grid(row=3, column=0, sticky="w", pady=2)
        self.lbl_estado = ttk.Label(frame_info, text="---", font=("Helvetica", 12, "bold"), foreground="blue")
        self.lbl_estado.grid(row=3, column=1, sticky="w", pady=2)
        
        ttk.Label(frame_info, text="Observaciones Entrada:").grid(row=4, column=0, sticky="nw", pady=2)
        self.txt_observaciones_entrada = tk.Text(frame_info, height=4, width=50, state="disabled")
        self.txt_observaciones_entrada.grid(row=4, column=1, sticky="w", pady=2)
        
        # Campos editables para la salida
        frame_salida = ttk.LabelFrame(contenedor, text="Finalización de Garantía", padding="10")
        frame_salida.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=5)
        frame_salida.columnconfigure(1, weight=1)
        
        ttk.Label(frame_salida, text="Estado Final:").grid(row=0, column=0, sticky="w", pady=5)
        self.combo_estado_final = ttk.Combobox(frame_salida, values=["Completada", "Rechazada"], state="readonly")
        self.combo_estado_final.grid(row=0, column=1, sticky="w", pady=5)
        self.combo_estado_final.set("Completada")
        
        ttk.Label(frame_salida, text="Precio Insumos ($):").grid(row=1, column=0, sticky="w", pady=5)
        self.entrada_precio_insumos = ttk.Entry(frame_salida)
        self.entrada_precio_insumos.grid(row=1, column=1, sticky="w", pady=5)
        self.entrada_precio_insumos.insert(0, "0")
        
        ttk.Label(frame_salida, text="Observaciones Finales:").grid(row=2, column=0, sticky="nw", pady=5)
        self.txt_observaciones_finales = tk.Text(frame_salida, height=4, width=50)
        self.txt_observaciones_finales.grid(row=2, column=1, sticky="w", pady=5)
        
        # Botones
        frame_botones = ttk.Frame(contenedor, padding="10")
        frame_botones.grid(row=4, column=0, columnspan=2, sticky="ew")
        
        
        self.btn_entregar = ttk.Button(frame_botones, text="Confirmar Entrega", command=self.entregar_garantia, state="disabled")
        self.btn_entregar.grid(row=0, column=0, padx=5)
        ttk.Button(frame_botones, text="Limpiar", command=self.limpiar_campos).grid(row=0, column=1, padx=5)
       
        
        

    def buscar_garantia(self):
        id_garantia = self.entrada_id_garantia.get().strip()
        if not id_garantia:
            messagebox.showwarning("Atención", "Ingrese un ID de garantía")
            return
        
        try:
            with TransaccionConexion() as (cursor, conexion):
                garantia = self.garantia.obtener_garantia_por_id(id_garantia, cursor)
                if not garantia:
                    messagebox.showinfo("No encontrado", "No se encontró la garantía")
                    self.limpiar_campos()
                    return
                   
                self.garantia_actual = garantia
                
                # Obtener datos relacionados
                reparacion = self.reparacion.obtener_reparacion_por_id(garantia.id_reparacion, cursor)
                dispositivo = self.dispositivo.obtener_dispositivo_por_id(reparacion.id_dispositivo, cursor)
                cliente = self.cliente.obtener_cliente_por_cedula(dispositivo.id_cliente, cursor)
                
                # Guardar modelos para el reporte
                self.reparacion_model = reparacion
                self.dispositivo_model = dispositivo
                self.cliente_model = cliente
                
                # Mostrar datos
                self.lbl_cliente.config(text=f"{cliente.nombre} ({cliente.cedula})")
                self.lbl_dispositivo.config(text=f"{dispositivo.marca} {dispositivo.version}")
                self.lbl_fecha_inicio.config(text=garantia.fecha_inicio)
                self.lbl_estado.config(text=garantia.estado)
                
                self.txt_observaciones_entrada.config(state="normal")
                self.txt_observaciones_entrada.delete("1.0", tk.END)
                self.txt_observaciones_entrada.insert("1.0", garantia.observaciones)
                self.txt_observaciones_entrada.config(state="disabled")
                
                self.btn_entregar.config(state="normal")
                
                conexion.commit()
                
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar la garantía: {e}")


    def entregar_garantia(self):
        if not self.garantia_actual:
            return
            
        try:
            estado_final = self.combo_estado_final.get()
            precio_insumos = self.entrada_precio_insumos.get().strip()
            observaciones_finales = self.txt_observaciones_finales.get("1.0", "end-1c").strip()
            
            # Validar precio
            try:
                precio_float = float(precio_insumos)
            except ValueError:
                messagebox.showwarning("Atención", "El precio de insumos debe ser un número válido")
                return
            
            
            estado_antiguo = self.garantia_actual.estado
            # Actualizar objeto
            self.garantia_actual.estado = estado_final
            self.garantia_actual.fecha_fin = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.garantia_actual.precio_insumos = precio_float
            self.garantia_actual.comentarios_finales = observaciones_finales

            try:
                with TransaccionConexion() as (cursor, conexion):
                    # actualizar_garantia ahora puede lanzar ValueError
                    self.garantia.actualizar_garantia(self.garantia_actual,estado_antiguo, cursor)
                    
                    # Si no lanzó excepción, aceptamos la transaccion
                    conexion.commit()
                    messagebox.showinfo("Exito", "Garantía entregada exitosamente")
                    self.generar_pdf_salida()
                    self.limpiar_campos()
            except ValueError as ve:
                messagebox.showwarning("Aviso", f"Error de validación: {ve}")
            except Exception as e:
                messagebox.showerror("Error", f"Error al actualizar garantía: {e}")
               
        except ValueError as ve:
            messagebox.showwarning("Aviso", f"Error de validación: {ve}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar garantía: {e}")


    def generar_pdf_salida(self):
        if self.cliente_model and self.dispositivo_model and self.reparacion_model:
            try:
                ruta = self.GeneradorPDF.generar_reporte_garantia(
                    self.cliente_model,
                    self.dispositivo_model, 
                    self.reparacion_model, 
                    self.garantia_actual
                )
                os.startfile(ruta)
            except Exception as e:
                messagebox.showerror("Error", f"Error al generar PDF: {e}")
        else:
            messagebox.showwarning("Advertencia", "No se pudo generar el PDF: datos faltantes")

    def limpiar_campos(self):
        self.entrada_id_garantia.delete(0, tk.END)
        self.lbl_cliente.config(text="---")
        self.lbl_dispositivo.config(text="---")
        self.lbl_fecha_inicio.config(text="---")
        self.lbl_estado.config(text="---")
        
        self.txt_observaciones_entrada.config(state="normal")
        self.txt_observaciones_entrada.delete("1.0", tk.END)
        self.txt_observaciones_entrada.config(state="disabled")
        
        self.combo_estado_final.set("Completada")
        self.entrada_precio_insumos.delete(0, tk.END)
        self.entrada_precio_insumos.insert(0, "0")
        self.txt_observaciones_finales.delete("1.0", tk.END)
        
        self.btn_entregar.config(state="disabled")
        self.garantia_actual = None
        self.cliente_model = None
        self.dispositivo_model = None
        self.reparacion_model = None