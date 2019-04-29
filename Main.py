import requests
import sys

from Display import *
from OptionHandler import *
from POST_handler import *

def main():

    #Grabs the options entered by the user
    args = option_parser()
    
    POST_generator(args.TargetURL, args.fuzz)
 
if __name__ == "__main__":

    #Default welcome text
    display_welcome()
    main()