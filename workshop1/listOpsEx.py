__author__ = 'nick'

def printValue(value="default Value"):
    return str(len(value)) + "::" + value

def addValues(value1=0, value2=0):
    return value1 + value2

def evenLengths(length):
    return length%2 == 0

def oddLengths(length):
    return length%2 != 0

print "map: applies function to each element of list"

fruits = ["Apple", "Orange", "Pear", "Banana", "Durian", "Grape"]

fruits2 = map(printValue, fruits)

print fruits2

lengths = map(len, fruits)

print lengths

print "Let's reduce lengths with addValues"

reduced = reduce(addValues, lengths, 0)

print "Reduced:", reduced

try:
    print "Let's reduce fruits with printValue"
    reduced = reduce(printValue, fruits)
    print "Reduced:", reduced
except:
    print "Expected error: printValue takes only one argument and reduce needs function with 2 arguments"

print "Let's try filter: adds element to list only if applied function returns true"

filteredEven = filter(evenLengths, lengths)
print "Even:", filteredEven

filteredOdd = filter(oddLengths, lengths)
print "Odd:", filteredOdd