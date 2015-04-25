#!/usr/bin/python

index = 5
while index > 0:
    print "While loop index:", index
    index -= 1

while True:
    print "Infinite while loop: \"while True\""
    print "End loop [y]?"
    userInput = raw_input("$ ")
    if userInput == "y":
        break
    print "You entered:", userInput

print "\"while True\" ended using break statement"
