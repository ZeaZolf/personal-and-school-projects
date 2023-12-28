"""
RMS Python Library
version: 1.2.1
This is a simple multi-use Python library used for my personal products, and sometimes for projects in School. So, don't be expecting some gourmet stuff in here.
will improve upon it in the future
"""

import random, requests

### Test function
def init():
	print("RMSL initalized")


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

