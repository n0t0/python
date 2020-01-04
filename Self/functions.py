## Functions

def printme(str):
    """
    This prints a passed string into this function
    """
    print str
    return
print printme("I'm first call to user defined function!")
print printme("Again second call to the same function")

## Pass by Reference vs Value
print '****'

def changeme(mylist):
    """
    This changes a passed list into this function
    """
    mylist.append([1,2,3,4])
    print "Value inside the function: ", mylist
    return

mylist = [10,20,30]
print changeme(mylist)
print "Value outside the function: ", mylist

####
print '****'

def printinfo(name, age):
    """
    This prints a passed info into this function
    """
    print 'Name: ', name
    print 'Age: ', age
    return

print printinfo(age=50, name='Nick')


## Lambda Functions

sum = lambda arg1, arg2: arg1 + arg2

print 'Value of total: ', sum(10, 20)
print 'Value of total: ', sum(20, 20)
