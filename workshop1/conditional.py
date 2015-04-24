#!/usr/bin/python

import sys

n = 10

# Conditional statement
if len(sys.argv) >= 2:
    n = int(sys.argv[1]) #type cast to int is necessary otherwise the argument will be treated as string

# Chained conditional
if n > 0:
    print n, "is positive"
elif n < 0:
    print n, "is negative"
else:
    print n, "is neutral"

# Nested conditional
if len(sys.argv) == 3:
    p = int(sys.argv[2])
    if n > p:
        print "Before: n=", n, " p=", p
        n, p = p, n
        print "n, p = p, n: n=", n, " p=", p
    else:
        if n==p:
            p = p + 1
        else:
            print "recorder not necessary"

