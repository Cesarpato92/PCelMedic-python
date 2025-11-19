class ModeloCliente:
   
    _cedula = None
    _nombre = None
    _email = None
    _celular = None

    def __init__(self):
        pass
    
    #Método especial para representación en string 
    def __str__(self):
        return (f"Cliente: {self._nombre} (Cédula: {self._cedula}, "
                f"Email: {self._email}, Celular: {self._celular})")
    
    "Getters y Setters"
    @property
    def cedula(self):
        return self._cedula
    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email
    
    @property
    def celular(self):
        return self._celular
    @celular.setter
    def celular(self, celular):
        self._celular = celular