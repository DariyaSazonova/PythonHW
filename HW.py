# Задача 2: Найдите сумму цифр трехзначного числа. 

# i = int(input('Введите трехзначное число: '))
# if(99 < i < 1000):
#     count = 0
#     while (i > 0):
#         a = i % 10
#         count = count + a
#         i = i // 10
#     print (f'Сумма равна {count}')
# else: 
#     print('Вы ввели не трехзначное число!')


   
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# S = int(input("Введите общее количество журавликов: "))
# if not S % 6:
#      x = S // 6
#      print(f'Катя {x * 4} ')
#      print(f'Сережа {x} ')
#      print(f'Петя {x}')
# else:
#     print(f'Вы ввели число, не кратное 6!')



#  Задача 6: Вы пользуетесь общественным транспортом? Вероятно, 
#  вы расплачивались за проезд и получали билет с номером. Счастливым 
#  билетом называют такой билет с шестизначным номером, 
#  где сумма первых трех цифр равна сумме последних трех. 
#  Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
#  Вам требуется написать программу, которая проверяет счастливость билета.
#  *Пример:*
#  385916 -> yes
#  123456 -> no

# n = (input('Введите шестизначный номер билета:  '))
# if (len (n) == 6):
#     s1 = (int(n[0]) + int((n[1])) + int(n[2]))
#     s2 = (int(n[3]) + int((n[4])) + int(n[5]))
#     if s1 == s2:
#         print('Yes')
#     else:
#         print('No')
# else: 
#     print("Введен некорректный номер билета, попробуйте еще раз!")


# Задача 8
# Требуется определить, можно ли от шоколадки 
# размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

# n = int(input("Введите один размер шоколадки в дольках: "))
# m = int(input("Введите другой размер шоколадки в дольках: "))

# k = int(input("Введите количество долек, которое хотите отломить: "))

# if k < m * n and (k % m == 0 or k % n == 0):
#     print('Да')
# else:
#     print('Нет')