# http://python-data.dr-chuck.net/known_by_Fikret.html

import urllib
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/known_by_Fikret.html"

cnt = int(raw_input("Enter count:"))
pos = int(raw_input("Enter position:"))


def getATags(url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    return soup('a')


def getUrl(tags, pos):
    return tags[pos-1].get('href', None)


for i in range(cnt+1):
    print url
    url = getUrl(getATags(url), pos)
