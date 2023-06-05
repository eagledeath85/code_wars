# answer = [
#             { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java',
#             'greeting': 'Hi Sofia, what do you like the most about Java?'
#             },
#             { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python',
#             'greeting': 'Hi Lukas, what do you like the most about Python?'
#             },
#             { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby',
#             'greeting': 'Hi Madison, what do you like the most about Ruby?'
#             }
#         ]


def greet_developers(lst):
    lst_tuple = tuple(lst)
    result_list = []
    for item in lst_tuple:
        value = f"Hi {item['firstName']}, what do you like the most about {item['language']}?"
        new_dict = {'greeting': value}
        item.update(new_dict)
        result_list.append(item)
    return result_list






list1 = [
        {'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35,
         'language': 'Java'},
        {'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35,
         'language': 'Python'},
        {'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32,
         'language': 'Ruby'}
    ]

greet_developers(list1)