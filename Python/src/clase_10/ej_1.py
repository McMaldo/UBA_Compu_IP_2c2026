"""
funcion cuenta_regresiva_y_es_par()
"""

def cuenta_regresiva_y_es_par(num: int) -> bool:

    es_par: bool = num % 2 == 0

    if not(es_par):
        num -= 1

    for i in range(num, 0, -2):
        print(i)

    print("despegue")

    return es_par;
