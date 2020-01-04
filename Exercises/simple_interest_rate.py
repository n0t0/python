#### Math

#### Calculating Interest Rate

#   Simple Formula = P (principal) x I (annual interest rate) x N (years)

#   Borrowing $1,000 at 6% (annual interest rate) for 8 months

print (1000*0.06*8/12)

print (15*12)

print 5.0/2

print '===='

l1 = [(1900, 15.7)]

for (num1, num2) in l1:
    while num1 < 2000 and num2 > 15.7:
        print '$2000 Required minimum downpayment'
        print num1, 'not enought'
        print 'Interest Rate too high!!!', num2
        break
    if num1 > 2000:
        print num1
    elif num2 < 15.7:
        print num2
    else:
        print 'Proceed to signing papers'
        print "With downpayment of: ", num1
        print "At rate of: ", num2

        break

interest_rate = (num1, num2)

print "===="

count = 2001
while True:
    print count
    if count < 3000:
        break








print "===="

def interest_rate(num1, num2):
    number = 0
    while number > 2000 or number < 15.7:
        number = int(input("Please enter a number: "))
        if number < 2000:
            print number, 'not enough'
        elif number < 15.7:
            print number, 'procentice too high'
        else:
            print 'signiture please'

#print interest_rate()
