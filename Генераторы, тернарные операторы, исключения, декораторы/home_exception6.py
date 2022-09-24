
import random

sum_num = 0
num = 0
try:
    while sum_num < 777:
        num = int(input('Введите число: '))

        out_back = random.randint(1, 13)
        if out_back == 1:

            exception = [ValueError(), ZeroDivisionError() ]

        sum_num += num
        with open('sum_file.txt', 'a') as file1:
            file1.write(str(num) + '\n')

except (ValueError, ZeroDivisionError ) as err:
    print('Вас постигла неудача!')


else:
    print(f'Вы успешно выполнили условие для выхода из порочного цикла! {sum_num}')
