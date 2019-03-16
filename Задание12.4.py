class Hexagon():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6
        print('Создан шестиугольник!')
    def calculate_perimetr(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6
hx = Hexagon(10, 55, 34, 34, 24, 42)
print(hx.calculate_perimetr())
    
