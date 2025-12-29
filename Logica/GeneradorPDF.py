from fpdf import FPDF
import os

class GeneradorPDF:
    def __init__(self):
        self.ruta_reportes = "Reportes"
        if not os.path.exists(self.ruta_reportes):
            os.makedirs(self.ruta_reportes)

    def generar_reporte_reparacion(self, cliente, dispositivo, reparacion):
        nombre_archivo = f"Orden_{reparacion.id_reparacion}-{cliente.cedula}.pdf"
        ruta_archivo = os.path.join(self.ruta_reportes, nombre_archivo)
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Título
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt=f"PCelMedic", ln=True, align='L')
        pdf.ln(10)

        #Subtitulo
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, txt=f"Orden de Reparación #{reparacion.id_reparacion}", ln=True, align='L')
        pdf.ln(10)
        
        # Datos del Cliente 
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, txt="Datos del Cliente", ln=True, align='L')
        pdf.set_font("Arial", size=10)
        
        # Tabla Cliente
        col_width = 70
        row_height = 10
        
        datos_cliente = [
            ("Cédula", str(cliente.cedula)),
            ("Nombre", str(cliente.nombre)),
            ("Email", str(cliente.email)),
            ("Celular", str(cliente.celular))
        ]
        
        for key, value in datos_cliente:
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(40, row_height, txt=key, border=1)
            pdf.set_font("Arial", size=12)
            pdf.cell(150, row_height, txt=value, border=1, ln=True)
            
        pdf.ln(10)

        # Datos del Dispositivo 
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, txt="Datos del Dispositivo", ln=True, align='L')
        pdf.set_font("Arial", size=10)
        
        datos_dispositivo = [
            ("ID Dispositivo", str(dispositivo.id_dispositivo)),
            ("Marca", str(dispositivo.marca)),
            ("Modelo", str(dispositivo.version)),
            ("Tipo Reparación", str(dispositivo.tipo_reparacion)),
            ("Tipo Seguridad", str(dispositivo.tipo_password)),
            ("Contraseña", str(dispositivo.password) if dispositivo.password else "N/A"),
            ("Comentarios", str(dispositivo.comentarios))
        ]
        
        for key, value in datos_dispositivo:
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(40, row_height, txt=key, border=1)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(150, row_height, txt=value, border=1)
            
        pdf.ln(10)
        
        # Detalles de la Reparación 
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, txt="Detalles de la Reparación", ln=True, align='L')
        pdf.set_font("Arial", size=10)
        
        datos_reparacion = [
            ("Fecha Ingreso", str(reparacion.fecha_ingreso)),
            ("Estado", str(reparacion.estado)),
            ("Precio Reparación", f"${reparacion.precio_reparacion:,.2f}")
        ]
        
        for i, (key, value) in enumerate(datos_reparacion):
            pdf.set_font("Arial", 'B', 12)
            # Resaltar precio
            if key == "Precio Reparación":
                pdf.set_fill_color(255, 255, 0) # Amarillo
                pdf.cell(40, row_height, txt=key, border=1, fill=True)
                pdf.set_font("Arial", 'B', 12)
                pdf.cell(150, row_height, txt=value, border=1, ln=True, fill=True)
            else:
                pdf.cell(40, row_height, txt=key, border=1)
                pdf.set_font("Arial", size=12)
                pdf.cell(150, row_height, txt=value, border=1, ln=True)
        
        pdf.output(ruta_archivo)
        return ruta_archivo

    def generar_reporte_garantia(self, cliente, dispositivo, reparacion, garantia):
        nombre_archivo = f"Garantia_{garantia.id_garantia}-{cliente.cedula}.pdf"
        ruta_archivo = os.path.join(self.ruta_reportes, nombre_archivo)
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Título
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt=f"PCelMedic", ln=True, align='L')
        pdf.ln(2)

        #Subtitulo
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, txt=f"Garantía #{garantia.id_garantia}", ln=True, align='L')
        pdf.ln(2)
        
        # Datos del Cliente 
        pdf.set_font("Arial", 'B', 10)
        pdf.cell(200, 10, txt="Datos del Cliente", ln=True, align='L')
        pdf.set_font("Arial", size=10)
        
        # Tabla Cliente
        col_width = 70
        row_height = 6
        
        datos_cliente = [
            ("Cédula", str(cliente.cedula)),
            ("Nombre", str(cliente.nombre)),
            ("Email", str(cliente.email)),
            ("Celular", str(cliente.celular))
        ]
        
        for key, value in datos_cliente:
            pdf.set_font("Arial", 'B', 10)
            pdf.cell(40, row_height, txt=key, border=1)
            pdf.set_font("Arial", size=10)
            pdf.cell(150, row_height, txt=value, border=1, ln=True)
            
        pdf.ln(2)

        # Datos del Dispositivo 
        pdf.set_font("Arial", 'B', 10)
        pdf.cell(200, 10, txt="Datos del Dispositivo", ln=True, align='L')
        pdf.set_font("Arial", size=10)
        
        datos_dispositivo = [
            ("Marca", str(dispositivo.marca)),
            ("Modelo", str(dispositivo.version)),
            ("Tipo Reparación", str(dispositivo.tipo_reparacion)),
            ("Comentarios", str(dispositivo.comentarios))
        ]
        
        for key, value in datos_dispositivo:
            pdf.set_font("Arial", 'B', 10)
            pdf.cell(40, row_height, txt=key, border=1)
            pdf.set_font("Arial", size=10)
            pdf.multi_cell(150, row_height, txt=value, border=1)
            
        pdf.ln(2)
        
        # Detalles de la Reparación 
        pdf.set_font("Arial", 'B', 10)
        pdf.cell(200, 10, txt="Detalles de la Reparación", ln=True, align='L')
        pdf.set_font("Arial", size=10)
        
        datos_reparacion = [
            ("Fecha Ingreso", str(reparacion.fecha_ingreso)),
            ("Estado", str(reparacion.estado)),
            ("Comentarios", str(reparacion.comentarios)),
            ("Precio Reparación", f"${reparacion.precio_reparacion:,.2f}")
        ]
        
        for i, (key, value) in enumerate(datos_reparacion):
            pdf.set_font("Arial", 'B', 10)
            # Resaltar precio
            if key == "Precio Reparación":
                pdf.set_fill_color(255, 255, 0) # Amarillo
                pdf.cell(40, row_height, txt=key, border=1, fill=True)
                pdf.set_font("Arial", 'B', 10)
                pdf.cell(150, row_height, txt=value, border=1, ln=True, fill=True)
            else:
                pdf.cell(40, row_height, txt=key, border=1)
                pdf.set_font("Arial", size=10)
                pdf.cell(150, row_height, txt=value, border=1, ln=True)
        
        pdf.ln(2)
        
        # Detalles de la Garantía 
        pdf.set_font("Arial", 'B', 10)
        pdf.cell(200, 10, txt="Detalles de la Garantía", ln=True, align='L')
        pdf.set_font("Arial", size=10)
        
        datos_garantia = [
            ("ID Garantía", str(garantia.id_garantia)),
            ("Fecha Inicio", str(garantia.fecha_inicio)),
            ("Fecha Fin", str(garantia.fecha_fin) if garantia.fecha_fin else "N/A"),
            ("Estado", str(garantia.estado)),
            ("Observaciones Entrada", str(garantia.observaciones)),
            ("Observaciones Finales", str(garantia.comentarios_finales) if garantia.comentarios_finales else "N/A"),
        ]
        
        for i, (key, value) in enumerate(datos_garantia):
            pdf.set_font("Arial", 'B', 10)
            pdf.cell(40, row_height, txt=key, border=1)
            pdf.set_font("Arial", size=10)
            pdf.cell(150, row_height, txt=value, border=1, ln=True)
        
        pdf.output(ruta_archivo)
        return ruta_archivo