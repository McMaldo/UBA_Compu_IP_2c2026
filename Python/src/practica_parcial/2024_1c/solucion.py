from queue import Queue as Cola


# Ejercicio 1
# t: 45'
def alarma_epidemiologica (registros: list[tuple[int, str]], infecciosas: list[str], umbral: float) -> dict[str, float]:
    casos_infec: dict[str, int] = {}
    res: dict[str, float] = {}

    for r in registros:
        enfermedad: str = r[1]

        if enfermedad in infecciosas:

            if not enfermedad in casos_infec:
                casos_infec[enfermedad] = 0

            casos_infec[enfermedad] += 1

    for caso in casos_infec.items():
        porcentaje: float = caso[1] / len(registros)

        if porcentaje >= umbral:
            res[caso[0]] = porcentaje

    return res


# Ejercicio 2
# t: 8'
def orden_de_atencion (urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
    res: Cola = Cola()

    while not urgentes.empty():
       u: int = urgentes.get()
       p: int = postergables.get()
       res.put(u)
       res.put(p)

    return res


# Ejercicio 3
# t: 9'
def nivel_de_ocupacion(camas_por_piso:list[list[bool]]) -> list[float]:
    res: list[float] = []

    for piso in camas_por_piso:
        total_camas_ocupada: int = 0

        for cama_ocupada in piso:
            if cama_ocupada:
                total_camas_ocupada += 1

        res.append(total_camas_ocupada / len(piso))

    return res


# Ejercicio 4
# t: 22'
def empleados_del_mes(horas: dict[int, list[int]]) -> list[int]:
    h_totales: dict[int, int] = {}
    h_max: int = 0
    res: list[int] = []

    for empleado in horas.items():
        empleado_id: int = empleado[0]
        empleado_horas: list[int] = empleado[1]
        h_totales[empleado_id] = 0

        for h in empleado_horas:
            h_totales[empleado_id] += h

        if h_totales[empleado_id] > h_max:
            h_max = h_totales[empleado_id]

    for empleado in h_totales.items():
        empleado_id = empleado[0]
        empleado_total: int = empleado[1]

        if empleado_total == h_max:
            res.append(empleado_id)


    return res

# t_total = 45' + 8' + 9' + 22' = 1h 24'
