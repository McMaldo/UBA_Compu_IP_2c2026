import random
from array import array

# Parte 4
# Ej 3
"""
Vamos a escribir un programa para simular el juego conocido como 7 y medio. 

El mismo deber ́a generar un n ́umero aleatorio entre 0 y 12 (excluyendo el 8 y 9) 
y deber ́a luego preguntarle al usuario si desea seguir sacando otra “carta” o plantarse. 

En este  ́ultimo caso el programa debe terminar. Los numeros aleatorios obtenidos deberan sumarse segun
el numero obtenido salvo por las “figuras” (10, 11 y 12) que sumar ́an medio punto cada una. El programa debe ir
acumulando los valores y si se pasa de 7.5 debe informar que el usuario ha perdido. Al finalizar la funci ́on devuelve
el historial de “cartas” que hizo que el usuario gane o pierda. Para generar n ́umeros pseudo-aleatorios entre 1 y 12
utilizaremos la funci ́on random.randint(1,12). Al mismo tiempo, la funci ́on random.choice() puede ser de gran
ayuda a la hora de repartir cartas
"""

def sacar_nueva_carta() -> int:
    nueva_carta: int = random.randint(1,12)
    cartas_excluidas: array[int] = [8,9]
    if nueva_carta in cartas_excluidas:
        return sacar_nueva_carta()
    return nueva_carta


def pedir_accion(total: int, accion: str, estaRetirado: bool) -> None:
    acciones_validas: list[str] = ["N","n","P","p"]

    while not accion in acciones_validas:
        print("[P para Plantarte][N para Pedir una Nueva Carta]")
        accion = input("Tenés: "+str(total)+", Siguiente Acción: ")

        if accion == "P" or accion == "p":
            estaRetirado == False
            accion = ""


def siete_o_miedo() -> None:
    medio_punto: array[int] = [10,11,12]
    estaRetirado: bool = False
    total: float = 0
    historial: list[int] = []
    accion: str = ""

    while not estaRetirado:
        nueva_carta: int = sacar_nueva_carta()
        historial.append(nueva_carta)

        if nueva_carta in medio_punto:
            total += 0.5
        else:
            total += nueva_carta
        
        pedir_accion(total, accion, estaRetirado)

