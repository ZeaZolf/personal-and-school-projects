"""
RMS Multi-Tool Python Library
version: 1.2
Work started: 11/14/2023 15:54 MST
This is a simple multi-use Python library used for Rose's (ZeaZolf or just_another_transfem) many individual projects. RMS - Rose's initals. That's why so. Will use random and requests library.
Requires internet connection. But everything, even your right kidney requires internet, so what's the disclaimer for?
"""

import random, requests

### Test function
def init():
	print("RMSL multi-tool library initalized.")


### Networking tools
def web_grabber(url):
	response = requests.get(url)
	body = response.json()
	return body

def web_grabber_with_para(url, params):
	response = requests.get(url, params=params)
	body = response.json()
	return body
def url_checker(url):
	response = requests.get(url)
	print("Status code is " + str(response.status_code()) + ". Refer to code list for info.")

### Random
def randnum(min, max):
	ret = random.randint(min, max)
	return ret

