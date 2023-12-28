"""
BREAKING BAD QUOTES, BITCH!
RMSL version - RMSL required
Finished as of 12/27/2023 7:25 PM
"""
# Libaries
import rmsl
# Req stuff
BASE_URL = "https://api.breakingbadquotes.xyz/v1/quotes"
# Requests
body = rmsl.web_grabber(BASE_URL)
# Output
print(body[0]["quote"])
print()
print("...was said by " + body[0]["author"])

again = input("Would you like more quotes? Hit enter for more. If not, type 'exit' to exit the program. ")

while again != exit:
    print()
    body = rmsl.web_grabber(BASE_URL)
    print(body[0]["quote"])
    print()
    print("...was said by " + body[0]["author"])
    print()
    again = input("Would you like more quotes? Hit enter for more. If not, type 'exit' to exit the program. ")

    if again == "exit":
        break
