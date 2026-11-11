""" Parcial de Python del primer cuatrimestre de 2025. """

from queue import LifoQueue as Pila


def prefijo_que_mas_suma(v: list[int]) -> int:
    max: int = v[0]

    for i in v:
        if max < i:
            max = i

    return max


def primera_entrega_en_blanco(parciales: Pila[tuple[str, int]]) -> str:
    resultado : str = ""
    return resultado


def desplazar_columna_hacia_arriba(A: list[list[int]], col: int) -> None:
    return


def armar_ranking(podios: list[dict[int, str]]) -> dict[str, int]:
    resultado : dict[str, int] = {}

    return resultado
