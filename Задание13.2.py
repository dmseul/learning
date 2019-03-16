class Square():
    def __init__(self, s):
        self.side = s
    def calc_pr(self):
        return 4 * self.side
    def change_size(self, a):
        self.side = self.side + a
s1 = Square(1)
print(s1.calc_pr())
s1.change_size(1)
print(s1.calc_pr())

    
