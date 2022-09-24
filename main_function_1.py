def victorina():
    import random
    FAMOUS_PEOPLE = {'Александр Сергеевич Пушкин': '26.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814',
                     'Сергей Александрович Есенин': '03.10.1895',
                     'Владимир Семенович Высоцкий': '25.01.1938', 'Виктор Робертович Цой': '21.06.1962',
                     'Константин Эдуардович Циолковский': '17.09.1857',
                     'Сергей Павлович Королев': '12.01.1907', 'Валентин Петрович Глушко': '20.08.1908',
                     'Андрей Николаевич Туполев': '29.10.1888',
                     'Юрий Алексеевич Гагарин': '09.03.1934'

                     }
    rounds = int(input('Сколько раз вы хотите играть? '))

    for i in range(rounds):
        name, data = random.choice(list(FAMOUS_PEOPLE.items()))
        answer = input(f'Когда родился - {name} ')

        if answer == data:
            print('Верно ')
        else:
            print('Неверно ')

    print('Пока!')

def my_account():
  bill_sum = 0
  history = []

  while True:
      print('1. пополнение счета: ')
      print('2. покупка: ')
      print('3. история покупок: ')
      print('4. выход: ')
      print(f'Ваш счет - {bill_sum}')

      choice = input('Выберите пункт меню: ')
      if choice == '1':
        cost = int(input('Введите сумму: '))
        bill_sum += cost
      elif choice == '2':
          cost = int(input('Введите сумму покупки: '))
          if cost > bill_sum:
              print('Недостаточно средств')
          else:
              bill_sum -= cost
              name = input('Введите название покупки: ')
              history.append((name, cost))
      elif choice == '3':
          print(history)
      elif choice == '4':
          break
      else:
          print('Неверный пункт меню')