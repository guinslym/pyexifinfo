import subprocess, json, os


this_file_exist = lambda x: os.path.exists(filename)

####HELPER section

def command_line(cmd):
    try:
        s = subprocess.check_output(cmd)
        return s.strip()
    except subprocess.CalledProcessError:
        return 0

def information(filename):
    """Returns the file exif"""
    result = get_json(filename)
    result = result[0]
    return result
######################

def ver():
    '''Retrieve the current version of exiftool installed on your computer
    '''
    s = command_line(["exiftool","-ver"])
    if s:
        return s.split()
    else:
        return 0

def get_json(filename):
    '''Return a json value of the exif

    '''
    filename = os.path.abspath(filename)
    s = command_line(['exiftool', '-G', '-j', '-sort', filename])
    if s:
        s = s.rstrip('\r\n')
        return json.loads(s)
    else:
	  return 0

def get_csv(filename):
    '''Return a csv representation of the exif
    arg: filename
    '''
    filename = os.path.abspath(filename)
    s = command_line(['exiftool', '-G', '-csv', '-sort', filename])
    if s:
        return s
    else:
        return 0

def get_xml(filename):
    '''Return a XML representation of the exif
    '''
    filename = os.path.abspath(filename)
    s = command_line(['exiftool', '-G', '-X', '-sort', filename])
    if s:
        return s
    else:
        return 0
        
def fileType(filename):
    """Returns the file extension"""
    result =  information(filename)
    return result.get('File:FileType', 0)

def mimeType(filename):
    """Returns the file extension"""
    result =  information(filename)
    return result.get('File:MIMEType', 0)

def imageSize(filename):
    """Returns the file size"""
    result =  information(filename)
    return result.get('Composite:ImageSize', 0)

def imageWidth(filename):
    """Returns the file width"""
    result =  information(filename)
    return result.get('PNG:ImageWidth', 0)    

def imageHeight(filename):
    """Returns the file height"""
    result =  information(filename)
    return result.get('PNG:imageHeight', 0) 