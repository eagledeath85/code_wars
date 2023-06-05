import json

def count_developers(lst):
    lst_tuple = tuple(lst)
    new_data = ({item['continent']: item['language']} for item in lst_tuple)
    new_data_tuple = tuple(new_data)
    given_dict = {'Europe': 'JavaScript'}
    count = 0
    for item in new_data_tuple:
        if item == given_dict:
            count += 1
    return count


lst1 = [
    {'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19,
     'language': 'JavaScript'},
    {'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28,
     'language': 'JavaScript'},
    {'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML'},
    {'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30,
     'language': 'CSS'},
    {'firstName': 'Noah', 'lastName': 'S.', 'country': 'Belgium', 'continent': 'Europe', 'age': 34,
     'language': 'JavaScript'}
]

print(count_developers(lst1))

