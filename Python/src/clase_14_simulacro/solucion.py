from queue import LifoQueue as Pila


# Ejercicio 1
def sumatoria(s: list[int]) -> int:
    total:int = 0

    for i in s:
        total += i

    return total


def ejercicio1(s: list[int], n: int) -> list[int]:
    res: list[int] = []
    aux: list[int] = []

    for i in s:
        aux.append(i)

        if sumatoria(aux) > n or aux[0] == n:
            aux.clear()
        elif sumatoria(aux) == n:
            if len(res) == 0:
                res = aux.copy()
            elif aux[0] > res[0]:
                res = aux.copy()

    return res


# Ejercicio 2
def ejercicio2(examenes: Pila[(str, int)]) -> Pila[str]:
    res: Pila[str] = Pila()
    tema_1: Pila[str] = Pila()
    tema_2: Pila[(str, int)] = Pila()

    while not examenes.empty():
        item: tuple[str, int] = examenes.get()

        if item[1] == 1:
            tema_1.put(item[0])
        else:
            tema_2.put(item)

    while not tema_1.empty():
        item: tuple[str, int] = tema_1.get()
        res.put(item)

    while not tema_2.empty():
        item: tuple[str, int] = tema_2.get()
        examenes.put(item)
    
    return res


# Ejercicio 3
def ejercicio3(A: list[list[int]]) -> None:
    for i in range(0, len(A)):
        A[i].append(minimo_de_lista(A[i]))


def minimo_de_lista(lista: list[int]) -> int:
    min: int = lista[0]

    for i in lista:
        if i < min:
            min = i

    return min


# Ejercicio 4
def ejercicio4(eleccion1: dict[str, str], eleccion2: dict[str, str]) -> dict[str, int]:
    res: dict[str, int] = {}

    for i in eleccion1.keys():
        if eleccion1[i] == eleccion2[i]:
            if not eleccion1[i] in res.keys():
                res[eleccion1[i]] = 1
            else:
                res[eleccion1[i]] += 1

    return res


# Ejercicio 5
def ejercicio5(a:int, b:int) -> int:
    if a > 0 and b % 2 == 0:
        return 1
    if a == 0 or b > 10:
        return 2
    return 3
# [ ] Casos de prueba: (1,2), (1,11), (1,3)
# [x] Casos de prueba: (1,2), (0,3), (1,11)
# [ ] Casos de prueba: (1,2), (1,11), (0,11), (1,1)


# Ejercicio 6 - nombre adecuado para la función a definir en el ejercicio 3
# [ ] eliminar_fila_con_minimo_de_columna
# [ ] agregar_fila_con_minimo_de_columna
# [x] agregar_columna_con_minimo_de_fila
# [ ] eliminar_columna_con_minimo_de_fila

# Comprobante de entrega: Evjz-GLO