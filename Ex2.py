# Задача 2: Найдите сумму цифр трехзначного числа.
number = input('Введите трехзначное число: ')
if int(number)>=100 and int(number)<=999:
    summa = int(number[0]) + int(number[1]) + int(number[2])
    print(summa)
else:
    print('Прочтите условие задачи и введите корректное число.')
