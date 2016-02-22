import urllib

fh = urllib.urlopen('http://www.py4inf.com/code/romeo-full.txt')
c = 0
for line in fh:
    c += len(line)
    if (c > 3000):
        continue
    else:
        print line.rstrip()

print 'Characters read:\t%d' % c
