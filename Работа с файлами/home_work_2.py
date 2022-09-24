import os
FILE_NAME = 'orders.txt'
orders = []
if os.path.exists(FILE_NAME):
   with open(FILE_NAME, 'r', encoding='utf-8') as f:
        for order in f:
            orders.append(order.replace('\n',''))

bill_sum = 0

FILE_SUM = 'bill_sum.txt'
orders_bill = []
if os.path.exists(FILE_SUM):
  with open(FILE_SUM, 'r', encoding='utf-8') as f:
    for order in f:
      orders_bill.append(order.replace('\n',''))


while True:
    print('0. Пополнить счет: ')
    print('1. Добавить покупку: ')
    print('2. История покупок: ')
    print('3. Выход')
    choice = input('Введите номер: ')
    if choice =='0':
      cost = int(input('Введите сумму: '))
      bill_sum += cost
      with open(FILE_SUM, 'w', encoding='utf-8') as f:
        f.write(f'Счет: {bill_sum}\n')
    if choice == '1':
        name = input('Введите название: ')
        orders.append(name)
    elif choice == '2':
        for order in orders:
            print(order)
    elif choice  == '3':
         with open(FILE_NAME, 'w', encoding='utf-8') as f:
             for order in orders:
                 f.write(f'{order}\n')
         break
    else:
        print('Неправильно введены данные')