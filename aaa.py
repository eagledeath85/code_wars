class AbstractAnimal:
    @staticmethod
    def sleep():
        print("ZzzZzz")

    def animal_sound(self):
        raise NotImplementedError

    def wake_up(self):
        self.animal_sound()
        print("I am awake!")


class Lion(AbstractAnimal):
    def __init__(self):
        pass

    def animal_sound(self):
        print("Roar!")

lion = Lion()
lion.animal_sound()