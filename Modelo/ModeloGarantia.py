class ModeloGarantia:

    def __init__(self):
        self._id_garantia = None
        self._estado = None
        self._observaciones = None
        self._fecha_inicio = None
        self._fecha_fin = None
        self._id_reparacion = None
        self._precio_insumos = None
        self._comentarios_finales = None

    #Método especial para representación en string 
    def __str__(self):
        return (f"Garantía: {self._id_garantia} (Estado: {self._estado}, "
                f"Observaciones: {self._observaciones}, Fecha Inicio: {self._fecha_inicio}, "
                f"Fecha Fin: {self._fecha_fin})")
    

    "Getters y Setters"
    @property
    def id_garantia(self):
        return self._id_garantia
    @id_garantia.setter
    def id_garantia(self, id_garantia):
        self._id_garantia = id_garantia

    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def observaciones(self):
        return self._observaciones
    @observaciones.setter
    def observaciones(self, observaciones):
        self._observaciones = observaciones

    @property
    def fecha_inicio(self):
        return self._fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio

    @property
    def fecha_fin(self):
        return self._fecha_fin
    
    @fecha_fin.setter
    def fecha_fin(self, fecha_fin):
        self._fecha_fin = fecha_fin

    @property
    def id_reparacion(self):
        return self._id_reparacion
    
    @id_reparacion.setter
    def id_reparacion(self, id_reparacion):
        self._id_reparacion = id_reparacion

    @property
    def precio_insumos(self):
        return self._precio_insumos
    
    @precio_insumos.setter
    def precio_insumos(self, precio_insumos):
        self._precio_insumos = precio_insumos

    @property
    def comentarios_finales(self):
        return self._comentarios_finales
    
    @comentarios_finales.setter
    def comentarios_finales(self, comentarios_finales):
        self._comentarios_finales = comentarios_finales
    