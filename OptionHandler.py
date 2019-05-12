#Will handle option/commandline parsing
#Just a rough high-level outline

from Display import *
import argparse

def option_parser():

    #parse command line args, -f is fuzzing, -u denotes a url 
    parser = argparse.ArgumentParser()

    #add options for -f, -u
    parser.add_argument("-f", help="Do fuzzing",action="store_true")
    parser.add_argument("-u", help="Pass parameters to URL",action="store_true")
    parser.add_argument("TargetURL", help="Target URL", type=str)
    
    # parse and return args
    args = parser.parse_args()
    return args