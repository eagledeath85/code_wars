



def count_languages(lst):
    language_dict = {}
    for person in lst:
        language = person['language']
        if language in language_dict:
            language_dict[language] += 1
        else:
            language_dict[language] = 1
    return language_dict



list1 = [
            { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C' },
            { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
            { 'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
            { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
            ]


count_languages(list1)


# Answer: answer = { 'C': 2, 'JavaScript': 1, 'Ruby': 1 }

