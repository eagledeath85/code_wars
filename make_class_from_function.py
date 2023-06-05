def make_class(*args):
    class Animal:
        def __init__(self, *values):
            self.__dict__ = {x:y for x, y in zip(args, values)}
    return Animal


Animel = make_class("name", "species", "age", "health", "weight", "color")
print()

dog1 = Animel("Bob", "Dog", 5, "good", "50lb", "brown")
dog2 = Animel("Bob", "Dog", 5, "good", "50lb", "brown")

print(dog1.name)