#Will handle option/commandline parsing
#Just a rough high-level outline

from Display import *
import argparse

def option_parser():

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help="Do fuzzing",action="store_true")
    parser.add_argument("-u", help="Pass parameters to URL",action="store_true")
    parser.add_argument("TargetURL", help="Target URL", type=str)
    
    args = parser.parse_args()

    return args