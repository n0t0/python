items = ['a','b']

def insideOutside(items):
    '''This will add several items inside a fuction'''
    items.append([17,21])
    print 'Items added inside a fuction', items
    return

print insideOutside(items)
print items

## 05/29/17
print '****'

numbers = (4, 2)
print sum(numbers)

print '****'


def biggerThan(num):
    for n in range(num):
        if n < 5:
            print 'Number is less than 5 and number is: ', num
        elif n == 5:
            print 'Number is 5'
        else:
            print 'Number is bigger than 5'

print biggerThan(3)

print '===='*40
print '||||'*40
print '===='*40

def total(num1, num2):
    for n in sum(num1 + num2):
        if n <= 10:
            print 'Total is smaller than 10', sum
        elif n == 10:
            print 'Total is 10', sum
        else:
            print 'Total is something else', sum

print total(1, 2)
