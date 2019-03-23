#Will handle option/commandline parsing
#Just a rough high-level outline

from Display import *


def option_parser(arguments):

    #splits command line input looking for flags by checking for tack
    for x in arguments:
        if x[0] == '-':
            flags = x.split("-")
            option_lookup(flags)

def option_lookup(flag):

    #dictionary mapping base output to identified flag
    flag_output = {'h' : display_help(),
                   'f' : display_fingerprint(),
                   'a' : display_attack(),
                   'x' : display_uniq_attack()}

    #something wrong with my logic here but checks to see if flag is valid and outputs accordingly
    if flag in flag_output:
        flag_output[flag]()
