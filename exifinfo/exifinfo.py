# -*- coding: utf-8 -*-
'''
import exiftool

files = ["a.jpg", "b.png", "c.tif"]
with exiftool.ExifTool() as et:
    metadata = et.get_metadata_batch(files)

metadata
#########################################################################

import exifinfo
exifinfo.get_json()


#How I want to call it

'a.png'.get_json()
or
exifinfo.get_json('a.png')


###Difficulty 
if file exist
if metadata in french

##helper
http://stackoverflow.com/questions/18337407/saving-utf-8-texts-in-json-dumps-as-utf8-not-as-u-escape-sequence
'''

#from exifinfo import ExifTool
import subprocess, json, os, csv

command_line = lambda x: subprocess.check_output(x)

def general(command_argument):
    try:
        s = command_line(command_argument)
        return s.split('\n')[0]
    except:
        return 0

def ver():
    return general(["exiftool","-ver"])

def get_json():
    try:
        s = command_line(['exiftool', '-G', '-j', 'a.png'])
        s = s.rstrip('\r\n')
        s = json.loads(s)
        #json.dumps(s, sort_keys=True, indent=4)
        #json_string = json.dumps(u"ברי צקלה", ensure_ascii=False).encode('utf8')
        return s
    except:
    	return 0

def get_csv():
    try:
        s = command_line(['exiftool', '-sort', '-G', '-csv', 'a.png'])
        return s.split('\n')[0]
    except:
    	return 0
        
def get_php():
    try:
        s = command_line(['exiftool', '-sort', '-G', '-php', 'a.png'])
        s = s.rstrip('\r\n')
        return s
    except:
        return 0

def get_xml():
    try:
        s = command_line(['exiftool', '-sort', '-G', '-X', 'a.png'])
        return s.split('\n')[0]
    except:
        return 0

def exiftool_tags():
    try:
        s = command_line(['exiftool', '-list'])
        return s.split('\n')
    except:
        return 0

import exiftool

files = ["a.png"]
with exiftool.ExifTool() as et:
    metadata = et.get_metadata_batch(files)

def extraire(metadata):
    top_level = {}
    print('\n\n')
    print(type(metadata))
    print('\n\n')
    for key, value in metadata.iteritems():
        if ':' in key:
            top, taxonymy = key.split(':')
            #print(top)
            if top in top_level.keys():
                #print(top_level.get(top))
                top_level.get(top).update({taxonymy:value})
            else:
                top_level.update({top:{taxonymy:value}})
        else:
            top_level.update({key:value})
    #print(top_level)
    return top_level


from bs4 import BeautifulSoup
import urllib

f = urllib.urlopen("http://www.sno.phy.queensu.ca/~phil/exiftool/")
soup = BeautifulSoup(f) 
soup

soup
mydivs = soup.find("table", { "class" : "norm tight sm bm" })
mydivs = mydivs.findAll('tr')

supported_files = []
for info in mydivs[1::]:
    print(info.find('td').text)
    supported_files.append(info.find('td').text)