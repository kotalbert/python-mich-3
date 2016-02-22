import socket
import re

conStr = raw_input('URL to be searched:')
host = re.findall('http://(.+?)/', conStr)

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host[0], 80))
    mysock.send('GET %s HTTP/1.0\n\n' % conStr)

    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print data

    mysock.close()
except:
    print 'Bad URL'
