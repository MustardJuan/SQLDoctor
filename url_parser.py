from urllib.parse import urlparse, parse_qs

def parse_url(url, replacements_list):

    parsed_url = urlparse(url)
    queries = parse_qs(parsed_url.query)
    
    new_query_list = []
    count = 0
    for key,value in queries.items():
        queries[key] = [replacements_list[count]]
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

    return new_url