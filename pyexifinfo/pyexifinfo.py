#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import subprocess
import json
import os
import sys

"""
#Helper functions
===========================================================
===========================================================
===========================================================
===========================================================
"""

def check_if_this_file_exist(filename):
    """Check if this file exist and if it's a directory
    
    This function will check if the given filename
    actually exists and if it's not a Directory
    
    Arguments:
        filename {[type]} -- filename

    Return:
        True  : if it's not a directory and if this file exist
        False : If it's not a file and if it's a directory
    """
    #get the absolute path
    filename = os.path.abspath(filename)

    #Boolean
    this_file_exist = os.path.exists(filename)
    a_directory = os.path.isdir(filename)

    result = this_file_exist and not a_directory
    return result

def exit_if_this_file_does_not_exit(filename):
    """Exit if this file does not exit
    
    Upon the previous function if This filename does
    not exist or if it's a directory EXIT this application
    
    Arguments:
        filename {[type]} -- your filename
    """
    result = check_if_this_file_exist(filename)
    if result:
        pass
    else:
        print(":( The filename that you gave me either does not exist")
        print("or it's a directory.")
        print("The given filename is: {0}".format(os.path.abspath(filename)))
        raise ValueError "Encountered error"

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
    exit_if_this_file_does_not_exit(filename)
    filename = os.path.abspath(filename)
    result = get_json(filename)
    if not result:
        message = 'The filename given is either a directory or \it \'s'
        raise ValueError  message + ' not the proper filename'
    else:
        result = result[0]
        return result
######################

"""
#API
===========================================================
===========================================================
===========================================================
===========================================================
"""

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
    exit_if_this_file_does_not_exit(filename)

    #Process this function
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
    exit_if_this_file_does_not_exit(filename)

    #Process this function
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
    exit_if_this_file_does_not_exit(filename)

    #Process this function
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



