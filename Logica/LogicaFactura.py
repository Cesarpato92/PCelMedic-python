
class LogicaFactura:
    def __init__(self, factura_dao):
        self.factura_dao = factura_dao

    def agregar_factura(self, modelo_factura, cursor):
        return self.factura_dao.agregar_factura(modelo_factura, cursor)
    
    def obtener_garantia_por_id(self, id_factura, cursor):
        return self.factura_dao.obtener_factura_por_id(id_factura, cursor)

    def obtener_factura_por_id_reparacion(self, id_reparacion, cursor):
        return self.factura_dao.obtener_factura_por_id_reparacion(id_reparacion, cursor)
        
    def obtener_ventas_por_rango(self, fecha_inicio, fecha_fin, cursor):
        return self.factura_dao.obtener_ventas_por_rango(fecha_inicio, fecha_fin, cursor)