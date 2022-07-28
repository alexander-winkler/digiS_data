import requests
from collections import Counter
from lxml import etree

# Api-Key has to be obtained via https://labs.deutsche-digitale-bibliothek.de/app/ddbapi/
api_key = ""

# Variables
query = "Förderprogramm zur Digitalisierung von Objekten des kulturellen Erbes des Landes Berlin"

# Functions

def queryDDB(query,n,step):
    endpoint = "https://api.deutsche-digitale-bibliothek.de/search"
    par = {
        'rows' : step,
        'offset' : n,
        'oauth_consumer_key' : api_key,
        'query' : query
    }
    
    r = requests.get(endpoint, params = par, timeout=20)
    print(r.url)
    
    return r

def noOfRes(query):
    endpoint = "https://api.deutsche-digitale-bibliothek.de/search"
    par = {
        'query' : query,
        'rows' : 1,
        'oauth_consumer_key' : api_key
    }
    res = requests.get(endpoint, par)
    n = res.json().get('numberOfResults')
    print(f"Hits for query: {query} \t {n}")
    return n

def iterativeQuery(query,step=50000):
    output = []
    results = noOfRes(query)
    for i in range(1,results +1 , step):
        print(f"item {i} to {i+step} (out of {results})")
        res = output.extend(queryDDB(query,i,step).json().get('results')[0].get('docs'))
    return output


completeDigis = iterativeQuery(query)
digiS_ids = Counter((i.get('id') for i in completeDigis))

for i in digiS_ids :
    print(i)
    filename = i
    try:
        etree.parse(filename + ".xml")
    except:
        try:
            with open(filename + ".xml", 'w') as OUT:
                print(infoID(i).json().get('source').get('record').get('$'), file = OUT)
        except Exception as e:
            print(e)