

class Person:
    def __init__(self, person_name):
        self.person_name = person_name

    def greet(self, other_name):
        print(f"Hello {other_name}, my name is {self.person_name}")


jack = Person("Jack")
jill = Person("Jill")

jack.greet("Jill")
jack.greet("Mary")
jill.greet("Jack")