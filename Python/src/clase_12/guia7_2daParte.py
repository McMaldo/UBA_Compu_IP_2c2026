"""
Introducción a la Programación 
2do Cuatrimestre 2026
Práctica 7: Matrices
"""

def ordenados(ns: list[int]) -> bool:
    for i in range(1, len(ns)):
        if not(ns[i-1] < ns[i]):
            return False
    return True


def sumatoria_de_matriz(matriz: list[list[int]]) -> int:
    total: int = 0
    for lista in matriz:
        for i in lista:
            total += i
    return total


def sumatoria_de_matriz_1(matriz: list[list[int]]) -> int:
    total: int = 0
    for i in range(len(matriz)):
        for k in range(len(matriz[i])):
            total += matriz[i][k]
    return total


def columna(matriz: list[list[int]],c) -> list[int]:
    res: list[int] = []
    for fila in matriz:
        for i in range(len(fila)):
            if i == c:
                res.append(fila[i])
            else:
                break
    return res


def columna_1(matriz: list[list[int]],c) -> list[int]:
    res: list[int] = []
    for fila in matriz:
        res.append(fila[c])
    return res


def columnas_ordenadas(matriz: list[list[int]]) -> list[bool]:
    res: list[bool] = []
    for i in range(len(matriz[0])):
        res.append(ordenados(columna(matriz, i)))
    return res


def columnas_ordenadas_1(matriz: list[list[int]]) -> list[bool]:
    matriz_por_col: list[list[int]] = []
    for i in range(len(matriz[0])):
        matriz_por_col.append(columna(matriz, i))
    res: list[bool] = []
    for col in matriz_por_col:
        res.append(ordenados(col))
    return res
