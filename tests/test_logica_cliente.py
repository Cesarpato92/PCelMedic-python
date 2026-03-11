import sys
import os

# Agregar la ruta del proyecto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Logica.LogicaCliente import LogicaCliente

def test_validaciones():
    
    logica = LogicaCliente()
    
    # Cedula
    assert logica.validacion_cedula("123456789") == True
    assert logica.validacion_cedula("") == False
    
    # Nombre
    assert logica.validacion_nombre("Juan") == True
    assert logica.validacion_nombre("") == False
    
    # Email
    assert logica.validacion_email("test@test.com") == True
    assert logica.validacion_email("test.com") == False
    
    # Celular
    assert logica.validacion_celular("3001234567") == True
    assert logica.validacion_celular("300abc") == False
    
    print("Validaciones individuales OK")


if __name__ == "__main__":
    test_validaciones()
    print("Todas las pruebas completadas.")