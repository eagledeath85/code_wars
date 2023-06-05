



def find_admin(lst, lang):
    github_admin = []
    for person in lst:
        if person['language'] == lang and person['githubAdmin'] == 'yes':
            github_admin.append(person)
    return github_admin





list1 = [
    { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
    { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 49, 'language': 'Ruby', 'githubAdmin': 'no' },
    { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' },
    { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript', 'githubAdmin': 'no' }
]

# answer1 = [
#     { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
#     { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' }
# ]

answer1 = find_admin(list1, 'JavaScript')
print(answer1)
