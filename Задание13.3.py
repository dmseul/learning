class Shape():
    def what_am_i(self):
        print('Я - фигура')
        
class Rectangle(Shape):
    def __init__(self, l, w):
        self.lenght = l
        self.width = w
        
    def calculate_perimeter(self):
        return (2 * self.lenght) + (2 * self.width)
    
class Square(Shape):
    def __init__(self,s):
        self.side = s
        
    def calculate_perimeter(self):
        return 4 * self.side
    
a1 = Square(10)
a2 = Rectangle(10, 20)

a1.what_am_i()
a2.what_am_i()
