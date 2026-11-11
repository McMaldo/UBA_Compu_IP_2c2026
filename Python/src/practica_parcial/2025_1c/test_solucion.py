import unittest
from queue import LifoQueue as Pila

from solucion import (
    armar_ranking,
    desplazar_columna_hacia_arriba,
    prefijo_que_mas_suma,
    primera_entrega_en_blanco,
)


class TestEjercicio1PrefijoQueMasSuma(unittest.TestCase):

    def test_prefijo_que_mas_suma(self):
        s = [2, -5, 4, 3, -1]
        self.assertEqual(prefijo_que_mas_suma(s), 4)


class TestEjercicio2PrimeraEntregaEnBlanco(unittest.TestCase):

    def test_primera_entrega_en_blanco(self):
        examenes = Pila()
        # Orden de entrega: Ana, Beto, Carla, Dani, Eze (Eze queda en el tope)
        for examen in [("Ana", 3), ("Beto", 0), ("Carla", 5), ("Dani", 0), ("Eze", 2)]:
            examenes.put(examen)
        # Beto y Dani entregaron en blanco, pero Beto fue el primero en entregar
        self.assertEqual(primera_entrega_en_blanco(examenes), "Beto")


class TestEjercicio3DesplazarColumnaHaciaArriba(unittest.TestCase):

    def test_desplazar_columna_hacia_arriba(self):
        A = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        desplazar_columna_hacia_arriba(A, 1)
        # La columna 1 era [2, 5, 8] y pasa a ser [5, 8, 2]; el resto queda igual
        esperado = [
            [1, 5, 3],
            [4, 8, 6],
            [7, 2, 9],
        ]
        self.assertEqual(A, esperado)


class TestEjercicio4ArmarRanking(unittest.TestCase):

    def test_armar_ranking(self):
        podios = [
            {1: "Ana", 2: "Beto", 3: "Carla"},
            {1: "Beto", 2: "Ana"},      # sin tercer puesto
            {1: "Carla", 3: "Ana"},     # sin segundo puesto
            {2: "Dani", 3: "Beto"},     # sin primer puesto
        ]
        # Ana: 3 + 2 + 1 + 0 = 6
        # Beto: 2 + 3 + 0 + 1 = 6
        # Carla: 1 + 0 + 3 + 0 = 4
        # Dani: 0 + 0 + 0 + 2 = 2
        esperado = {"Ana": 6, "Beto": 6, "Carla": 4, "Dani": 2}
        self.assertEqual(armar_ranking(podios), esperado)


if __name__ == "__main__":
    unittest.main()
