

def order_food(lst):
    food_dict = {}
    for person in lst:
        food_type = person['meal']
        if person['meal'] in food_dict:
            food_dict[person['meal']] += 1
        else:
            food_dict[person['meal']] = 1
    return food_dict


list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard' },
    { 'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian' },
]

# answer = { 'vegetarian': 2, 'standard': 1, 'vegan': 1 }
answer = order_food(list1)
print(answer)