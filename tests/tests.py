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
    a = p.get_json("tests/"+image)
    assert len(a[0]) == 25

def test_get_fileType():
    a = p.fileType("tests/"+image)
    assert a.lower() == 'png'

def test_get_mimeType():
    a = p.mimeType("tests/"+image)
    assert a.lower() == 'image/png'

def test_get_imageSize():
    a = p.imageSize("tests/"+image)
    assert a.lower() == '601x203'

def test_get_imageWidh():
    a = p.imageWidth("tests/"+image)
    assert a == 601

def test_get_imageHeight():
    a = p.imageHeight("tests/"+image)
    assert a == 203