#Will handle option/commandline parsing
#Just a rough high-level outline

from Display import *
import argparse

def option_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help="Display fingerprint of database",action="store_true")
    parser.add_argument("--fuzz", help="Do fuzzing",action="store_true")
    parser.add_argument("-a", help="Display attack",action="store_true")
    parser.add_argument("-x", help="Display unique attack",action="store_true")
    parser.add_argument("TargetURL", help="Target URL", type=str)
    
    args = parser.parse_args()

    return args
