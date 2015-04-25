#!/usr/bin/python

import sys

firstArg = 10

# Conditional statement
if len(sys.argv) >= 2:
    firstArg = int(sys.argv[1]) #type cast to int is necessary otherwise the argument will be treated as string

# Chained conditional
if firstArg > 0:
    print firstArg, "is positive"
elif firstArg < 0:
    print firstArg, "is negative"
else:
    print firstArg, "is neutral"

# Nested conditional
if len(sys.argv) == 3:
    secondArg = int(sys.argv[2])
    if firstArg > secondArg:
        print "Before: firstArg=", firstArg, " secondArg=", secondArg
        firstArg, secondArg = secondArg, firstArg
        print "firstArg, secondArg = secondArg, firstArg: firstArg=", firstArg, " secondArg=", secondArg
    else:
        if firstArg == secondArg:
            secondArg += 1
            print "After increment, secondArg:", secondArg
        else:
            print "recorder not necessary"

