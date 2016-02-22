import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

c = 0

while True:
    data = mysock.recv(512)
    l = len(data)
    c += l
    if (l < 1):
        break
    if (c > 3000):
        continue
    else:
        print data

print 'Characters read:\t%d' % c

mysock.close()
