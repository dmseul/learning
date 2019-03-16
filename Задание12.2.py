import math
class Circle():
    def __init__(self, r):
        self.radius = r
        print('Создано!')
    def area(self):
        return math.pi * (self.radius ** 2)
cr1 = Circle(10)
print(cr1.area())
