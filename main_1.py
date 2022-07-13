import platform
from main_function import victorina, my_account
from auxiliary_function import create, delete, cop_y, list_fol, list_file, list_dir

n = ' '
while n != 'выход':
    print('Выберите меню:\n 1 -Создать папку ,2 - Удалить папку,3 - Копировать папку,'
          '\n 4 - посмотреть папки, 5 - посмотреть файлы, 6 - посмотреть данные ОС,'
          '\n 7 - играть в викторину, 8 - мой банковский счет, 9 - посмотреть файлы в текущей директории,'
          '\n 10 - выход ')
    n = int(input('Введите понравившееся: '))
    if n == 1:
        print('Вновь созданные папки ')
        create()
    if n == 2:
        print('Удалить созданные папки')
        delete()

    if n == 3:
        print('Копирование файлов')
        cop_y()
    if n == 4:
       list_fol()
    if n == 5:
        list_file()
    if n == 6:
        print('Ваша платформа:', platform.system())

    if n == 7:
        victorina()
    if n == 8:
        my_account()
    if n == 9:
       list_dir()
    if n == 10:
        break

