from pyexifinfo import *
import pyexifinfo as p
import os

# content of test_sample.py
image = 'python-logo-master-v3-TM.png'
def test_version_is_greater_than_8():
    """ test the version is greater than 8 """
    a = p.ver()
    #transforming bytes to string
    a = a[0].decode('utf-8')
    #transform string to float
    a = float(a)
    assert a >= 8

def test_get_json():
    a = p.get_json(image)
    print('hello')
    assert len("sss") == 3
