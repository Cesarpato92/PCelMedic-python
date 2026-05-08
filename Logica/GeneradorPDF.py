from fpdf import FPDF
import os
from datetime import datetime

class GeneradorPDF:
    def __init__(self):
        self.ruta_reportes = "Reportes"
        if not os.path.exists(self.ruta_reportes):
            os.makedirs(self.ruta_reportes)


    def generar_reporte_reparacion(self, cliente, dispositivo, reparacion):
        fecha = datetime.now().strftime("%Y-%m-%d")
        nombre_archivo = f"Orden_{reparacion.id_reparacion}-{cliente.cedula}-{fecha}.pdf"
        ruta_archivo = os.path.join(self.ruta_reportes, nombre_archivo)
        
        pdf = FPDF()
        pdf.add_page()
        
        # Título principal
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "PCelMedic", ln=True, align='C')
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, f"Orden de Reparación #{reparacion.id_reparacion}", ln=True, align='C')
        pdf.ln(10)
        
        # Función auxiliar para crear tablas (CONVERSIÓN A STRING)
        def agregar_seccion(titulo, datos):
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, titulo, ln=True, align='L')
            pdf.set_font("Arial", size=10)
            
            for clave, valor in datos:
                pdf.set_font("Arial", 'B', 11)
                pdf.cell(45, 8, str(clave), border=1)      # ← Convertir a string
                pdf.set_font("Arial", size=11)
                pdf.cell(0, 8, str(valor), border=1, ln=True)  # ← Convertir a string
            pdf.ln(5)
        
        # Datos del Cliente (convertir cédula a string)
        agregar_seccion("Datos del Cliente", [
            ("Cédula", str(cliente.cedula)),
            ("Nombre", cliente.nombre),
            ("Email", cliente.email),
            ("Celular", cliente.celular)
        ])
        
        # Datos del Dispositivo (convertir ID a string)
        agregar_seccion("Datos del Dispositivo", [
            ("ID Dispositivo", str(dispositivo.id_dispositivo)),
            ("Marca", dispositivo.marca),
            ("Modelo", dispositivo.version),
            ("Tipo Reparación", dispositivo.tipo_reparacion),
            ("Tipo Seguridad", dispositivo.tipo_password),
            ("Contraseña", dispositivo.password or "N/A"),
            ("Comentarios", dispositivo.comentarios or "Ninguno")
        ])
        
        # Detalles de la Reparación
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Detalles de la Reparación", ln=True, align='L')
        
        # Fecha y estado 
        pdf.set_font("Arial", 'B', 11)
        pdf.cell(45, 8, "Fecha Ingreso", border=1)
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, str(reparacion.fecha_ingreso), border=1, ln=True)

        pdf.set_font("Arial", 'B', 11)
        pdf.cell(45, 8, "Estado", border=1)
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, reparacion.estado, border=1, ln=True)
        
        # Comentarios
        pdf.set_font("Arial", 'B', 11)
        pdf.cell(45, 8, "Comentarios", border=1)
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 8, reparacion.comentarios or "Ninguno", border=1, ln=True)

        # Precio (resaltado)
        pdf.set_font("Arial", 'B', 11)
        pdf.set_fill_color(255, 255, 0)
        pdf.cell(45, 8, "Precio Reparación", border=1, fill=True)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 8, f"${reparacion.precio_reparacion:,.2f}", border=1, ln=True, fill=True)
        
        pdf.set_font("Arial", 'B', 8)
        pdf.cell(0, 10, "Este documento es un comprobante de recepción. No válido como factura legal.", ln=True, align='L')
        # Guardar
        pdf.output(ruta_archivo)
        return ruta_archivo

    def generar_reporte_garantia(self, cliente, dispositivo, reparacion, garantia):

        fecha = datetime.now().strftime("%Y-%m-%d")
        nombre_archivo = f"Garantia_{garantia.id_garantia}-{cliente.cedula}-{fecha}.pdf"
        ruta_archivo = os.path.join(self.ruta_reportes, nombre_archivo)
        
        pdf = FPDF()
        pdf.add_page()
        
        # Título
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "PCelMedic", ln=True, align='C')
        pdf.ln(2)

        # Subtitulo
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, f"Garantía #{garantia.id_garantia}", ln=True, align='C')
        pdf.ln(5)
        
        # Datos del Cliente
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Datos del Cliente", ln=True, align='L')
        
        datos_cliente = [
            ("Cédula", str(cliente.cedula)),
            ("Nombre", cliente.nombre),
            ("Email", cliente.email),
            ("Celular", cliente.celular)
        ]
        
        for key, value in datos_cliente:
            pdf.set_font("Arial", 'B', 10)
            pdf.cell(40, 7, key, border=1)
            pdf.set_font("Arial", size=10)
            pdf.cell(0, 7, value, border=1, ln=True)
            
        pdf.ln(5)

        # Datos del Dispositivo 
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Datos del Dispositivo", ln=True, align='L')
        
        datos_dispositivo = [
            ("ID Dispositivo", str(dispositivo.id_dispositivo)),
            ("Marca", dispositivo.marca),
            ("Modelo", dispositivo.version),
            ("Tipo Reparación", dispositivo.tipo_reparacion),
            ("Comentarios", dispositivo.comentarios or "Ninguno")
        ]
        
        for key, value in datos_dispositivo:
            pdf.set_font("Arial", 'B', 10)
            pdf.cell(40, 7, key, border=1)
            pdf.set_font("Arial", size=10)
            # Para comentarios largos, usar multi_cell pero ajustando posición
            if key == "Comentarios" and len(value) > 50:
                # Guardar posición X actual
                x = pdf.get_x()
                y = pdf.get_y()
                pdf.multi_cell(0, 7, value, border=1)
                pdf.set_y(y + 7)  # Ajustar posición Y
            else:
                pdf.cell(0, 7, value, border=1, ln=True)
        
        pdf.ln(5)

        # Detalles de la Reparación
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Detalles de la Reparación", ln=True, align='L')
        
        datos_reparacion = [
            ("ID Reparación", str(reparacion.id_reparacion)),
            ("Fecha Ingreso", str(reparacion.fecha_ingreso)),
            ("Estado", reparacion.estado),
            ("Comentarios", reparacion.comentarios or "Ninguno"),
            ("Precio Reparación", f"${reparacion.precio_reparacion:,.2f}")
        ]
        
        for key, value in datos_reparacion:
            pdf.set_font("Arial", 'B', 10)
            # Resaltar precio
            if key == "Precio Reparación":
                pdf.set_fill_color(255, 255, 0)
                pdf.cell(40, 7, key, border=1, fill=True)
                pdf.set_font("Arial", 'B', 10)
                pdf.cell(0, 7, value, border=1, ln=True, fill=True)
                pdf.set_fill_color(255, 255, 255)
            else:
                pdf.cell(40, 7, key, border=1)
                pdf.set_font("Arial", size=10)
                pdf.cell(0, 7, value, border=1, ln=True)
        
        pdf.ln(5)
        
        # Detalles de la Garantía
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Detalles de la Garantía", ln=True, align='L')
        
        datos_garantia = [
            ("Fecha Inicio", str(garantia.fecha_inicio)),
            ("Fecha Fin", str(garantia.fecha_fin) if garantia.fecha_fin else "N/A"),
            ("Estado", garantia.estado),
            ("Observaciones Entrada", garantia.observaciones or "Ninguna"),
            ("Observaciones Finales", garantia.comentarios_finales or "N/A"),
        ]
        
        for key, value in datos_garantia:
            pdf.set_font("Arial", 'B', 10)
            pdf.cell(40, 7, key, border=1)
            pdf.set_font("Arial", size=10)
            pdf.cell(0, 7, value, border=1, ln=True)

        pdf.set_font("Arial", 'B', 8)
        pdf.cell(0, 10, "Este documento es un comprobante de recepción. No válido como factura legal.", ln=True, align='L')
        
        pdf.output(ruta_archivo)
        return ruta_archivo
    
    def generar_factura(self, cliente, dispositivo, reparacion, id_factura):
        
        fecha = datetime.now().strftime("%Y-%m-%d")
        nombre_archivo = f"Factura_{id_factura}-{cliente.cedula}-{fecha}.pdf"
        ruta_archivo = os.path.join(self.ruta_reportes, nombre_archivo)
        
        pdf = FPDF()
        pdf.add_page()
        
        # Título
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, f"PCelMedic - Recibo de pago # {id_factura}", ln=True, align='C')
        pdf.ln(10)
        
        # Datos del Cliente 
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Cliente", ln=True, align='L')
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 6, f"Nombre: {cliente.nombre}", ln=True)
        pdf.cell(0, 6, f"Cédula: {cliente.cedula}", ln=True)
        pdf.cell(0, 6, f"Email: {cliente.email}", ln=True)
        pdf.cell(0, 6, f"Teléfono: {cliente.celular}", ln=True)
        pdf.ln(10)

        # Datos del Dispositivo
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Dispositivo", ln=True, align='L')
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 6, f"Equipo: {dispositivo.marca} {dispositivo.version}", ln=True)
        pdf.cell(0, 6, f"ID Dispositivo: {dispositivo.id_dispositivo}", ln=True)
        pdf.ln(10)

        # Detalles del Servicio
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Detalles del Servicio", ln=True, align='L')
        
        # Tabla simple
        pdf.set_font("Arial", 'B', 10)
        pdf.cell(140, 8, "Descripción", 1)
        pdf.cell(40, 8, "Valor", 1, ln=True)
        
        pdf.set_font("Arial", size=10)
        descripcion = f"Reparación de {dispositivo.marca} {dispositivo.version} - {dispositivo.tipo_reparacion}"
        pdf.cell(140, 8, descripcion, 1)
        pdf.cell(40, 8, f"${reparacion.precio_reparacion:,.2f}", 1, ln=True)

        if reparacion.comentarios:
            pdf.set_font("Arial", size=10)
            pdf.multi_cell(0, 6, f"Comentarios: {reparacion.comentarios}", border=0, align='L')
        
        # Total
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(140, 10, "Total a Pagar", 1)
        pdf.cell(40, 10, f"${reparacion.precio_reparacion:,.2f}", 1, ln=True, align='R')
        
        pdf.ln(20)
        pdf.set_font("Arial", size=6)
        pdf.cell(0, 5, "Gracias por confiar en PCelMedic.", ln=True, align='C')
        pdf.cell(0, 5, "Pertenezco al regimen de No Responsables de IVA (Art. 437 del Estatuto Tributario).", ln=True, align='C')

        pdf.set_font("Arial", 'B', 8)
        pdf.cell(0, 10, "Este documento es un comprobante de recepción. No válido como factura legal.", ln=True, align='L')
        pdf.output(ruta_archivo)
        return ruta_archivo