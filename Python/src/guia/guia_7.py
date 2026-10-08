# Ej 1
def pertenece(num: int, num_list: list[int]) -> bool:
    for i in num_list:
        if i == num:
            return True
    return False


def pertenece2(num: int, num_list: list[int]) -> bool:
    if num_list == []:
        return False
    if num == num_list[0]:
        return True
    return pertenece2(num, num_list[1:])


def pertenece3(num: int, num_list: list[int]) -> bool:
    return num in num_list


# Ej 2
def divide_a_todos(num: int, num_list: list[int]) -> bool:
    for i in num_list:
        if i % num != 0:
            return False
    return True


# Ej 3
