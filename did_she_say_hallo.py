def did_she_say_hallo(sentence: str) -> bool:
    possible_languages = ('hello', 'cia', 'salut', 'hallo', 'hola', 'ahoj', 'czesc')
    for word in possible_languages:
        if word in sentence.casefold():
            return True
    return False

print(did_she_say_hallo('meh hola'))
