# Data
# Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_248055.html
# (Sum ends with 50)

import urllib
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/comments_248055.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')
s = 0
for tag in tags:
    s += int(tag.contents[0])
print s
