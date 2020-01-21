#### Build-In Functions

#   Lenght Function

print len('This is a sentence')

l1 = [1,2,3,4]
l2 = [1,2,3,4,4,5,6]
l3 = [1,2,3,4,4,4,5,5,6]

print len(l2)
print len(l1 + l2 + l3)

print "*******"

start = 2
end = 20
for num in range(start, end, 2):
    print num

print "*******"

for num in range(0,40):
    if num % 2 == 0:
        print num
    else:
        print 'Odd number!'

## 05/28/17
print '****'

s = 'This is only a test'

print s.split()[0]
