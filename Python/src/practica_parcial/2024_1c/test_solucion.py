import unittest
from queue import Queue as Cola

from solucion import (
    alarma_epidemiologica,
    empleados_del_mes,
    nivel_de_ocupacion,
    orden_de_atencion,
)


def cola_desde_lista(elementos):
    c = Cola()
    for e in elementos:
        c.put(e)
    return c


def lista_desde_cola(cola):
    resultado = []
    while not cola.empty():
        resultado.append(cola.get())
    return resultado


class TestParcial(unittest.TestCase):

    # Ejercicio 1: alarma_epidemiologica
    def test_alarma_epidemiologica(self):
        registros = [
            (1, "dengue"), (2, "gripe"), (3, "dengue"), (4, "covid"),
            (5, "dengue"), (6, "fractura"), (7, "sarampion"), (8, "covid"),
        ]
        infecciosas = ["dengue", "covid", "sarampion", "gripe"]
        umbral = 0.25
        esperado = {"dengue": 0.375, "covid": 0.25}
        self.assertEqual(alarma_epidemiologica(registros, infecciosas, umbral), esperado)

    # Ejercicio 2: orden_de_atencion
    def test_orden_de_atencion(self):
        urgentes = cola_desde_lista([7, 3, 9])
        postergables = cola_desde_lista([4, 8, 1])
        esperado = [7, 4, 3, 8, 9, 1]
        res = orden_de_atencion(urgentes, postergables)
        self.assertEqual(lista_desde_cola(res), esperado)

    # Ejercicio 3: nivel_de_ocupacion
    def test_nivel_de_ocupacion(self):
        camas_por_piso = [
            [True, False, True, False],    # 2/4 = 0.5
            [True, True, True, True],      # 4/4 = 1.0
            [False, False, False, False],  # 0/4 = 0.0
            [True, False, False, False],   # 1/4 = 0.25
        ]
        esperado = [0.5, 1.0, 0.0, 0.25]
        self.assertEqual(nivel_de_ocupacion(camas_por_piso), esperado)

    # Ejercicio 4: empleados_del_mes
    def test_empleados_del_mes(self):
        horas = {
            1: [8, 8, 8],    # 24
            2: [10, 7, 7],   # 24
            3: [4, 4, 4],    # 12
            4: [12, 6, 6],   # 24
            5: [6, 6, 6],    # 18
        }
        self.assertEqual(sorted(empleados_del_mes(horas)), [1, 2, 4])

    def test_empleados_del_mes_2(self):
        horas = {
            1: [1, 1, 1],    # 03
            2: [10, 7, 7],   # 24
            3: [4, 4, 4],    # 12
            4: [12, 6, 6],   # 24
            5: [6, 10, 10],  # 26
        }
        self.assertEqual(sorted(empleados_del_mes(horas)), [5])


if __name__ == "__main__":
    unittest.main()
