from tkinter import messagebox
import DAO.FacturasDAO as factura_dao

class LogicaFactura:
    def __init__(self):
        self.factura_dao = factura_dao.FacturasDAO()

    def agregar_factura(self, modelo_factura):
        return self.factura_dao.agregar_factura(modelo_factura)
    
    def obtener_garantia_por_id(self, id_factura):
        return self.factura_dao.obtener_factura_por_id(id_factura)

    def obtener_factura_por_id_reparacion(self, id_reparacion):
        return self.factura_dao.obtener_factura_por_id_reparacion(id_reparacion)
        
    def obtener_ventas_por_rango(self, fecha_inicio, fecha_fin):
        return self.factura_dao.obtener_ventas_por_rango(fecha_inicio, fecha_fin)