import requests
import sys

from Display import *
from OptionHandler import *
from POST_handler import *
from url_parser import *

def main():

    #Grabs the options entered by the user
    args = option_parser()
    
    if(args.u):
        # post_using_url(args.TargetURL)
        parse_url(args.TargetURL)
    else:
        POST_generator(args.TargetURL, args.f)
 
if __name__ == "__main__":

    #Default welcome text
    display_welcome()
    main()