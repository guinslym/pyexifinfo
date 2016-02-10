PyExifInfo
===================


Yet Another python wrapper for Phil Harvey' Exiftool
ExifTool is the corner stone library to look for when you need to extract Exif or other types of metadata whithin a picture.
ExifTool est la package de référence quand il s'agit d'analyser l'Exif ou les métadonnées d'une photo

https://github.com/guinslym/pyexifinfo

Installation
------------
To install pyexifinfo, simply:

.. code:: sh

    $ pip install pyexifinfo

Usage
-----

.. code:: python
import pyexifinfo as p

p.ver() #retrieve your ExifTool version
filename = 'python-logo.png'
p.get_json(filename) #retrieve a json representation of this file exif
=>
[{u'File:FilePermissions': u'rw-rw-r--', u'PNG:Interlace': u'Noninterlaced', u'S
ourceFile': u'/home/laptop/python-logo.png', u'PNG:ColorType': u'RGB with Alpha', u'File:MIMEType': u'image/png',u'File:FileAccessDate': u'2015:07:20 16:37:22-04:00', u'File:FileModifyDate': u'2014:12:12 20:55:59-05:00', u'File:FileSize': u'9.9 kB', u'PNG:ImageWidth': 290, u'File:FileType': u'PNG', u'File:FileName': u'python-logo.png', u'PNG:Compression': u'Deflate/Inflate', u'PNG:PixelsPerUnitY': 2835, u'PNG:PixelsPerUnitX': 2835, u'PNG:ImageHeight': 82, u'PNG:PixelUnits': u'Meters', u'File:Directory': u'/home/laptop', u'File:FileInodeChangDate': u'2015:07:20 16:37:22-04:00', u'PNG:Filter': u'Adaptive', u'PNG:BitDepth': 8, u'Composite:ImageSize': u'290x82', u'ExifTool:ExifToolVersion': 9.46}]


Other useful functions
-----

.. code:: python
from pyexifinfo get_csv, get_xml, fileType, mimeType, imageSize, imageWidth, imageHeight
filename = 'python-logo.png'

result = get_csv(filename)
result = get_xml(filename)
result = fileType(filename)
result = mimeType(filename)



