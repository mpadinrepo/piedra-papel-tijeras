# # test_Tarefa42.py
# import unittest
# from Tarefa42 import calcular_iva_21, calcular_iva_04, aplicar_descuento, calcular_total_compra

# class TestTarefa42(unittest.TestCase):
#     def test_calcular_iva_21(self):
#         self.assertEqual(calcular_iva_21(100), 21.0)
#         self.assertEqual(calcular_iva_21(50), 10.5)

#     def test_calcular_iva_04(self):
#         self.assertEqual(calcular_iva_04(100), 4.0)
#         self.assertEqual(calcular_iva_04(50), 2.0)

#     def test_aplicar_descuento(self):
#         self.assertEqual(aplicar_descuento(100), 10.0)
#         self.assertEqual(aplicar_descuento(50), 5.0)

#     def test_calcular_total_compra(self):
#         lista_compra = [
#             {'precio_sin_iva': 100, 'funcion_iva': calcular_iva_21, 'funcion_descuento': aplicar_descuento},
#             {'precio_sin_iva': 50, 'funcion_iva': calcular_iva_04, 'funcion_descuento': None},
#             # Agrega más productos según sea necesario
#         ]

#         total, iva, descuento = calcular_total_compra(lista_compra)

#         # Verifica que el resultado total sea correcto
#         self.assertEqual(total, 163.0)

#         # Verifica que el resultado del IVA sea correcto
#         self.assertEqual(iva, 23.0)

#         # Verifica que el resultado del descuento sea correcto
#         self.assertEqual(descuento, 10.0)

# if __name__ == '__main__':
#     unittest.main()

import pytest
from Tarefa42 import calcular_iva_21, calcular_iva_04, aplicar_descuento, calcular_total_compra
from tu_programa import calcular_iva_21, calcular_iva_04, aplicar_descuento, calcular_total_compra

def test_calcular_iva_21():
    assert float(calcular_iva_21(100)) == 21.0
def test_calcular_iva_04():
    assert float(calcular_iva_04(100)) == 4.0