from statistics import mean


list1 = [
    { 'firstName': 'Maria', 'lastName': 'Y.', 'country': 'Cyprus', 'continent': 'Europe', 'age': 37, 'language': 'Java' },
    { 'firstName': 'Victoria', 'lastName': 'T.', 'country': 'Puerto Rico', 'continent': 'Americas', 'age': 70, 'language': 'Python' },
]

list2 = [
    { 'firstName': 'Noa', 'lastName': 'A.', 'country': 'Israel', 'continent': 'Asia', 'age': 20, 'language': 'Ruby' },
    { 'firstName': 'Andrei', 'lastName': 'E.', 'country': 'Romania', 'continent': 'Europe', 'age': 21, 'language': 'C' },
]


age_list = []
for person in list1:
    age_list.append(person['age'])
average_age = round(mean(age_list))
print(average_age)