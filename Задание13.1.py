class Rectangle():
    def __init__(self, l, w):
        self.lenght = l
        self.width = w
    def calculate_perimeter(self):
        return (2 * self.lenght) + (2 * self.width)
class Square():
    def __init__(self,s):
        self.side = s
    def calculate_perimeter(self):
        return 4 * self.side
ra = Rectangle(10, 20)
sq = Square(10)
print(ra.calculate_perimeter())
print(sq.calculate_perimeter())
