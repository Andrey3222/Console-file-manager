def list_dir():
  import os
  print('Список файлов в текущей дериктории:', os.listdir(path="."))# список файлов и директорий в папке.

def list_file():
  import os
  rootdir = os.getcwd()

  for subdir, dirs, files in os.walk(rootdir):
      for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".py"):
               print (filepath)

def list_fol():
    import os
    for something in os.listdir():
        if os.path.isdir(something):
           print('Вывод только папок',something)

def create():
  import os
  for i in range(2):
    if not os.path.exists(f'new{i}'):# Создать папку передаем путь проверяем на существование
      os.mkdir(f'new{i}')


def delete():
    import os
    for i in range(2):# Удалить созданную папку
        # Удалить папку
        os.rmdir(f'new{i}')


def cop_y():
    import shutil # Скопировать файл
    shutil.copy('main_function.py', 'new 33.py')
