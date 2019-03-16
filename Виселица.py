def vis(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    letter = list(word)
    board = ['_'] * len(word)
    win = False
    print('Добро пожаловать на казнь!')
    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Введите букву: '
        quess = input(msg)
        if quess in letter:
            cind = letter.index(quess)
            board[cind] = quess
            letter[cind] = '$'
        else:
            wrong += 1
        print(''.join(board))
        a = wrong + 1
        print('\n'.join(stages[0:a]))
        if '_' not in board:
            print('Вы выиграли! Было загадано слово: ')
            print(' '.join(board))
            win = True
            break
    if not win:
         print('\n'.join(stages[0: wrong]))
         print('Вы проиграли! Было загадано слово: {}'.format(word))
vis('номер')

