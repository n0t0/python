## Formatting
print 'My name is %s and weight is %d kg!' % ('Zara,', 48)

print '===='

l = [1,0,5,10]

for num in l:
    if num == 10:
        print num

## 5/28/2017
print '****'

print 'This is going to make me %s!' % ('freak')

print "This {x} only a {y}. In this {y}, 'TEST' and 'IS' will be formatted.".format(x='is', y='test')

# 6/10/2017
print '='*80
print '|'*80
print '='*80

print 'Python formatting symbols:\n%s \n%d \n%f' % ('%s\t stands for string', 13.551251, 17.12412421)


print '='*80
print '|'*80
print '='*80

a = '%s\t Prints a String'
b = 13.477
c = 17.477

print 'Formatting Symbols:\n%s \n%d \n%f' % (a, b, c)


print '='*80
print '|'*80
print '='*80

print '{a},{b},{c}'.format(a='%s',b='%d',c='%f')
print '{a}, %c' % 'c'.format(a='%c stands for ')
print '%d' % 12.8
print '%g' % 124.41241
print '{a}, %d'.format(a='stands for Decimal') % 12.125125
