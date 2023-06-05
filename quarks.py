# q1.interact(q2)
#   -> q1.color = q2.color
#   -> q2.color = q1.color

class Quark:

    baryon_number = 1 / 3

    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def get_color(self):
        return self.color

    def get_flavor(self):
        return self.flavor

    def set_color(self, color):
        self.color = color
        return self.color

    def interact(self, q):
        self.color, q.color = q.color, self.color


q1 = Quark("red", "up")
print(f"q1 colour is: {q1.color}")

q2 = Quark("blue", "strange")
print(f"q2 colour is: {q2.color}")

q1.interact(q2)
print(f"q1 new color is: {q1.color} and q2 new color is: {q2.color}")