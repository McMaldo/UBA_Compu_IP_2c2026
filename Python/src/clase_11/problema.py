def suma_total(secuencia: list[int]) -> int:
    suma: int = 0
    for i in secuencia:
        suma += i
    return suma


def palabras_unidas(secuencia: list[str])-> str:
    res: str = ""
    for s in secuencia:
        if s != "" and res == "":
            res = s
        elif s != "":
            res += " " + s
    return res


def separar_por_comas(palabra: str) -> str:
    res: str = ""
    for c in palabra:
        if res == "":
            res = c
        else:
            res += "," + c
    return res


def promedio(numeros: int) -> float:
    suma: int = 0
    for n in numeros:
        suma += n
    return suma / len(numeros)


# Con la Función Nativa de Python
def pertenece(n: int, ns: list[int]) -> bool:
    return n in ns


# Con el Early Return de un For
def pertenece_1(n: int, ns: list[int]) -> bool:
    for i in ns:
        if n == i:
            return True
    return False


# Con Recursión
def pertenece_2(n: int, ns: list[int]) -> bool:
    if ns == []:
        return False
    if n == ns[0]:
        return True
    return pertenece_2(n, ns[1:])


# Con una Estructura Lógica con Recursión (ideal para Lazy)
def pertenece_3(n: int, ns: list[int]) -> bool:
    return (n == ns[0] or ns != []) and pertenece_3(n, ns[1:])


# Con un While y Lógica de Cortocircuito
def pertenece_4(n: int, ns: list[int]) -> bool:
    i: int = 0
    while i < len(ns) and ns[i] != n:
        i += 1
    return i < len(ns)


# Primer Procedimiento en Python
def ceros_en_posiciones_pares(ns: list[int]) -> None: # ns es un "inout"
    for i in range(0, len(ns), 2):
        ns[i] = 0
    # NO tiene Return porque es un Procedimiento
