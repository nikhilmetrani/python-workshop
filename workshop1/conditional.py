#!/usr/bin/python

import sys

n = 10

if len(sys.argv) >= 2:
    n = int(sys.argv[1]) #type cast to int is necessary otherwise the argument will be treated as string

if n > 0:
    print n, "is positive"
elif n < 0:
    print n, "is negative"
else:
    print n, "is neutral"