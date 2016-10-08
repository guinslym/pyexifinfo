#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        filename {string} -- filename

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
    if result == False:
        raise ValueError('The filename given was either non existent or was a directory')
    else:
        return result

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
        s = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        s = s.stdout.read()

        return s.strip()

    except subprocess.CalledProcessError:
        return 0

def information(filename):
    """Returns the file exif"""
    check_if_this_file_exist(filename)
    filename = os.path.abspath(filename)
    result = get_json(filename)
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
    """ Version of Exiftool

    Retrieve the current version of exiftool installed on your computer

    Returns:
        [string] -- a string in a list. i.e: ['9.46']

    Raises:
        ValueError -- If you uninstalled or haven't installed yet Exiftool
        than this should raise an error
    """
    s = command_line(["exiftool","-ver"])
    if s:
        return s.split()
    else:
        raise ValueError("You didn't install Exiftool on this Operating System")

def get_json(filename):
    """ Return a json value of the exif

    Get a filename and return a JSON object

    Arguments:
        filename {string} -- your filename

    Returns:
        [JSON] -- Return a JSON object
    """
    check_if_this_file_exist(filename)

    #Process this function
    filename = os.path.abspath(filename)
    s = command_line(['exiftool', '-G', '-j', '-sort', filename])
    if s:
        #convert bytes to string
        s = s.decode('utf-8').rstrip('\r\n')
        return json.loads(s)
    else:
        return s

def get_csv(filename):
    """ Return a csv representation of the exif

    get a filename and returns a unicode string with a CSV format

    Arguments:
        filename {string} -- your filename

    Returns:
        [unicode] -- unicode string
    """
    check_if_this_file_exist(filename)

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
    """ Return a XML representation of the exif

    get a filename and return a unicode string  in a XML format

    Arguments:
        filename {string} -- your filename

    Returns:
        string -- a string formatted XML representation
    """
    check_if_this_file_exist(filename)

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
