# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

# url = raw_input('Enter - ')
url = "https://cmake.org/cmake-tutorial/"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('p')
c = 0
for tag in tags:
    c += 1

print c
