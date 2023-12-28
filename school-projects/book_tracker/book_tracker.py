"""
Book Tracker
School project
Date finished: 12-14-2023 11:36:10 AM MST
Requires RMSL library
"""
### RMSL IMPORT & TEST 
import rmsl, sys
#rmsl.init()
print()
### CONSTANTS
BASE_URL = "https://openlibrary.org/search.json"
FIELDS = "title,author_name"

### QUERY
query = input("What book are you interested in? ")

### PARAMS
p = {"title": query, "fields": FIELDS} 
### BOOK GRABBER
body = rmsl.web_grabber_with_para(BASE_URL, params=p)
bn = body["docs"][0]
bt = bn["title"]
ba = bn["author_name"][0]
print()
print("This book is", bt, "by", ba)
print()
print("""Would you like to:
(1) ...add it to your list?
(2) ...view your list?
(3) ...exit the program?
""")
usr_ip = int(input("Enter your choice: "))
print()
if usr_ip == 1:
    with open("books.txt", "a") as file:
        print(bt, ba, sep=" | ", file=file)
if usr_ip == 2:
    with open("books.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line)
if usr_ip == 3:
    sys.exit()
