import sys
import os
import pytest

#agregamos la ruta del proyecto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from  Utilidades.Validador import Validador


def test_validaciones():
    validador = Validador()

    #Pruebas de valicacion de precio
    print("\nProbando validación de precio")
    # 011 - Validadion de precio positivo
    precio1 = 150000
    resultado1, _ = validador.validar_precio(precio1)
    print (f"Precio {precio1} : {'VALIDO' if resultado1 else 'INVALIDO'}")
    assert resultado1 == True

    # 012 - validacion precio negativo
    precio2 = -100000
    resultado2, mensaje = validador.validar_precio(precio2)
    print (f"Precio {precio2} : {'VALIDO' if resultado2 else 'INVALIDO'}")
    if not resultado2:
        print(f"Motivo: {mensaje}")
    assert resultado2 == False, mensaje

    # 013 - Validacion precio usando texto
    precio3 = "cien"
    resultado3, mensaje = validador.validar_precio(precio3)
    print (f"Precio {precio3} : {'VALIDO' if resultado3 else 'INVALIDO'}")
    if not resultado3:
        print(f"Motivo: {mensaje}")
    assert resultado3 == False
    
    print("\nValidaciones individuales OK")


if __name__ == "__main__":
    print("INICIANDO PRUEBAS DE VALIDACION DE PRECIO")
    print("-" * 50)

    test_validaciones()
    print("Todas las pruebas completadas de forma exitosa")