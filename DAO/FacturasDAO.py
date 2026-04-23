from Modelo.ModeloFactura import ModeloFactura

class FacturasDAO:
    def __init__(self):
        pass

    def agregar_factura(self, modelo_factura, cursor):
        sql = "INSERT INTO factura (fecha, total, id_reparacion) VALUES (%s, %s, %s)"
        valores = (modelo_factura.fecha, modelo_factura.total, modelo_factura.id_reparacion)
        cursor.execute(sql, valores)
        
        if cursor.rowcount > 0:
            return cursor.lastrowid
        return None
    
    def obtener_factura_por_id(self, id_factura, cursor):
        factura_encontrada = None
        sql = "SELECT id_factura, fecha, total, id_reparacion FROM factura WHERE id_factura = %s"
        valores = (id_factura,)
        cursor.execute(sql, valores)
        resultado = cursor.fetchone()

        if resultado:
            factura_encontrada = ModeloFactura()
            factura_encontrada.id_factura = resultado[0]
            factura_encontrada.fecha = resultado[1]
            factura_encontrada.total = resultado[2]
            factura_encontrada.id_reparacion = resultado[3]
        
        return factura_encontrada

    def obtener_factura_por_id_reparacion(self, id_reparacion, cursor):
        factura_encontrada = None
        sql = "SELECT id_factura, fecha, total, id_reparacion FROM factura WHERE id_reparacion = %s"
        valores = (id_reparacion,)
        cursor.execute(sql, valores)
        resultado = cursor.fetchone()

        if resultado:
            factura_encontrada = ModeloFactura()
            factura_encontrada.id_factura = resultado[0]
            factura_encontrada.fecha = resultado[1]
            factura_encontrada.total = resultado[2]
            factura_encontrada.id_reparacion = resultado[3]
        
        return factura_encontrada

    def obtener_ventas_por_rango(self, fecha_inicio, fecha_fin, cursor):
       
        resultados = []
     
        sql =  """
                SELECT f.fecha, SUM(f.total) as total_ventas, SUM(r.costo_repuesto) as total_repuestos
                FROM factura f
                JOIN reparacion r ON f.id_reparacion = r.id_reparacion
                where f.fecha BETWEEN %s AND %s
                GROUP BY f.fecha
                ORDER BY f.fecha ASC
            """
        valores = (fecha_inicio, fecha_fin)
        cursor.execute(sql, valores)

        resultados = cursor.fetchall()
            
        return resultados


        