class Triangle():
    def __init__(self, h, bl):
        self.height = h
        self.baselenght = bl
        print('Обьект создан!')
    def area(self):
        return (self.height * self.baselenght) / 2
tri = Triangle(10,20)
print(tri.area())
