

symbol = [1,'s']

for s in symbol:
    if s == '%s':
        print 'This is a string'
    else:
        print 'This is an integer'

## 06/12/2017
print '===='*40
print '||||'*40
print '===='*40

def f1():
    print 'Schupeno'


def f2():
    f1()
    print 'Pironche'


def f3():
    print 'Bonche'
    f2()


def f4():
    print 'Onche'
    f3()

print f4()


print '===='*40
print '||||'*40
print '===='*40
# 06/26/2017

def func1():
    num = raw_input('Enter a number: ')
    print 'Nice'


number = str(func1())


def func2(func1):
    for n in number:
        if number == 4:
            print 'Lucky you'
        elif number < 4:
            print 'Number is less than 4', number
        elif number > 4:
            print 'Number is bigger than 4', number


print func2(func1)


print '===='*40
print '||||'*40
print '===='*40

emotion = ['agressive', 'amazed']

def func3():

    e = raw_input('emotion: ')
    if e in emotion:
        print e
    else:
        print 'emotion not in the list'

print func3()

#mood = str(func3(emotion)
