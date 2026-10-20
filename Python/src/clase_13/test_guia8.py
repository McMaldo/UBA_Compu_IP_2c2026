import unittest
from guia8 import *
from queue import LifoQueue as Pila
from queue import Queue as Cola

class buscar_el_maximo(unittest.TestCase):

    def test_maximo_caso_0(self):
        pila_0: Pila[int] = Pila()
        pila_0.put(0)
        pila_0.put(0)
        pila_0.put(0)
        pila_0.put(0)
        self.assertEqual(buscar_el_maximo(pila_0), 0)

    def test_maximo_caso_1(self):
        pila_0: Pila[int] = Pila()
        pila_1: Pila[int] = Pila()
        pila_0.put(10)
        pila_1.put(10)
        pila_0.put(3)
        pila_1.put(3)
        pila_0.put(7)
        pila_1.put(7)
        pila_0.put(9)
        pila_1.put(9)
        pila_0.put(9)
        pila_1.put(9)
        self.assertEqual(buscar_el_maximo(pila_0), 10)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
