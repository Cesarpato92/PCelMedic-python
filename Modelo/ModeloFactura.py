class ModeloFactura:

    def __init__(self):
        self._id_factura = None
        self._fecha = None
        self._total = None
        self._id_reparacion = None

    #Método especial para representación en string 
    def __str__(self):
        return (f"Factura: {self._id_factura} (Fecha: {self._fecha}, "
                f"Total: {self._total})")
    
    "Getters y Setters"
    @property
    def id_factura(self):
        return self._id_factura

    @id_factura.setter
    def id_factura(self, id_factura):
        self._id_factura = id_factura

    @property
    def fecha(self):
        return self._fecha
    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def total(self):
        return self._total
    @total.setter
    def total(self, total):
        self._total = total

    @property
    def id_reparacion(self):
        return self._id_reparacion
    @id_reparacion.setter
    def id_reparacion(self, id_reparacion):
        self._id_reparacion = id_reparacion

    