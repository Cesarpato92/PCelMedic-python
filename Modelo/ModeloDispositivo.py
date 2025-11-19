class ModeloDispositivo:
    def __init__(self):
        self._id_dispositivo = None
        self._marca = None
        self._tipo_reparacion = None
        self._tipo_password = None
        self._password = None
        self._comentarios = None
        self._id_cliente = None

    #Método especial para representación en string 
    def __str__(self):
        return (f"Dispositivo: {self._tipo_reparacion} {self._marca} {self._tipo_password} "
                f"(Password: {self._password}, Comentarios: {self._comentarios})")
    
    "Getters y Setters"
    @property
    def id_dispositivo(self):
        return self._id_dispositivo
    @id_dispositivo.setter
    def id_dispositivo(self, id_dispositivo):
        self._id_dispositivo = id_dispositivo
    
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tipo_reparacion(self):
        return self._tipo_reparacion
    @tipo_reparacion.setter
    def tipo_reparacion(self, tipo_reparacion):
        self._tipo_reparacion = tipo_reparacion

    @property
    def tipo_password(self):
        return self._tipo_password
    @tipo_password.setter
    def tipo_password(self, tipo_password):
        self._tipo_password = tipo_password

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        self._password = password
    
    @property
    def comentarios(self):
        return self._comentarios    
    @comentarios.setter
    def comentarios(self, comentarios):
        self._comentarios = comentarios

    @property
    def id_cliente(self):
        return self._id_cliente
    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self._id_cliente = id_cliente