

def duplicates(arr: list) -> list:
# Takes an array as input
# Go through the array and check any duplicates in it
# Put the duplicates values in a list
    duplicates = []
    seen = set()
    for item in arr:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.add(item)
    return list(duplicates)




# list_test = [1, 2, 4, 4, 3, 3, 1, 5, 3, '5', '3', '1', '5']
# list_test = []
list_test = ['zut', 'alors', 1, 2, 4, 4, 3, 3, '1', 5, 3, 'zut']
result = duplicates(list_test)
print(result)