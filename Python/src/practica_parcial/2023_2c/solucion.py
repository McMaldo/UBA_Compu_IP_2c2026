# Ejercicio 1
# 47'
def ind_nesima_aparicion(s: list, n: int, elem: int) -> int:
    """
    dada una secuencia de enteros s, y dos enteros n y elem devuelve la posición en la cual elem aparece por n-ésima vez en s.

    Requires:
        n > 0

    Args:
        s   (list): secuencia de colectivos que pasan por la parada
        n    (int): cuantass veces tiene que aparecer el mismo colectivo
        elem (int): cual es la linea de colectivo

    Returns:
        int: posición en la cual elem aparece por n-ésima vez en s. En caso de que elem aparezca menos de n veces en s, devolver -1.
    """
    apariciones: int = 0

    for i in range(len(s)):
        if s[i] == elem:
            apariciones += 1

        if apariciones == n:
            return i

    return -1


# Ejercicio 2
# 35'
def mezclar(s1: list, s2: list) -> list:
    res: list = []

    for i in range(len(s1)):
        res.append(s1[i])
        res.append(s2[i])

    return res


# Ejercicio 3
# 40'
def frecuencia_posiciones_por_caballo(caballos: list, carreras: dict) -> dict:
    """
    Genera un diccionario de caballos:#posiciones, que para cada caballo devuelva la lista de cuántas veces salió en esa posición.

    Args:
        caballos (list): lista de caballos que corrieron las carreras
        carreras (dict): resultados del hipódromo en el formato carreras:posiciones_caballos

    Returns
        dict[carreras:posiciones_caballos]: diccionario de caballos:#posiciones, que para cada caballo devuelva la lista de cuántas veces salió en esa posición.
    """
    res: dict[str, list[int]] = {}

    for carrera in carreras.values():
        for posicion in range(len(carrera)):
            caballo_actual: str = carrera[posicion]

            if not caballo_actual in res:
                res[caballo_actual] = [0,0,0,0]

            res[caballo_actual][posicion] += 1

    return res


# Ejercicio 4
# 20'
def matriz_capicua(m: list) -> bool:
    for l in m:
        if not es_capicua(l):
            return False

    return True


def es_capicua(l: list) -> bool:
    j: int = len(l)

    for i in range(j):
        if l[i] != l[j-1]:
            return False
        j -= 1

    return True


# Total: 47' + 35' + 40' + 20' = 2h 22'
