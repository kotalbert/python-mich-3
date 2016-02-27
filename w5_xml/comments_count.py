# Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_248052.xml (Sum ends with 77)

import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_248052.xml'
print 'Retrieving ', url

uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved ', len(data), ' characters'
tree = ET.fromstring(data)

commentsRoot = tree.find('comments')
comments = commentsRoot.findall('comment')

s = 0

for comment in comments:
    c = int(comment.find('count').text)
    s += c

print s
