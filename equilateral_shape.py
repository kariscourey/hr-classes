# class EquilateralShape:
#     # A class with no state or behavior
#     pass

# Return the result of multiplying the number of sides with the length of the side.

import math


class EquilateralShape:
    def __init__(self, num_sides, side_length): # self = param python provides automatically in every method of a class; holds the first instance of the class
        self.num_sides = num_sides
        self.side_length = side_length

    def calculate_perimeter(self):
        return self.num_sides * self.side_length

    def calculate_area(self):
        raise ValueError

        # side_squared = pow(self.side_length, 2)

        # # improve long if-elif-else with inheritance
        # if self.num_sides == 3:
        #     return math.sqrt(3) / 4 * side_squared
        # elif self.num_sides == 4:
        #     return side_squared
        # elif self.num_sides == 5:
        #     weird_value = math.sqrt(25 + 10 * math.sqrt(5))
        #     return weird_value / 4 * side_squared
        # elif self.num_sides == 6:
        #     return (3 * math.sqrt(3)) / 2 * side_squared
        # else:
        #     raise ValueError


class EquilateralTriangle(EquilateralShape):
    def __init__(self, side_length):
        super().__init__(3, side_length)

    def calculate_area(self):
        side_squared = pow(self.side_length, 2)
        return math.sqrt(3) / 4 * side_squared


class Square(EquilateralShape):
    def __init__(self, side_length):
        super().__init__(4, side_length)

    def calculate_area(self):
        return pow(self.side_length, 2)


class EquilateralPentagon(EquilateralShape):
    def __init__(self, side_length):
        super().__init__(5, side_length)

    def calculate_area(self):
        side_squared = pow(self.side_length, 2)
        weird_value = math.sqrt(25 + 10 * math.sqrt(5))
        return weird_value / 4 * side_squared


class EquilateralHexagon(EquilateralShape):
    def __init__(self, side_length):
        super().__init__(6, side_length)

    def calculate_area(self):
        side_squared = pow(self.side_length, 2)
        return (3 * math.sqrt(3)) / 2 * side_squared



triangle1 = EquilateralShape(3, 1) # using name of class on RHS calls __init__ method of class
triangle2 = EquilateralShape(3, 100)
square = EquilateralShape(3, 1)

print(triangle1.num_sides)    # Prints 3
print(triangle1.side_length)  # Prints 1

print(triangle2.num_sides)    # Prints 3
print(triangle2.side_length)  # Prints 100

print(square.num_sides)       # Prints 4
print(square.side_length)     # Prints 1



triangle = EquilateralTriangle(2)
print(triangle.num_sides)    # Prints 3
print(triangle.side_length)  # Prints 2

print(triangle.calculate_perimeter())
# Prints 6

print(triangle.calculate_area())
# Prints 1.7320508075688772


# We now use this
square = Square(3)

# We do not use this, anymore
# square = EquilateralShape(4, 3)


# Inside the __init__ method, for every instance that the EquilateralShape class initializes, it takes the value of the num_sides parameter and sets it as a property on that instance named num_sides.
