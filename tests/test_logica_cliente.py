import sys
import os

# Agregar la ruta del proyecto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Logica.LogicaCliente import LogicaCliente

def test_validaciones():
    
    logica = LogicaCliente()
    # Pruebas de validacion de cedula
    print("\nProbando validación de cedula")
    resultado1 = logica.validacion_cedula("123456789")
    print(f"Cedula '123456789': {'VALIDO' if resultado1 else 'INVALIDO'}")
    assert resultado1 == True
    
    resultado2 = logica.validacion_cedula("")
    print(f"Cedula vacía: {'VALIDO' if resultado2 else 'INVALIDO'}")
    assert resultado2 == False
    
    # validacion de nombre
    print("\nProbando validacien de nombre ")
    resultado3 = logica.validacion_nombre("Cesar")
    print(f"Nombre 'Cesar': {'VALIDO' if resultado3 else 'INVALIDO'}")
    assert resultado3 == True
    
    resultado4 = logica.validacion_nombre("")
    print(f"Nombre vacio: {'VALIDO' if resultado4 else 'INVALIDO'}")
    assert resultado4 == False
    
    # validación de email
    print("\nProbando validacion de email")
    resultado5 = logica.validacion_email("cesar@test.com")
    print(f"Email 'test@test.com': {'VALIDO' if resultado5 else 'INVALIDO'}")
    assert resultado5 == True
    
    resultado6 = logica.validacion_email("test.com")
    print(f"Email 'test.com': {'VALIDO' if resultado6 else 'INVALIDO'}")
    assert resultado6 == False
    
    # validación de celular
    print("\nProbando validacion de celular")
    resultado7 = logica.validacion_celular("3001234567")
    print(f"Celular '3001234567': {'VALIDO' if resultado7 else 'INVALIDO'}")
    assert resultado7 == True
    
    resultado8 = logica.validacion_celular("300abc")
    print(f"Celular '300abc': {'VALIDO' if resultado8 else 'INVALIDO'}")
    assert resultado8 == False
    
    print("\nValidaciones individuales OK")

if __name__ == "__main__":
    print("INICIANDO PRUEBAS DE VALIDACION")
    print("-" * 50)
    test_validaciones()
    print("Todas las pruebas completadas de forma exitosa")