def Cube(example_list: list) -> list:
    try_list = list()
    for i in example_list:
        try_list.append((i, i**3))
    try_list.sort()
    return try_list


example_list = [5, 2, 3, 7, 9, 1]
sorted_tuples = Cube(example_list)
print(sorted_tuples)
