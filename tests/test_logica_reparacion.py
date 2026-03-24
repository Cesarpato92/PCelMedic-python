import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Logica.LogicaReparacion import LogicaReparacion
from Modelo.ModeloReparacion import ModeloReparacion


def test_validaciones_reparacion():
  
    print("Probando validaciones de reparacion")
    print("-"*50)

    logica = LogicaReparacion()

    # 014 - Validar el cambio de estado de "En proceso" a "Completada"
    print("\nprueba 014 Cambio: En Proceso a Completada")
    reparacion1 = ModeloReparacion()
    reparacion1.id_reparacion = 1
    reparacion1.estado = "Completada"
    reparacion1.comentarios = "Se cambio la pantalla con exito"
    reparacion1.costo_repuestos = 150000
    estado_antiguo = "En Proceso"
    resultado1, mensaje1 = logica.validacion_datos_cambiar_estado(reparacion1, estado_antiguo)
    print(f"Resultado: {'VALIDO' if resultado1 else 'INVALIDO'}")
    if not resultado1:
        print(f"Motivo: {mensaje1}")
    assert resultado1 == True

    # 015 - Validar el cambio de estado de "Completada" a "En proceso"
    print("\nprueba 015 Cambio: Completada a En Proceso")
    reparacion2 = ModeloReparacion()
    reparacion2.id_reparacion = 2
    reparacion2.estado = "En Proceso"
    reparacion2.comentarios = "Se cambio la pantalla con exito"
    reparacion2.costo_repuestos = 150000
    estado_antiguo = "Completada"
    resultado2, mensaje2 = logica.validacion_datos_cambiar_estado(reparacion2, estado_antiguo)
    
    print(f"Resultado: {'VALIDO' if resultado2 else 'INVALIDO'}")
    if not resultado2:
        print(f"Motivo: {mensaje2}")
    assert resultado2 == False, {mensaje2}
    

if __name__ == "__main__":
    
    test_validaciones_reparacion()
    print("\n" + "-" * 50)
    print("Todas las pruebas completadas de forma exitosa")