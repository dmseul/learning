from random import shuffle

class Card:
    suits = ['пики',
             'черви',
             'буби',
             'крести']
    
    values = [None, None, '2', '3',
              '4', '5', '6', '7',
              '8', '9', '10',
              'валет', 'дама',
              'король', 'туз']
    
    def __init__(self, v, s):
        self.value = v
        self.suit = s
        
    def __It__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
            return False
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
            return False

    def __repr__(self):
        return self.values[self.value] + " " + self.suits[self.suit]

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_cards(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
    
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def  __init__(self):
        name1 = input('Введите имя первого игрока: \n')
        name2 = input('\nВведите имя второго игрока: \n')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        
    def wins(self, winner):
        w = '\n{} забирает карты'
        w = w.format(winner)
        print('\n', w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = '\n{} кладёт {}, {} кладёт {}'
        d = d.format(p1n, p1c, p2n, p2c)
        print('\n', d)

    def play_game(self):
        cards = self.deck.cards
        print('\n Поехали!')
        while len(cards) >= 2:
            m = '\nНажмите Х для выхода. \nНажмите любую клавишу, чтобы продолжить.'
            response = input(m)
            if m == 'Х':
                break
            p1c = self.deck.rm_cards()
            p2c = self.deck.rm_cards()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win = self.winner(self.p1, self.p2)
        print('\nИгра окончена. \nПобедил {}!'.format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return 'дружба'
game = Game()
game.play_game()

        



    
                
        
