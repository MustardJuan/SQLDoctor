from urllib.parse import urlparse, parse_qs
from pull_from_CSV import *
import requests


def parse_url(url):

    payloads_list = [] # will be the list of just payloads
    payloads = pull_from_CSV() # dictionary where the key is the database name, and value is the payload

    # extracting payloads from dictionary (will be the value)
    for key,value in payloads.items():
        payloads_list.append(value)

    parsed_url = urlparse(url) # use urlparse to parse the url for certain values
    queries = parse_qs(parsed_url.query) # get the queries from the URL (we are getting the parameters and their values in a dictionary)
    
    # iterate through payload list
    for payload in payloads_list:
        new_query_list = [] # will be a list of the new queries (it will be the parameters equal to payloads)
        
        #count = 0 
        for key,value in queries.items():
            queries[key] = [payload]
            new_query_list.append(key+"="+queries[key][0])

            #count += 1

        count = 0 # used for checking if we are on the last parameter value item
        new_query = "" # will be the new query with & symbols
        for item in new_query_list:

            #checking if we are on last parameter, if so we do not need an & symbol at the end 
            if(count < len(new_query_list) - 1): 
                new_query = new_query + item + "&" # append new parameter with value to our new_query
            else:
                new_query = new_query + item
            
            count += 1

        # Make the new URL with the scheme(e.g. http) and the netloc (e.g. google.com) and the path (e.g. /search.php) add ? then the parameters and new query
        new_url = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path + "?" + parsed_url.params + new_query
        


        # Post the new URL
        post_using_url(new_url, new_query)

    return new_url

def post_using_url(url, payload):
 
    r = requests.get(url) # since we are using a URL we can use GET instead of POST
    
    file = open("URL_Information.txt", "a") # logging of all attempts and their returns
    file.write("Payload: " + payload + "\n\n" + r.text + "\n\n") # write the information to the log file

    # if the status code is not a 404 write information to success file, this file will have the interesting information
    if(r.status_code != 404):
        file_success = open("Successes", "a")
        file_success.write("Payload: " + payload + " and the URL: " + url + "\n")
        file_success.write(r.text + "\n")


    print("Payload: " + payload + " and the URL: " + url)
    print(r.status_code)