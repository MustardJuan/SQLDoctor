import requests
import sys

from Display import *
from OptionHandler import *

def main():

    #Variable that holds payload
    payload = "some random payload"

    #Grabs the options entered by the user
    URLFlag = option_parser(sys.argv)

    #Grabs the URL from the command line specified by the user
    victimURL = sys.argv[2]

    #Executes POST request using the specified payload with the URL
    webResponse = requests.post(victimURL, payload)

    print(victimURL)

if __name__ == "__main__":

    #Default welcome text
    display_welcome()

    main()