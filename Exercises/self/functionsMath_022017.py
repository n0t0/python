#### Functions

# High school Algebra functions

def f(x):
    return 3 * x ** 2  - 2 * x + 5

print f(2)
print f(5)
print f(-1)

print '='*80
print '|'*80
print '='*80


def fib(n):
    """
    Print Fibonacci series up to n.
    """
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b


print fib(45)

## Return Statement
print '****'

def sum( arg1, arg2 ):
    # Add both parameteres and return them
    total = arg1 + arg2
    print 'Inside the function: ', total
    return total

total = sum(10, 20)
print "Outside the function: ", total

####
print '****'

def sumProblem(x, y):
    """
    Display any number of sum problems with functions.
    """
    sum = x + y
    sentence = 'The sum of {} and {} is {}.'.format(x,y, sum)
    print(sentence)

print sumProblem(6, 5)

####
print '*****'

def mainMath():
    sumProblem(2,4)
    sumProblem(123,321)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    sumProblem(a,b)

print mainMath()
