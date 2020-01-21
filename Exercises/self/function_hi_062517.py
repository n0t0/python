database = ['Mila', 'Maya', 'Maria']

def hi():
    name = raw_input('Enter your name: ')
    if name in database:
        print 'Hello'
    else:
        print 'New user'
        print 'Hi ' + name + ' Nice to meet you'

print hi()
