from Modelo.ModeloGarantia import ModeloGarantia

class GarantiaDAO:
    def __init__(self):
        pass
    
    def agregar_garantia(self, modelo_garantia, cursor):
        sql = "INSERT INTO garantia (estado, observaciones, fecha_inicio, id_reparacion) " \
        "VALUES (%s, %s, %s, %s)"
        valores = (modelo_garantia.estado, modelo_garantia.observaciones, modelo_garantia.fecha_inicio, modelo_garantia.id_reparacion)
        cursor.execute(sql, valores)
        
        id_garantia = cursor.lastrowid    
        return id_garantia
    
    def obtener_garantia_por_id(self, id_garantia, cursor):
        
        garantia_encontrada = None

        sql = "SELECT id_garantia, estado, observaciones, fecha_inicio, fecha_fin, id_reparacion, precio_insumos, comentarios_finales FROM garantia WHERE id_garantia = %s"
        valores = (id_garantia,)

        cursor.execute(sql, valores)

        resultado = cursor.fetchone()

        if resultado:
            garantia_encontrada = ModeloGarantia()
            garantia_encontrada.id_garantia = resultado[0]
            garantia_encontrada.estado = resultado[1]
            garantia_encontrada.observaciones = resultado[2]
            garantia_encontrada.fecha_inicio = resultado[3]
            garantia_encontrada.fecha_fin = resultado[4]
            garantia_encontrada.id_reparacion = resultado[5]
            garantia_encontrada.precio_insumos = resultado[6]
            garantia_encontrada.comentarios_finales = resultado[7]                
       
        return garantia_encontrada

    def actualizar_garantia(self, modelo_garantia, cursor):
      

            sql = "UPDATE garantia SET estado = %s, fecha_fin = %s, precio_insumos = %s, comentarios_finales = %s WHERE id_garantia = %s"
            valores = (modelo_garantia.estado, modelo_garantia.fecha_fin, modelo_garantia.precio_insumos, modelo_garantia.comentarios_finales, modelo_garantia.id_garantia)
            
            cursor.execute(sql, valores)
            
            
            
          