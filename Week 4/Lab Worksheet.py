import math

print(math.sqrt(2401))

print(math.log2(1024))


def displayTwice():
    '''Prints a message to the user twice.'''
help(displayTwice)
def displayTwice(msg):
    print(msg)
    print(msg)
print(displayTwice("Hi"))



def findMax(a,b):
    """Finds the maximum of two values."""
    if ( a > b ):
	    max = a
    else:
	    max = b
    return max
print(findMax(2,5))


def numMultiplication(a,b):
    '''Multiplies to numbers together.'''
    a = input("Input a value.")
    a = int(a)
    b = input("Input a second value.")
    b = int(b)
    if b == "":
        print(numMultiplication(a*a))
    else:
        print(numMultiplication(a*b))


def someFunc(x, y, z):
	print("x is", x, "\ny is", y, "\nz is", z)
someFunc(y=5, z=7, x=3)


print("1", "2", "3", "4", sep=',')




def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total/len(numbers)
print(calcAve(2,5))


hypot = lambda a,b : math.sqrt(a * a + b * b)
print(type(hypot))


to_seconds = lambda a, b: a * 3600 and b * 60
print(to_seconds(1, 30))