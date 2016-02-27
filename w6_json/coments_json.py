# Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_248056.json (Sum ends with 12)

import json
import urllib

url = 'http://python-data.dr-chuck.net/comments_248056.json'
jh = urllib.urlopen(url)
data = jh.read()
print 'Retrieved ', len(data), ' characters'

parsed = json.loads(data)
comments = parsed['comments']

s = 0

for com in comments:
   c = int(com['count'])
   s += c

print s
