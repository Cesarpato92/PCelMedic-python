class ModeloReparacion:

    def __init__(self):
        self._id_reparacion = None
        self._fecha_ingreso = None
        self._estado = None
        self._costo_repuestos = None
        self._precio_reparacion = None
        self._comentarios = None
        self._id_dispositivo = None

    #Método especial para representación en string 
    def __str__(self):
        return (f"Reparación: {self._id_reparacion} (Fecha Ingreso: {self._fecha_ingreso}, "
                f"Estado: {self._estado}, Costo Repuestos: {self._costo_repuestos}, "
                f"Precio Reparación: {self._precio_reparacion}, Comentarios: {self._comentarios})")
    
    "Getters y Setters"
    @property
    def id_reparacion(self):
        return self._id_reparacion
    @id_reparacion.setter
    def id_reparacion(self, id_reparacion):
        self._id_reparacion = id_reparacion
    
    @property
    def fecha_ingreso(self):
        return self._fecha_ingreso
    @fecha_ingreso.setter
    def fecha_ingreso(self, fecha_ingreso):
        self._fecha_ingreso = fecha_ingreso

    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def costo_repuestos(self):
        return self._costo_repuestos
    @costo_repuestos.setter
    def costo_repuestos(self, costo_repuestos):
        self._costo_repuestos = costo_repuestos

    @property
    def precio_reparacion(self):
        return self._precio_reparacion
    @precio_reparacion.setter
    def precio_reparacion(self, precio_reparacion):
        self._precio_reparacion = precio_reparacion

    @property
    def comentarios(self):
        return self._comentarios
    @comentarios.setter
    def comentarios(self, comentarios):
        self._comentarios = comentarios

    @property
    def id_dispositivo(self):
        return self._id_dispositivo
    @id_dispositivo.setter
    def id_dispositivo(self, id_dispositivo):
        self._id_dispositivo = id_dispositivo