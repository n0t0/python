## Lambda Function

import math

def square_root(x):
    return math.sqrt(x)

print square_root(4)

square_root = lambda x: math.sqrt(x)

print square_root(9)

sum = lambda x, y: x+y # def sun(x+y): return x + y

print sum(20,12)
