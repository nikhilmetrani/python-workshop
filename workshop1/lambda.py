__author__ = 'nick'

print "List of lambda expressions"
listLambda = [(lambda x: x**2), (lambda x: x**3), (lambda x: x**4)]

for expression in listLambda:
    print expression(2)

print "dictionary of lambda expressions"

lambdaDict = dict()

lambdaDict["Square"] = (lambda x: x**2)
lambdaDict["Cube"] = (lambda x: x**3)
lambdaDict["Quadruple"] = (lambda x: x**4)

print lambdaDict["Square"](8)

print "Closure and scope of lambda expressions"

def multiplyby(number):
    return (lambda x: x*number)

twotimes = multiplyby(2)
threetimes = multiplyby(3)
ninetimes = multiplyby(9)

print "twotimes(9):", twotimes(9)
print "threetimes(9):", threetimes(9)
print "ninetimes(9):", ninetimes(9)