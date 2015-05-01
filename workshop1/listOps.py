#!/usr/bin/python
__author__ = 'nick'

#import list
fruits = ["Apple", "Orange", "Pear", "Banana", "Durian", "Grape"]

print "Executing for loop: for fruit in fruits"
for fruit in fruits:
    print fruit.upper(),

print ""
print "Executing for loop: for index in range(len(fruits))"
for index in range(len(fruits)):
    print fruits[index],

print""
print "String is immutable list"
fruit = "Orange"
for char in fruit:
    print char,

for index in range(len(fruit)):
    print fruit[index],

print ""
try:
    fruit[2] = "C"
except:
    print "Error in: fruit[2] = \"C\"", "String is immutable"

print "Slices: fruits[2:3] will show elements 2 and 3 but not 4"

print fruits[2:4]

print "Before pop(2):", fruits
fruits.pop(2)
print "After pop(2):", fruits

print "Before remove(2):", fruits
fruits.remove("Durian")
print "After remove(2):", fruits

print "Before sort:", fruits
fruits.sort()
print "After sort:", fruits

print "Before del:", fruits
del fruits
try:
    print "After del:", fruits
except:
    print "Error: variable fruits was deleted"
