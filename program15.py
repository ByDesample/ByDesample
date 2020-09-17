def AddTuple(add_tuple: list) -> list:
    try_list = list()
    for i in add_tuple:
        try_list.append((i, i**3))
    return try_list


cihat = [2, 1, 3, 5]

print(AddTuple(cihat))
