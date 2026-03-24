import sys
import os
import pytest

# Agregar la ruta del proyecto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Logica.LogicaCliente import LogicaCliente

def test_validaciones():
    
    logica = LogicaCliente()
    # Pruebas de validacion de cedula
    print("\nProbando validación de cedula")
    print("-"*50)
    #001 - validar cedula solo numeros
    resultado1, _ = logica.validacion_cedula("1234567890")
    print("#001 - validar cedula solo numeros")
    print(f"Cedula '123456789': {'VALIDO' if resultado1 else 'INVALIDO'}")
    assert resultado1 == True
    
    #002 - Validar cedula numeros y letras
    resultado2, mensaje = logica.validacion_cedula("123456789A")
    print(" #002 - Validar cedula numeros y letras")
    print(f"Cedula '123456789A': {'VALIDO' if resultado2 else 'INVALIDO'}")
    if not resultado2:
        print(f"Motivo: {mensaje}")
    assert resultado2 == False, {mensaje}

    #003 - Validar cedula vacia
    resultado3, mensaje = logica.validacion_cedula(" ")
    print("#003 - Validar cedula vacia")
    print(f"Cedula vacia: {'VALIDO' if resultado3 else 'INVALIDO'}")
    if not resultado3:
        print(f"Motivo: {mensaje}")
    assert resultado3 == False, {mensaje}
    
    # validación de email
    print("\nProbando validacion de email")
    print("-"*50)
    #004 - validar formato correcto email
    resultado4, _ = logica.validacion_email("cesar@test.com")
    print("#004 - validar formato correcto email")
    print(f"Email 'cesar@test.com': {'VALIDO' if resultado4 else 'INVALIDO'}")
    assert resultado4 == True
    
    #005 - validar email sin dominio
    resultado5, mensaje = logica.validacion_email("cesar@.com")
    print("#005 - validar email sin dominio")
    print(f"Email'cesar@.com': {'VALIDO' if resultado5 else 'INVALIDO'}")
    if not resultado5:
        print(f"Motivo: {mensaje}")
    assert resultado5 == False, {mensaje}
    
    #006 - Validar email sin @
    resultado6, mensaje = logica.validacion_email("cesartest.com")
    print("#006 - Validar email sin @")
    print(f"Email'cesartest.com': {'VALIDO' if resultado6 else 'INVALIDO'}")
    if not resultado6:
        print(f"Motivo: {mensaje}")
    assert resultado6 == False, {mensaje}
    
    # validacion de nombre
    print("\nProbando validación de nombre ")
    print("-"*50)
    #007 - validar nombre solo letras
    resultado7, _ = logica.validacion_nombre("Cesar")
    print("#007 - validar nombre solo letras")
    print(f"Nombre 'Cesar': {'VALIDO' if resultado7 else 'INVALIDO'}")
    assert resultado7 == True
    
    #008 - validar nombre usando letras y numeros
    resultado8, mensaje = logica.validacion_nombre("Cesar4")
    print("#008 - validar nombre usando letras y numeros")
    print(f"Nombre 'Cesar4': {'VALIDO' if resultado8 else 'INVALIDO'}")
    if not resultado8:
        print(f"Motivo: {mensaje}")
    assert resultado8 == False, {mensaje}
    
    
    # validación de celular 
    print("\nProbando validacion de celular")
    print("-"*50)
    # 009 - Validacion numero entre 7 y 15 caracteres
    resultado9, _ = logica.validacion_celular("3001234567")
    print("#009 - Validacion numero entre 7 y 15 caracteres")
    print(f"Celular '3001234567': {'VALIDO' if resultado9 else 'INVALIDO'}")
    assert resultado9 == True
    
    #010 - Validacion numeros y letras
    resultado10, _ = logica.validacion_celular("3002012abc")
    print("#010 - Validacion numeros y letras")
    print(f"Celular '3002012abc': {'VALIDO' if resultado10 else 'INVALIDO'}")
    if not resultado10:
        print(f"Motivo: {mensaje}")
    assert resultado10 == False, {mensaje}

    print("\nValidaciones individuales OK")

if __name__ == "__main__":
    print("Iniciando pruebas de logica de cliente")
    print("-" * 50)
    test_validaciones()
    print("Todas las pruebas completadas de forma exitosa")
    print("-"*50)