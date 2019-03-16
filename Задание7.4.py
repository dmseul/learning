qs = ['a', 'b?', 'c?']
n = 0
while True:
    a = input('Угадай букву или нажми Х для выхода.\n')
    if a == 'X':
        a = 'Х'
    if a == 'Х':
          break
    if a in qs:
        print('Угадал!')
    else:
        print('Не угадал!')
    
    
