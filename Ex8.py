# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку 
# на два прямоугольника).

size1 = int(input('Введите количество долек на первой стороне: '))
size2 = int(input('Введите количество долек на второй стороне: '))
result = int(input('Сколько долек Вы хотите съесть? N= '))
if result%size1 == 0 or result%size2 ==0:
    print('Получилось отломить. Приятного аппетита!')
else:
    print('Ой, ошибка. Нужен новый шоколад...')