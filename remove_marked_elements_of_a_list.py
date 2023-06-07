# [1, 1, 2, 3, 1, 2, 3, 4], [1, 3] -> [2, 2, 4]


def remove_elements(lst1: list, lst2: list) -> list:
    # output = []
    # for element in lst1:
    #     if element not in lst2:
    #         output.append(element)
    output = [element for element in lst1 if element not in lst2]
    return output


print(remove_elements([1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8], [1, 3, 4, 2]))