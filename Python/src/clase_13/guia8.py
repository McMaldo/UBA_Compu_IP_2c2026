from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
from typing import TypeVar
 
T = TypeVar('T')

# Ejercicio 1.1
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    res: Pila[int] = Pila()
    for i in range(0,cantidad):
        numero_random: int = random.randint(desde,hasta)
        res.put(numero_random)
    return res

generar_nros_al_azar(10,1,10)

#auxiliares de pila
def pila_desde_lista (lista: list[T]) -> Pila[T]:
    res: Pila[int] = Pila()
    for i in lista:
        res.put(i)
    return res

def mostrar_pila (p: Pila[T]) -> None:
    res: list[T] = []
    while p.not_empty():
        res.append(p.get())
    print(res)

 
# Ejercicio 1.3
def buscar_el_maximo(p: Pila[int]) -> int:
    pila_aux: Pila[int] = Pila()
    max: int = p.get()
    pila_aux.put(max)

    while p.not_empty():
        first_in: int = p.get()
        pila_aux.put(first_in)
        if max < first_in:
            max = first_in
    
    while pila_aux.not_empty():
        first_in: int = pila_aux.get()
        p.put(first_in)

    return max
    
# Ejercicio 2.13.1
def armar_secuencia_de_bingo() -> Cola[int]:
    res: Cola[int] = Cola()
    numeros_jugados: list[int] = []

    while len(numeros_jugados) < 100:
        numero_sacado: int = random.randint(0,100)
        if not numero_sacado in numeros_jugados:
            res.put(numero_sacado)
            numeros_jugados.append(numero_sacado)

    return res

def armar_secuencia_de_bingo_2() -> Cola[int]:
    numeros: list[int] = list(range(0,100))
    random.shuffle(numeros)

    res: Cola[int] = Cola()
    for i in numeros:
        res.put(i)

    return res

# Ejercicio 2.13.2
def pertenece (cadena: list[T], elem:T) -> bool:
    for e in cadena:
        if elem == e:
            return True
    return False
    
def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    carton_sin_salir: list[int] = carton.copy()
    cantidad_jugadas: int = 0
    bolillas_sacadas: Cola[int] = Cola()

    while bolillero.not_empty():
        bolilla: int = bolillero.get()

        if pertenece(carton_sin_salir, bolilla):
            carton_sin_salir.remove(bolilla)
            cantidad_jugadas += 1
        
        bolillas_sacadas.put(bolilla)

    while bolillas_sacadas.not_empty():
        bolillero.put(bolillas_sacadas.get())

    return cantidad_jugadas


#auxiliares de cola
def cola_desde_lista (lista: list[T]) -> Cola[T]:
    pass

def mostrar_cola (c: Cola[T]) -> None:
    pass
