from urllib.parse import urlparse, parse_qs
from pull_from_CSV import *
import requests

def parse_url(url):

    payloads_list = []
    payloads = pull_from_CSV()

    for key,value in payloads.items():
        payloads_list.append(value)

    parsed_url = urlparse(url)
    queries = parse_qs(parsed_url.query)
    
    for payload in payloads_list:
        new_query_list = []
        count = 0
        for key,value in queries.items():
            queries[key] = [payload]
            new_query_list.append(key+"="+queries[key][0])

            count += 1

        count = 0
        new_query = ""
        for item in new_query_list:
            if(count < len(new_query_list) - 1):
                new_query = new_query + item + "&"
            else:
                new_query = new_query + item
            count += 1

        new_url = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path + "?" + parsed_url.params + new_query
        
        post_using_url(new_url, new_query)

    return new_url

def post_using_url(url, payload):

    r = requests.get(url)
    
    #temp test code to write to file
    file = open("hi.txt", "a")
    file.write("Hello this is the payload: " + payload + "\n\n" + r.text + "\n\n")
    print(r.status_code)
    # print(r.text)