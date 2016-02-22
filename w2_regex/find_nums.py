import re

fh = open('data.txt')


def sumNums(line):
    """
    Sum a numbers found in a line
    """
    s = 0
    nums = re.findall('[0-9]+', line)
    for num in nums:
        s += int(num)
    return s

s = 0
for line in fh:
    s += sumNums(line.rstrip())

print ("Sum of numbers in file:\t %d" % s)
