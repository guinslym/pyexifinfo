import subprocess, json, os


def command_line(cmd):
    try:
        s = subprocess.check_output(cmd)
        return s.strip()
    except:
        return 0

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
        
