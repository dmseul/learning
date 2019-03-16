class Square():
    def __init__(self, s):
        self.side = s
    def __repr__(self):
        return('{} на {} на {} на {}'.format(self.side, self.side, self.side, self.side))
a1 = Square(10)
print(a1)
