"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def theorem_proof(n, sum=0, formula=-1):
    if sum == formula:
        return print('Равенство верное')
    else:
        sum += n
        return theorem_proof(n, sum+1, (n * (n + 1) / 2))


print('Првоерка равенства 1+2+...+n = n(n+1)/2')
try:
    use_number = int(input('Введите целое положительное число n: '))
    if use_number > 0:
        theorem_proof(use_number)
    else:
        print('Введено некорректное значение, завершение программы')
except ValueError:
    print('Введено некорректное значение, завершение программы')
