import os

file = ' '
with os.scandir(path='.') as f:
    for entry in f:
        if not entry.name.startswith('.') and entry.is_file():
               file += entry.name + ', '

# a = print('files:'+file)
with open('listdir.txt', 'w', encoding='utf-8') as f:
    f.write(f'file:{file}\n')



p = ' '
for something in os.listdir():

    if os.path.isdir(something):
       p+=(something+',')

# b = print('dirs:'+p)


with open('listdir.txt', 'a', encoding='utf-8') as f:
    f.write(f'dirs: '+p)