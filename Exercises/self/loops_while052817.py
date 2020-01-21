for number in range(0,10):
    if number % 2 == 0:
        print '{x}'.format(x='Door is still open')
        continue

while '{x}' == True:
    print 'The dog can go out!'
    break

print '****'


door = (0, 1)

for num in door:
    if num == 0:
        print "Door is open!"
        print "Dog can escape."
    elif num == 1:
        print "Door is closed."
        break

## 06/12/2017
print '===='*40
print '||||'*40
print '===='*40

n = 4

while n < 4:
    print '{i}'.format(i='Bottle is full')
    n += 1


while '{i}' == True:
    print 'Bottle is still full'
    print 'Take one more sip'
    print n

    if n < 4:
        print '{i}'.format(i='Bottle is full')
        break


print '===='*40
print '||||'*40
print '===='*40

number = 4203
count = 0

while number != 0:
    count += 1
    number //= 10


print count

print '===='*40
print '||||'*40
print '===='*40
# 06/26/2017

mood = ['good', 'bad']

def emotion_detect():
    m = raw_input('How are you? ').lower()
    while m in mood:
        if m == 'good':
            print 'Glad you are good'
            break
        elif m == 'bad':
            print 'Take a pill'
            break
        else:
            continue
    else:
        print 'Unclarified emotion'

print emotion_detect()
