import re

class Validador:
    """Clase utilitaria para validaciones comunes en el sistema."""
    
    @staticmethod
    def validar_email(email):
        if not email:
            return False, "El correo electrónico es obligatorio."
        if len(email) > 100:
            return False, "El correo electrónico es demasiado largo (máx 100)."
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, email):
            return False, "El formato del correo electrónico no es válido."
        return True, ""

    @staticmethod
    def validar_celular(celular):
        if not celular:
            return False, "El número de celular es obligatorio."
        if not celular.isdigit():
            return False, "El número de celular debe contener solo dígitos."
        if len(celular) != 10:
            return False, "El número de celular debe tener exactamente 10 dígitos."
        return True, ""

    @staticmethod
    def validar_cedula(cedula):
        if not cedula or cedula.strip() == "":
            return False, "La cédula no puede estar vacía."
        if not cedula.isdigit():
            return False, "La cédula debe contener solo dígitos."
        if len(cedula.strip()) > 20:
            return False, "La cédula debe tener máximo 20 dígitos."
        return True, ""

    @staticmethod
    def validar_nombre(nombre, max_len=150):
        if not nombre or nombre.strip() == "":
            return False, "El nombre es obligatorio."
        if len(nombre) > max_len:
            return False, f"El nombre no puede superar los {max_len} caracteres."
        return True, ""

    @staticmethod
    def validar_precio(precio):
        try:
            val = float(precio)
            if val <= 0:
                return False, "El precio debe ser mayor a cero."
            return True, ""
        except (ValueError, TypeError):
            return False, "El precio debe ser un número válido."

    @staticmethod
    def validar_id(id_val, nombre_campo="ID"):
        if not str(id_val).isdigit():
            return False, f"El {nombre_campo} debe ser un número."
        val = int(id_val)
        if val <= 0:
            return False, f"El {nombre_campo} no puede ser negativo o cero."
        if val > 2147483647:
            return False, f"El {nombre_campo} supera el valor permitido."
        return True, ""
