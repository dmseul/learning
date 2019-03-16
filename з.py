class Horse():
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
class Rider():
    def __init__(self, name):
        self.name = name
r1 = Rider('Dima')
h1 = Horse('Mick', r1)
print(h1.owner.name)
