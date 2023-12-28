"""
Show Informer
Originally created for a school project
Finished as of 09/20/2023 at 10:53 AM 
"""
### LIBRARY

import requests
### URLS
BASE_URL = "http://api.tvmaze.com"
PATH = "/singlesearch/shows"

### FUNCTIONS 
def check_url():
    global BASE_URL
    global PATH
    qt = { "q" : "Test"}
    test = requests.get(BASE_URL + PATH, params=qt)
    if test.status_code != 200:
        return False
    else:
        return True
    
def show_inform(show):
    global BASE_URL, PATH
    queery = { "q" : show}
    shwr = requests.get(BASE_URL + PATH, params=queery)
    body = shwr.json()
    print("Here is the information for: " + body["name"])
    print()
    print("Date first aired: "+ body["premiered"])
    print("Genres: " + str(body["genres"]))
    print("Show status: " + body["status"])
    plot = body["summary"]
    unwc = { "<p>" : "", "</p>" : "", "<b>" : "", "</b>": ""}
    for unwc, repl in list(unwc.items()):
        plot = plot.replace(unwc, repl)
    print("A summary: " + plot)    
    

### CALLS AND CHECKS

if check_url() == True:
    title = input("What show would you like to see info of? " )
    show_inform(title)
    print()
    print()
    t2 = input("Would you like to search another show? If not, then type 'exit' to exit. ")
    while t2 != "exit":
        
        if t2 == "exit":
            break 
        else:
            show_inform(t2)
            print()
            print()
            t2 = input("Would you like to search another show? If not, then type 'exit' to exit. ")
