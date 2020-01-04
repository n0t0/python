## for Loops


for letter in 'Python':
    print "current letter is: ", letter

fruits = ['banana', 'apple', 'kiwi', 'raspberry']
for fruit in fruits:
    print 'current fruit is: ', fruit

#   else statement with Loops
print '****'

for num in range(10,20):
    for i in range(2,num):
        if num%i == 0:
            j=num/i
            print '%d equals %d * %d' % (num, i, j)
    else:
        print num,'is a prime number'

## 02/27/2017
print '****'

l = [2000, 15.3]

for num in l:
    if num >= 2000:
        print 'at down payment: ', num
    elif num >= 11.9:
        print 'and interest rate: ', num
    else:
        print 'you need more money'

print '****'

l1 = [(2001, 18.3)]

for (num1, num2) in l1:
    if num1 < 2000:
        print '$2000 Required minimum downpaymen'
        print num1, 'not enought'
    elif num2 >= 15.3:
        print 'Interest Rate is too high!!!', num2
    else:
        print 'Proceed to signing papers'

## 06/12/2017

print '===='*40
print '||||'*40
print '===='*40

train = 1,2,3,4,5,6

for name in train:
    value = name * 10

print value

print '===='*40
print '||||'*40
print '===='*40


for friend in ['Margon', 'Kevin', 'David']:
    invitation = 'Hi ' + friend + ' come and see me.'
    print invitation


for i in range(5):
    print i, 'is now: '


for i in range (13):
    print i, '\t', 2**i

for i in range(13):
    print i, '\t', i**2


i = 2

print i
print i*2
print 2**i
print 3**i


print '===='*40
print '||||'*40
print '===='*40


students = [("Gonzo", ["CompSci", "Physics"]),
            ("Justin", ["Math", "CompSci", "Stats"]),
            ("Ed", ["CompSci", "Accounting", "Economics"]),
            ("Margot", ["InfSys", "Accounting", "Economics", "CommLaw"]),
            ("Peter", ["Sociology", "Economics", "Law", "Stats", "Music"])]



for name, subjects in students:
    print name, '\t takes', '\t following classes', subjects



counter = 0

for name, subjects in students:
    for s in subjects:
        if s == 'CompSci':
            print name, '\t is taking \t', s
            counter +=1

print 'Number of students taking the following class: ', counter
