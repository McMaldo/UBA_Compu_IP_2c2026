import unittest
from queue import LifoQueue as Pila
from solucion import (
    ejercicio1,
    sumatoria,
    ejercicio2,
    ejercicio3,
    ejercicio4
)


class test_ejercicio_1(unittest.TestCase):
    """Tests para ejercicio1"""
    
    def test_ejercicio_1_ok(self):
        """
        Ejemplo: ejercicio1([1,3,2,5,4,1,8], 5) debe devolver [4,1]
        """
        res = ejercicio1([1, 3, 2, 5, 4, 1, 8], 5)
        self.assertEqual(res, [4, 1])

    def test_aux_sumatoria(self):
        res = sumatoria([1,2,3,4])
        self.assertEqual(res, 10)


class test_ejercicio_2(unittest.TestCase):
    """Tests para ejercicio2"""
    
    def test_ejercicio_2(self):
        """
        Ejemplo: Si examenes contiene (de tope a base) [("Ana",1),("Beto",2),("Caro",1)],
        entonces se debe devolver ["Ana","Caro"] y examenes contiene [("Beto",2)]
        """
        examenes = Pila()
        # Cargamos de base a tope: ("Caro",1), ("Beto",2), ("Ana",1)
        examenes.put(("Caro", 1))
        examenes.put(("Beto", 2))
        examenes.put(("Ana", 1))
        
        resultado = ejercicio2(examenes)

        # Verificar la pila resultante (tema 1)
        self.assertEqual(resultado.qsize(), 2)
        nombres_tema1 = []
        while not resultado.empty():
            nombres_tema1.append(resultado.get())
        self.assertEqual(nombres_tema1, ["Ana", "Caro"])
        
        # Verificar que examenes solo tiene tema 2
        self.assertEqual(examenes.qsize(), 1)
        self.assertEqual(examenes.get(), ("Beto", 2))


class test_ejercicio_3(unittest.TestCase):
    """Tests para ejercicio3"""

    def test_ejercicio_3(self):
        """
        Ejemplo: Si A = [[3,1],[2,2]], luego de ejecutar ejercicio3(A),
        A = [[3,1,1],[2,2,2]]
        """
        A = [[3, 1], [2, 2]]
        ejercicio3(A)
        self.assertEqual(A, [[3, 1, 1], [2, 2, 2]])


class test_ejercicio_4(unittest.TestCase):
    """Tests para ejercicio4"""
    
    def test_ejercicio_4(self):
        """
        Ejemplo: ejercicio4({"Ana":"X","Beto":"Y","Caro":"X"}, {"Ana":"X","Beto":"X","Caro":"X"})
        debe devolver {'X':2}
        """
        eleccion1 = {"Ana": "X", "Beto": "Y", "Caro": "X"}
        eleccion2 = {"Ana": "X", "Beto": "X", "Caro": "X"}
        resultado = ejercicio4(eleccion1, eleccion2)
        self.assertDictEqual(resultado, {'X': 2})


if __name__ == '__main__':
    unittest.main()
