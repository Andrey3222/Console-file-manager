from insde_function import ins_fun, ins_fil, ins_sort
import math
import os

def test_ins_fun():
    assert ins_fun() == [1.6, 10.4, 6.4, 10.08]

def test_ins_fil():
    assert ins_fil() == ['мак', 'мак', 'мак', 'мак', 'мак']

def test_ins_sort():
    assert ins_sort() == ['red', 'blue', 'green', 'orange']



def test_mkdir():
    os.mkdir('folder_mk')
    assert 'folder_mk' in os.listdir()
    os.rmdir('folder_mk')

def test_pi():
    assert 2 * round(math.pi, 2) == 6.28

def test_pow():
    assert math.pow(3, 2) == 9

def test_hypot():
    assert math.hypot(4, 2) == 4.47213595499958





