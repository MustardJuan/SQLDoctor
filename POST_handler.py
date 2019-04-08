from bs4 import BeautifulSoup
import requests
import re
from Display import *

#searches html page for any potential forms 
#generates and executes POST requests to the victim webserver
def POST_generator():
    
    URL = "someURLEntry"
    r = requests.get(URL)
    html_bytes = r.text

   #bsoup allows for ease of html parsing and provides general formatting
    soup =  BeautifulSoup(html_bytes, 'lxml')
    token = soup.find_all('input')

    #regex that is used to search for name fields in html
    pattern = "((name=)([\"])\w*([\"]))"
    list_input_names = []
    form_inputs = []

    #actual html tag and field search done via the re.findall call
    #those found are sent to - list_input_names
    for i in token:
        try:
            found = re.findall(pattern, str(i))
            list_input_names.append(found[0][0])
        except:
            print("no name found")
    
    for i in list_input_names:
	#re.findall call looks for all name tags that satisfy the regex constraint
        form_inputs.append(re.findall(r'"(.*?)"',i)[0])

    print(form_inputs)

    POST_send("pass arguments which are listed below")

#Actually sends the POST request with the payload/information as specified 
def POST_send(URL, username_field, password_field, username_input, password_input):
    
    payload = {username_field: username_input, password_field : password_input}
    victim = URL
    r = requests.post(victim, payload)
    print(r.text)

if __name__ == "__main__" :

    display_welcome()	
    POST_generator()
