import requests
import sys

from Display import *
from OptionHandler import *
from POST_handler import *
from url_parser import *

def main():

    #Grabs the options entered by the user
    args = option_parser()
    
    # basically determines if we end up searching for fields or use the ones provided
    if(args.u):
        parse_url(args.TargetURL)
    else:
        POST_generator(args.TargetURL, args.f)
 
if __name__ == "__main__":

    #Default welcome text
    display_welcome()
    main()