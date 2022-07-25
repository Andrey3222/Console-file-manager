def ins_fun():

    distance_mile = [1.0, 6.5, 4.0, 6.3]
    kilometr_distance = list(map(lambda x: x * 1.6, distance_mile))
    return kilometr_distance

if __name__ == '__main__':
   print(ins_fun())

def ins_fil():
  mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
  zolushka = list(filter(lambda x: x == 'мак', mixed))
  return zolushka
if __name__ =='__main__':
   print(ins_fil())

def ins_sort():
    l1 = ['blue', 'green', 'red', 'orange']
    return (sorted(l1, key=len))

if __name__ =='__main__':
    print(ins_sort())


