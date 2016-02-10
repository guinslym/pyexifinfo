PyExifInfo
======================================================

Yet Another python wrapper for Phil Harvey' Exiftool
ExifTool is the corner stone library to look for when you need to extract Exif or other types of metadata whithin a picture or many other files type.

(French) ExifTool est la package de référence quand il s'agit d'analyser l'Exif ou les métadonnées d'une photo

##Installation
		[sudo] pip install -U pyexifinfo
		#sudo is optionnal

###Requirements
[ExifTool](http://www.sno.phy.queensu.ca/~phil/exiftool/) by Phil Harvey. Read, Write and Edit Image Metadata Information!

##Usage

```python
import pyexifinfo as p

p.ver() #retrieve your ExifTool version
filename = 'python-logo.png'
p.get_json(filename) #retrieve a json representation of this file exif
=>
[{u'File:FilePermissions': u'rw-rw-r--', u'PNG:Interlace': u'Noninterlaced', u'S
ourceFile': u'/home/laptop/python-logo.png', u'PNG:ColorType': u'RGB with Alpha', u'File:MIMEType': u'image/png',u'File:FileAccessDate': u'2015:07:20 16:37:22-04:00', u'File:FileModifyDate': u'2014:12:12 20:55:59-05:00', u'File:FileSize': u'9.9 kB', u'PNG:ImageWidth': 290, u'File:FileType': u'PNG', u'File:FileName': u'python-logo.png', u'PNG:Compression': u'Deflate/Inflate', u'PNG:PixelsPerUnitY': 2835, u'PNG:PixelsPerUnitX': 2835, u'PNG:ImageHeight': 82, u'PNG:PixelUnits': u'Meters', u'File:Directory': u'/home/laptop', u'File:FileInodeChangDate': u'2015:07:20 16:37:22-04:00', u'PNG:Filter': u'Adaptive', u'PNG:BitDepth': 8, u'Composite:ImageSize': u'290x82', u'ExifTool:ExifToolVersion': 9.46}]
```
####or with style
```json
import pyexifinfo as p
import json

data = p.get_json(filename)
print( json.dumps(data, sort_keys=True,
                  indent=4, separators=(',', ': ')) )

[
    {
        "Composite:ImageSize": "601x203",
        "ExifTool:ExifToolVersion": 9.46,
        "File:Directory": "/home/laptop/Documents/",
        "File:FileAccessDate": "2016:02:10 00:28:11-05:00",
        "File:FileInodeChangeDate": "2016:02:10 00:27:30-05:00",
        "File:FileModifyDate": "2016:02:10 00:27:30-05:00",
        "File:FileName": "python-logo.png",
        "File:FilePermissions": "rw-rw-r--",
        "File:FileSize": "82 kB",
        "File:FileType": "PNG",
        "File:MIMEType": "image/png",
        "PNG:BitDepth": 8,
        "PNG:ColorType": "RGB with Alpha",
        "PNG:Compression": "Deflate/Inflate",
        "PNG:CreationTime": "06/05/04",
        "PNG:Filter": "Adaptive",
        "PNG:ImageHeight": 203,
        "PNG:ImageWidth": 601,
        "PNG:Interlace": "Noninterlaced",
        "PNG:PixelUnits": "Meters",
        "PNG:PixelsPerUnitX": 2800,
        "PNG:PixelsPerUnitY": 2800,
        "PNG:SignificantBits": "8 8 8 8",
        "PNG:Software": "Macromedia Fireworks MX 2004",
        "SourceFile": "/home/laptop/Documents/python-logo.png"
    }
]
```

####With XML (rdf)
```xml	
data = p.get_xml(filename)
print(data)
=>

<?xml version='1.0' encoding='UTF-8'?>
<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>

<rdf:Description rdf:about='/home/laptop/Documents/python-logo.png'
  xmlns:et='http://ns.exiftool.ca/1.0/' et:toolkit='Image::ExifTool 9.46'
  xmlns:ExifTool='http://ns.exiftool.ca/ExifTool/1.0/'
  xmlns:System='http://ns.exiftool.ca/File/System/1.0/'
  xmlns:File='http://ns.exiftool.ca/File/1.0/'
  xmlns:PNG='http://ns.exiftool.ca/PNG/PNG/1.0/'
  xmlns:Composite='http://ns.exiftool.ca/Composite/1.0/'>
 <ExifTool:ExifToolVersion>9.46</ExifTool:ExifToolVersion>
 <System:Directory>/home/guinsly/totrash/pyexif/pyexifinfo/pyexifinfo</System:Directory>
 <System:FileAccessDate>2016:02:10 00:28:11-05:00</System:FileAccessDate>
 <System:FileInodeChangeDate>2016:02:10 00:27:30-05:00</System:FileInodeChangeDate>
 <System:FileModifyDate>2016:02:10 00:27:30-05:00</System:FileModifyDate>
 <System:FileName>python-logo.png</System:FileName>
 <System:FilePermissions>rw-rw-r--</System:FilePermissions>
 <System:FileSize>82 kB</System:FileSize>
 <File:FileType>PNG</File:FileType>
 <File:MIMEType>image/png</File:MIMEType>
 <PNG:BitDepth>8</PNG:BitDepth>
 <PNG:ColorType>RGB with Alpha</PNG:ColorType>
 <PNG:Compression>Deflate/Inflate</PNG:Compression>
 <PNG:CreationTime>06/05/04</PNG:CreationTime>
 <PNG:Filter>Adaptive</PNG:Filter>
 <PNG:ImageHeight>203</PNG:ImageHeight>
 <PNG:ImageWidth>601</PNG:ImageWidth>
 <PNG:Interlace>Noninterlaced</PNG:Interlace>
 <PNG:PixelUnits>Meters</PNG:PixelUnits>
 <PNG:PixelsPerUnitX>2800</PNG:PixelsPerUnitX>
 <PNG:PixelsPerUnitY>2800</PNG:PixelsPerUnitY>
 <PNG:SignificantBits>8 8 8 8</PNG:SignificantBits>
 <PNG:Software>Macromedia Fireworks MX 2004</PNG:Software>
 <Composite:ImageSize>601x203</Composite:ImageSize>
</rdf:Description>
</rdf:RDF>


```

#####functions

```python
from pyexifinfo get_json
from pyexifinfo get_csv
from pyexifinfo get_xml
from pyexifinfo fileType
from pyexifinfo mimeType

filename = 'python-logo.png'

result = get_json(filename)
result = get_csv(filename)
result = get_xml(filename)
result = fileType(filename)
result = mimeType(filename)
```

###Supported fileType (read only)
```
  File Types
  ------------+-------------+-------------+-------------+------------
  3FR   | DVB   | KEY   | ORF   | RWL   
  3G2   | DYLIB | LA    | OTF   | RWZ   
  3GP   | EIP   | LFP   | PAC   | RM    
  AA    | EPS   | LNK   | PAGES | SEQ   
  AAX   | EPUB  | M2TS  | PBM   | SO    
  ACR   | ERF   | M4A/V | PCD   | SR2   
  AFM   | EXE   |g MEF  | PDB   | SRF   
  AI    | EXIF  | MIE   | PDF   | SRW   
  AIFF  | EXR   | MIFF  | PEF   | SVG   
  APE   | EXV   | MKA   | PFA   | SWF   
  ARW   | F4A/V | MKS   | PFB   | THM   
  ASF   | FFF   | MKV   | PFM   | TIFF  
  AVI   | FLA   | MNG   | PGF   | TORRENT
  AZW   | FLAC  | MOBI  | PGM   | TTC   
  BMP   | FLV   | MODD  | PLIST | TTF   
  BTF   | FPF   | MOI   | PICT  | VCF   
  CHM   | FPX   | MOS   | PMP   | VRD   
  COS   | GIF   | MOV   | PNG   | VSD   
  CR2   | GZ    | MP3   | PPM   | WAV   
  CRW   | HDP   | MP4   | PPT   | WDP   
  CS1   | HDR   | MPC   | PPTX  | WEBP  
  DCM   | HTML  | MPG   | PS    | WEBM  
  DCP   | ICC   | MPO   | PSB   | WMA   
  DCR   | ICS   | MQV   | PSD   | WMV   
  DFONT | IDML  | MRW   | PSP   | WV    
  DIVX  | IIQ   | MXF   | QTIF  | X3F   
  DJVU  | IND   | NEF   | RA    | XCF   
  DLL   | INX   | NRW   | RAF   | XLS   
  DNG   | ITC   | NUMBERS  RAM  | XLSX  
  DOC   | J2C   | ODP   | RAR   | XMP   
  DOCX  | JNG   | ODS   | RAW   | ZIP   
  DPX   | JP2   | ODT   | RIFF  |
  DR4   | JPEG  | OFR   | RSRC  |
  DSS   | K25   | OGG   | RTF   |
  DV    | KDC   | OGV   | RW2   |

 ```
