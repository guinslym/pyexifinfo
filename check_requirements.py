import subprocess
import sys, os

def check_if_exiftool_is_already_installed():
    """Requirements
    
    This function will check if Exiftool is installed
    on your system

    Return: True if Exiftool is Installed
            False if not
    """
    result = 1;
    command = ["exiftool", "-ver"]

    with open(os.devnull, "w") as fnull:
        result = subprocess.call(
            command, 
            stdout = fnull, 
            stderr = fnull
        )
    #Exiftool is not installed
    if result != 0:
        print_a_header('Exiftool needs to be installed on your system')
        print_a_header('Visit http://www.sno.phy.queensu.ca/~phil/exiftool/')
        return False
    else:
        return True

def print_a_header(message="-"):
    """Header

    This function will output a message in a header
    
    Keyword Arguments:
        message {str} -- [the message string] (default: {"-"})
    """
    print("-".center(60,'-'))
    print(message.center(60,'-'))
    print("-".center(60,'-'))
    print()
