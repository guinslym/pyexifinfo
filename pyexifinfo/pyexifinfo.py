import subprocess, json, os


this_file_exist = lambda x: os.path.exists(filename)

####HELPER section

def command_line(cmd):
    """Handle the command line call

    keyword arguments:
    cmd = a list

    return
    0 if error
    or a string for the command line output
    """
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
        #convert bytes to string
        s = s.decode('utf-8').rstrip('\r\n')
        return json.loads(s)
    else:
        return filename

def get_csv(filename):
    '''Return a csv representation of the exif
    arg: filename
    '''
    filename = os.path.abspath(filename)
    s = command_line(['exiftool', '-G', '-csv', '-sort', filename])
    if s:
        #convert bytes to string
        s = s.decode('utf-8')
        return s
    else:
        return 0

def get_xml(filename):
    '''Return a XML representation of the exif'''
    filename = os.path.abspath(filename)
    s = command_line(['exiftool', '-G', '-X', '-sort', filename])
    if s:
        #convert bytes to string
        s = s.decode('utf-8')
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



