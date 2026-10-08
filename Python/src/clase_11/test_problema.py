import unittest
from Python.src.clase_11.problema import palabras_unidas, suma_total

class test_suma(unittest.TestCase):

    def test_suma_vacia(self):
        secuencia: list[int] = []
        self.assertEqual(suma_total(secuencia), 0)
    
    def test_suma_todo_0(self):
        secuencia: list[int] = [0,0,0]
        self.assertEqual(suma_total(secuencia), 0)

    def test_suma_1_elem(self):
        secuencia: list[int] = [1]
        self.assertEqual(suma_total(secuencia), 1)

    def test_suma_n_elem(self):
        secuencia: list[int] = [1,2,3]
        self.assertEqual(suma_total(secuencia), 6)


class test_palabras_unidas(unittest.TestCase):
    
    def test_palabras_unidas_todo_largo_0(self):
        s: list[str] = ["","",""]
        self.assertEqual(palabras_unidas(s), "")

    def test_palabras_unidas_1_elem(self):
        s: list[str] = ["elem"]
        self.assertEqual(palabras_unidas(s), "elem")

    def test_palabras_unidas_elem_y_vacio(self):
        s: list[str] = ["elem",""]
        self.assertEqual(palabras_unidas(s), "elem")

    def test_palabras_unidas_n_elem(self):
        s: list[str] = ["1","2","3"]
        self.assertEqual(palabras_unidas(s), "1 2 3")


if __name__ == '__main__':
    unittest.main(verbosity=2)