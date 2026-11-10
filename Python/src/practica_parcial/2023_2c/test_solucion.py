import unittest

from solucion import (
    es_capicua,
    frecuencia_posiciones_por_caballo,
    ind_nesima_aparicion,
    matriz_capicua,
    mezclar,
)


class test_ind_nesima_aparicion(unittest.TestCase):
    def test_ind_nesima_aparicion_ok(self):
        s = [-1, 1, 1, 5, -7, 1, 3]
        n = 2
        e = 1
        self.assertEqual(ind_nesima_aparicion(s, n, e), 2)


class test_mezclar(unittest.TestCase):
    def test_mezclar_ok(self):
        s1 = [1, 3, 0, 1]
        s2 = [4, 0, 2, 3]
        res = [1, 4, 3, 0, 0, 2, 1, 3]
        self.assertEqual(mezclar(s1, s2), res)


class test_frecuencia_posiciones_por_caballo(unittest.TestCase):
    def test_frecuencia_posiciones_por_caballo_ok(self):
        caballos = ["linda", "petisa", "mister", "luck"]
        carreras = {
        "carrera1": ["linda", "petisa", "mister", "luck"],
        "carrera2": ["petisa", "mister", "linda", "luck"]
        }
        res: dict[str, list[int]] = {
          "petisa": [1,1,0,0],
          "mister": [0,1,1,0],
          "linda": [1,0,1,0],
          "luck": [0,0,0,2]
        }
        self.assertEqual(frecuencia_posiciones_por_caballo(caballos, carreras), res)


class test_matriz_capicuao(unittest.TestCase):
    def test_matriz_capicua_ok(self):
        m = [[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]
        self.assertTrue(matriz_capicua(m))

    def test_lista_capicua_ok(self):
        l = [1,2,3,2,1]
        self.assertTrue(es_capicua(l))

    def test_lista_no_es_capicua(self):
        l = [1,2,0,3,2,1]
        self.assertFalse(es_capicua(l))

if __name__ == '__main__':
    unittest.main()
