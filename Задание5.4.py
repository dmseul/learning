me = {'любимый урок':'Алгебра',
               'рост': '175'}
x = input('Что вы хотите узнать о себе? ')
if x in me:
    x = me[x]
    print(x)
else:
    print('Такого нет в моей базе данных')
