PyExifInfo
======================================================

Yet Another python wrapper for Phil Harvey' Exiftool
ExifTool is the corner stone library to look for when you need to extract Exif or other types of metadata whithin a picture or many other files type.

(French) ExifTool est la package de référence quand il s'agit d'analyser l'Exif ou les métadonnées d'une photo

##Installation
		[sudo] pip install pyexifinfo

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
  3FR   r     | DVB   r/w   | KEY   r     | ORF   r/w   | RWL   r/w
  3G2   r/w   | DYLIB r     | LA    r     | OTF   r     | RWZ   r
  3GP   r/w   | EIP   r     | LFP   r     | PAC   r     | RM    r
  AA    r     | EPS   r/w   | LNK   r     | PAGES r     | SEQ   r
  AAX   r/w   | EPUB  r     | M2TS  r     | PBM   r/w   | SO    r
  ACR   r     | ERF   r/w   | M4A/V r/w   | PCD   r     | SR2   r/w
  AFM   r     | EXE   r     | MEF   r/w   | PDB   r     | SRF   r
  AI    r/w   | EXIF  r/w/c | MIE   r/w/c | PDF   r/w   | SRW   r/w
  AIFF  r     | EXR   r     | MIFF  r     | PEF   r/w   | SVG   r
  APE   r     | EXV   r/w/c | MKA   r     | PFA   r     | SWF   r
  ARW   r/w   | F4A/V r/w   | MKS   r     | PFB   r     | THM   r/w
  ASF   r     | FFF   r/w   | MKV   r     | PFM   r     | TIFF  r/w
  AVI   r     | FLA   r     | MNG   r/w   | PGF   r     | TORRENT r
  AZW   r     | FLAC  r     | MOBI  r     | PGM   r/w   | TTC   r
  BMP   r     | FLV   r     | MODD  r     | PLIST r     | TTF   r
  BTF   r     | FPF   r     | MOI   r     | PICT  r     | VCF   r
  CHM   r     | FPX   r     | MOS   r/w   | PMP   r     | VRD   r/w/c
  COS   r     | GIF   r/w   | MOV   r/w   | PNG   r/w   | VSD   r
  CR2   r/w   | GZ    r     | MP3   r     | PPM   r/w   | WAV   r
  CRW   r/w   | HDP   r/w   | MP4   r/w   | PPT   r     | WDP   r/w
  CS1   r/w   | HDR   r     | MPC   r     | PPTX  r     | WEBP  r
  DCM   r     | HTML  r     | MPG   r     | PS    r/w   | WEBM  r
  DCP   r/w   | ICC   r/w/c | MPO   r/w   | PSB   r/w   | WMA   r
  DCR   r     | ICS   r     | MQV   r/w   | PSD   r/w   | WMV   r
  DFONT r     | IDML  r     | MRW   r/w   | PSP   r     | WV    r
  DIVX  r     | IIQ   r/w   | MXF   r     | QTIF  r/w   | X3F   r/w
  DJVU  r     | IND   r/w   | NEF   r/w   | RA    r     | XCF   r
  DLL   r     | INX   r     | NRW   r/w   | RAF   r/w   | XLS   r
  DNG   r/w   | ITC   r     | NUMBERS r   | RAM   r     | XLSX  r
  DOC   r     | J2C   r     | ODP   r     | RAR   r     | XMP   r/w/c
  DOCX  r     | JNG   r/w   | ODS   r     | RAW   r/w   | ZIP   r
  DPX   r     | JP2   r/w   | ODT   r     | RIFF  r     |
  DR4   r/w/c | JPEG  r/w   | OFR   r     | RSRC  r     |
  DSS   r     | K25   r     | OGG   r     | RTF   r     |
  DV    r     | KDC   r     | OGV   r     | RW2   r/w   |
  Meta Information
  ----------------------+----------------------+---------------------
  EXIF           r/w/c  |  CIFF           r/w  |  Ricoh RMETA    r
  GPS            r/w/c  |  AFCP           r/w  |  Picture Info   r
  IPTC           r/w/c  |  Kodak Meta     r/w  |  Adobe APP14    r
  XMP            r/w/c  |  FotoStation    r/w  |  MPF            r
  MakerNotes     r/w/c  |  PhotoMechanic  r/w  |  Stim           r
  Photoshop IRB  r/w/c  |  JPEG 2000      r    |  DPX            r
  ICC Profile    r/w/c  |  DICOM          r    |  APE            r
  MIE            r/w/c  |  Flash          r    |  Vorbis         r
  JFIF           r/w/c  |  FlashPix       r    |  SPIFF          r
  Ducky APP12    r/w/c  |  QuickTime      r    |  DjVu           r
  PDF            r/w/c  |  Matroska       r    |  M2TS           r
  PNG            r/w/c  |  MXF            r    |  PE/COFF        r
  Canon VRD      r/w/c  |  PrintIM        r    |  AVCHD          r
  Nikon Capture  r/w/c  |  FLAC           r    |  ZIP            r
  GeoTIFF        r/w/c  |  ID3            r    |  (and more)
 ```
