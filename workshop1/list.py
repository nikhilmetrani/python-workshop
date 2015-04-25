#!/usr/bin/python

fruits = ["Apple", "Orange", "Pear"]
print "A list of fruits:", fruits

numbers = [90, 78, 39]
print "A list of numbers:", numbers

nothing = []
print "An empty list:", nothing

print "List is mutable!"
print fruits
print "fruits[1]=\"Durian\""
fruits[1] = "Durian"
print "After:", fruits

print "Negative index means count from end!"
print "fruits[2] = fruits[-1]"
print fruits[2], "=", fruits[-1]

print "Membership test"
print "\"Durian\" in fruits:",
print "Durian" in fruits
print "\"Banana\" in fruits:",
print "Banana" in fruits
