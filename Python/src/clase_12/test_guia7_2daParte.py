"""
Introducción a la Programación 
2do Cuatrimestre 2026
Práctica 7: Matrices
"""
import unittest
from guia7_2daParte import ordenados, sumatoria_de_matriz, columna, columnas_ordenadas

"""
Tests Ordenados
"""
class Test_ordenados(unittest.TestCase):

    def test_1(self):
        lista = [0]
        self.assertTrue(ordenados(lista))

    def test_2(self):
        lista = [1,2,3,4]
        self.assertTrue(ordenados(lista))

    def test_3(self):
        lista = [1,2,2]
        self.assertFalse(ordenados(lista))

    def test_4(self):
        lista = [1,2,3,1,2,3]
        self.assertFalse(ordenados(lista))

    def test_5(self):
        lista = [3,2,1]
        self.assertFalse(ordenados(lista))


"""
Tests Sumar toda la matriz
"""
class Test_sumatoria_de_matriz(unittest.TestCase):

    def test_1(self):
        self.assertEqual(sumatoria_de_matriz([[1]]),1)

    def test_2(self):
        self.assertEqual(sumatoria_de_matriz([[1,1],[1,1]]),4)
    
    def test_3(self):
        self.assertEqual(sumatoria_de_matriz([[1,-1],[1,-1]]),0)

    def test_4(self):
        self.assertEqual(sumatoria_de_matriz([[1,1,1,1]]),4)


"""
Test Columna
"""
class Test_columna(unittest.TestCase):

    def test_1(self):
        m = [[0]]
        c = 0
        r = [0]
        self.assertEqual(columna(m, c), r)

    def test_2(self):
        m = [[0],[1],[2],[3]]
        c = 0
        r = [0,1,2,3]
        self.assertEqual(columna(m, c), r)
    
    def test_3(self):
        m = [[0,1],[1,2],[2,3],[3,4]]
        c = 1
        r = [1,2,3,4]
        self.assertEqual(columna(m, c), r)


"""
Tests Columnas Ordenadas
"""
class Test_columnas_ordenadas(unittest.TestCase):   

    def test_1(self):
        m = [[0]]
        r = [True]
        self.assertEqual(columnas_ordenadas(m), r)

    def test_2(self):
        m = [[0],[1],[2],[3]]
        r = [True]
        self.assertEqual(columnas_ordenadas(m), r)
    
    def test_3(self):
        m = [[0,1],[1,2],[2,3],[3,4]]
        r = [True,True]
        self.assertEqual(columnas_ordenadas(m), r)

    def test_4(self):
        m = [[1,1],[2,2],[2,3],[4,4]]
        r = [False,True]
        self.assertEqual(columnas_ordenadas(m), r)

    def test_5(self):
        m = [[0,1,2],[2,1,0],[2,3,4]]
        r = [False,False,False]
        self.assertEqual(columnas_ordenadas(m), r)

if __name__ == '__main__':
    unittest.main(verbosity=2)
