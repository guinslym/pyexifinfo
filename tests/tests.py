import pyexifinfo as p
import csv

#tested with Pytest
#
#
# python logo (MIT)
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

def test_get_csv():
    a = p.get_csv("tests/"+image)
    assert a[0:10] == "SourceFile"

def test_get_xml():
    a = p.get_xml("tests/"+image)
    assert a[0:5] == "<?xml"

def test_get_fileType():
    a = p.fileType("tests/"+image)
    assert a.lower() == 'png'

def test_get_mimeType():
    a = p.mimeType("tests/"+image)
    assert a.lower() == 'image/png'

