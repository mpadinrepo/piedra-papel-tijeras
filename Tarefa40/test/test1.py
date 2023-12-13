import unittest

def calcular_suma(n):
    resultado = n * (n + 1) // 2
    return resultado

class TestMiPrograma(unittest.TestCase):
    def test_calcular_suma_con_n_5(self):
        self.assertEqual(calcular_suma(5), 15)

    def test_calcular_suma_con_n_10(self):
        self.assertEqual(calcular_suma(10), 55)

    def test_calcular_suma_con_n_0(self):
        self.assertEqual(calcular_suma(0), 0)

    def test_calcular_suma_con_n_1(self):
        self.assertEqual(calcular_suma(1), 1)

if __name__ == '__main__':
    unittest.main()
