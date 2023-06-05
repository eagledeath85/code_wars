import math


class Block:
    def __init__(self, my_list):
        self.my_list = my_list

    def get_width(self):
        return self.my_list[0]

    def get_length(self):
        return self.my_list[1]

    def get_height(self):
        return self.my_list[2]

    def get_volume(self):
        return math.prod(self.my_list)

    def get_surface_area(self):
        square_total_area = 2 * self.my_list[0] * self.my_list[1]
        rectangle_total_area = 4 * self.my_list[1] * self.my_list[2]
        total_area = square_total_area + rectangle_total_area
        return total_area


block1 = Block([2,2,2])
print(block1.get_volume())
print(block1.get_surface_area())