from Modelo.ModeloDispositivo import ModeloDispositivo

class DispositivoDAO:

    def __init__(self):
        pass
    
    def agregar_dispositivo(self, modelo_dispositivo, cursor):
        
            sql = """INSERT INTO dispositivo (marca, tipo_reparacion, tipo_contrasena, contrasena, comentarios, id_cliente, version ) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            valores = (modelo_dispositivo.marca, 
                       modelo_dispositivo.tipo_reparacion,
                       modelo_dispositivo.tipo_password, 
                       modelo_dispositivo.password,
                       modelo_dispositivo.comentarios,
                       modelo_dispositivo.id_cliente,
                       modelo_dispositivo.version)
            cursor.execute(sql, valores)
            return cursor.lastrowid #Id del dispositivo


    def obtener_dispositivo_por_id(self, id_dispositivo, cursor):
       
        dispositivo_encontrado = None
        

        sql = "SELECT marca, tipo_reparacion, tipo_contrasena, contrasena, comentarios, id_cliente, version FROM dispositivo WHERE id_dispositivo = %s"
        #Ingresar primero el id_dispositivo al objeto modelo_dispositivo antes de llamar a este metodo
        valores = (id_dispositivo,)
            
        cursor.execute(sql, valores)

        #se obtiene el primer resultado
        resultado = cursor.fetchone()
        if resultado:
                
            dispositivo_encontrado = ModeloDispositivo()
            dispositivo_encontrado.id_dispositivo = id_dispositivo
            dispositivo_encontrado.marca = resultado[0]
            dispositivo_encontrado.tipo_reparacion = resultado[1]
            dispositivo_encontrado.tipo_password = resultado[2]
            dispositivo_encontrado.password = resultado[3]
            dispositivo_encontrado.comentarios = resultado[4]
            dispositivo_encontrado.id_cliente = resultado[5]
            dispositivo_encontrado.version = resultado[6]
                
        return dispositivo_encontrado