import unittest
from ej_1 import cuenta_regresiva_y_es_par

class test_cuenta_regresiva_y_es_par(unittest.TestCase):

    def test_case_1(self):
        self.assertTrue(cuenta_regresiva_y_es_par(10))

    def test_case_2(self):
        self.assertFalse(cuenta_regresiva_y_es_par(11))

    def test_case_3(self):
        self.assertEqual(cuenta_regresiva_y_es_par(12), True)

if __name__ == '__main__':
    unittest.main(verbosity = 2)
