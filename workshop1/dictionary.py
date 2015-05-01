__author__ = 'nick'

import sys

def histogram(dictArg):
    dict2 = dict()
    for value in dictArg:
        if value not in dict2:
            dict2[value] = 1
        else:
            dict2[value] += 1
    return dict2

def printdict(dictArg):
    for value in dictArg:
        print value, dictArg[value]

dictionary = dict()

dictionary["one"] = "Jeden"
dictionary["two"] = "Dwa"
dictionary["three"] = "Trzy"
dictionary["four"] = "Cztery"
dictionary["five"] = "Piec"
dictionary["six"] = "Szesc"
dictionary["seven"] = "Siedem"
dictionary["eight"] = "Esiem"
dictionary["nine"] = "Dziewiec"
dictionary["ten"] = "Dziesiec"

if (len(sys.argv) >= 2):
    number = str(sys.argv[1])
else:
    number = raw_input('Enter number from one to ten> ')

if number in dictionary:
    print "Polish translation for", number, "is: ", dictionary[number]
else:
    print "Number", number, "does not exist"

print dictionary.values()

print "Histogram"

hist = histogram("This is a string test")

printdict(hist)