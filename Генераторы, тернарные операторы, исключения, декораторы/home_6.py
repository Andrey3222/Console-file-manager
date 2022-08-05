'''
Тернарные операторы
'''
import random

a = 12
b = 5

res = a + 2 if a > b else b-3
print(res,'\n')


s = 'python'
t = 'upper'

res_t = s.upper() if t == 'upper' else s
print(res_t,'\n')

'''
Генераторы
'''
a = [0 for i in range(7)]
print(a,'\n')

b = [2 for i in range(10)]
print(b,'\n')

c = [ord(i) for i in 'abcd']
print(c,'\n')

d = [random.randint(-10, 10) for i in range(10)]
print(d,'\n')

e = [ elem for elem in d if elem > 0]
print(e,'\n')

f = [elem for elem in d if elem % 2 ==0]
print(f)

g = input('Введите число через пробел: ').split()
g = [int(i) for i in g]
print(g)

n = 3
m = 6
w = [[1] * m for i in range(n)]
w[1][3] = 100
for i in w:
    print(i)

a = [(i, j) for i in 'abc' for j in [2, 3, 4]]
print(a)

a = [i * j for i in [2, 3, 4, 5] for j in [5, 4, 6] if  i*j > 10]
print(a)

