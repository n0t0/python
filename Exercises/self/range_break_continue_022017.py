## Range

a = ['Skip', 'the', 'candle', 'light']
for i in range(len(a)):
    print i, a[i]


range(10)
print range(10)
print range(5, 10)
print range(0, 10, 3)
print range(-10,0)

#   Loop searching for prime numbers
#   Break statement

for n in range(2,10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        #loop fell through without finding a factor
        print n, 'is a prime number'


#   Continue statement

for num in range(2,10):
    if num % 2 == 0:
        print 'found an even number', num
        continue
    print 'found a number', num

#   Pass statement
