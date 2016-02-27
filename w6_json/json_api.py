import urllib
import json


def get(uname):
    if len(uname) < 1:
        return None

    url = surl + urllib.urlencode({'sensor': 'false', 'address': uname})
    print url
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved ', len(str(data)), ' characters'
    try:
        js = json.loads(data)
    except:
        js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        return None
    print json.dumps(js, indent=4)
    return js


def getPlaceID(js):
    if js is None:
        return None
    return js['results'][0]['place_id']


surl = 'http://python-data.dr-chuck.net/geojson?'
while True:
    uname = raw_input("Enter Uni Name: ")
    js = get(uname)
    print getPlaceID(js)
