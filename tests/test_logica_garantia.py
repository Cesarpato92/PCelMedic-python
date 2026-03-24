import sys
import os
from datetime import datetime
from unittest.mock import Mock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Logica.LogicaGarantia import LogicaGarantia
from Modelo.ModeloGarantia import ModeloGarantia


def test_validaciones_garantia():

    
    print("Iniciando validaciones de garantia")
    print("-"*60)
    
    logica = LogicaGarantia()
    
    #Prueba 016 - Cambio de "En Garantia" a "Completada"
    print("\nPrueba 016 - Cambio: En Garantia a Completada")
    print("-" * 50)
    
    garantia1 = ModeloGarantia()
    garantia1.id_garantia = 1
    garantia1.estado = "Completada"
    garantia1.comentarios_finales = "Cambio de modulo defectuoso OK"
    garantia1.precio_insumos = 150000
    garantia1.fecha_fin = datetime.now().strftime("%Y-%m-%d") 
    estado_antiguo1 = "En Garantia"
    
    resultado1, mensaje1 = logica.validar_campos_a_actualizar(garantia1, estado_antiguo1)
    print(f"\nEstado anterior: {estado_antiguo1}")
    print(f"Estado nuevo: {garantia1.estado}")
    print(f"Precio insumos: {garantia1.precio_insumos}")
    print(f"Fecha fin: {garantia1.fecha_fin}")
    print(f"Comentarios finales: {garantia1.comentarios_finales}")
    print(f"Resultado: {'VALIDO' if resultado1 else 'INVALIDO'}")
    if not resultado1:
        print(f"Motivo: {mensaje1}")
    assert resultado1 == True

    #Prueba 017 - Cambio de "En Garantia" a "Rechazada"
    print("\nPrueba 017 - Cambio: En Garantia a Rechazada")
    print("-" * 40)
    
    garantia2 = ModeloGarantia()
    garantia2.id_garantia = 2
    garantia2.estado = "Rechazada"
    garantia2.comentarios_finales = "No cumple la garantia"
    garantia2.precio_insumos = 0
    garantia2.fecha_fin = datetime.now().strftime("%Y-%m-%d") 
    estado_antiguo2 = "En Garantia"
    
    resultado2, mensaje2 = logica.validar_campos_a_actualizar(garantia2, estado_antiguo2)
    print(f"Estado anterior: {estado_antiguo2}")
    print(f"Estado nuevo: {garantia2.estado}")
    print(f"Precio insumos: {garantia2.precio_insumos}")
    print(f"Fecha fin: {garantia2.fecha_fin}")
    print(f"Comentarios finales: {garantia2.comentarios_finales}")
    print(f"Resultado: {'VALIDO' if resultado2 else 'INVALIDO'}")
    if not resultado2:
        print(f"Motivo: {mensaje2}")
    assert resultado2 == True

    #Prueba 018 - Cambio de "Completada" a "Rechazada"
    print("\nPrueba 018 - Cambio: Completada a Rechazada")
    print("-" * 40)
    
    garantia3 = ModeloGarantia()
    garantia3.id_garantia = 3
    garantia3.estado = "Rechazada"
    garantia3.comentarios_finales = "No se encontro el repuesto"
    garantia3.precio_insumos = 0
    garantia3.fecha_fin = datetime.now().strftime("%Y-%m-%d") 
    estado_antiguo3 = "Completada"
    
    resultado3, mensaje3 = logica.validar_campos_a_actualizar(garantia3, estado_antiguo3)
    print(f"Estado anterior: {estado_antiguo3}")
    print(f"Estado nuevo: {garantia3.estado}")
    print(f"Precio insumos: {garantia3.precio_insumos}")
    print(f"Fecha fin: {garantia3.fecha_fin}")
    print(f"Comentarios finales: {garantia3.comentarios_finales}")
    print(f"Resultado: {'VALIDO' if resultado3 else 'INVALIDO'}")
    if not resultado3:
        print(f"Motivo: {mensaje3}")
    assert resultado3 == False, f"{mensaje3}"



if __name__ == "__main__":
    test_validaciones_garantia()
    print("\n" + "-" * 50)
    print("Todas las pruebas completadas de forma exitosa")
    print("-"*50)