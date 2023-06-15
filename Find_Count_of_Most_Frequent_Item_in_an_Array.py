from collections import Counter


def most_frequent_item_count(collection):
    counter = Counter(collection)
    result = max(counter.items(), key=lambda x: x[1])
    return result[1]


input_array = [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
result = most_frequent_item_count(input_array)
print(result)