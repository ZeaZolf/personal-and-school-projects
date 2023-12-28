"""
BREAKING BAD QUOTES, BITCH!
Original version - pre-RMSL, finished 11/11/2023 09:02 AM
"""
# Libaries
import requests
# Req stuff
BASE_URL = "https://api.breakingbadquotes.xyz/v1/quotes"
# Requests
r = requests.get(BASE_URL)
body = r.json()
# Output
print(body[0]["quote"])
print()
print("...was said by " + body[0]["author"])

again = input("Would you like more quotes? Hit enter for more. If not, type 'exit' to exit the program.")

while again != exit:
    print()
    r = requests.get(BASE_URL)
    body = r.json()
    print(body[0]["quote"])
    print()
    print("...was said by " + body[0]["author"])
    print()
    again = input("Would you like more quotes? Hit enter for more. If not, type 'exit' to exit the program.")

    if again == "exit":
        break
