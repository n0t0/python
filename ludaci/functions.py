def hello(name, *args, **kargs):
    print name
    for k in kargs.iterkeys():
        print k, kargs[k]

hello('catwoman', 'asdf', 'asdf', 'asdjhkfl', test1='asdjfkh', test2='boza')

print '****' * 20

def hello(name, *args, **kargs):
    print name
    for k in kargs.iterkeys():
        if k == 'test1':
            print k, kargs[k]

hello('catwoman', test1='asdjfkh', test2='boza', boza='asdf')

print '****' * 20

def hello(name, *args, **kargs):
    print name
    for k, v in kargs.iteritems():
        if k.startswith('test'):
            print k, v

hello('catwoman', test1='asdjfkh', test2='boza', boza='asdf')
