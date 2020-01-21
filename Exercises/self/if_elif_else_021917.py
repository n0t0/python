## Decisions

# if Statement

var = 100
if var == 200:
    print '1 - got a true expression value'
    print var
elif var == 150:
    print '2 - got a true expression value'
    print var
elif var == 100:
    print '3 - got a true expression value'
    print var
else:
    print '4 - got a false expression value'

# Nesting if, elif, else statements
print '****'

var = 100
if var < 200:
    print 'expression value is less that 200'
    if var == 150:
        print 'which is 150'
    elif var == 100:
        print 'which is 100'
    elif var == 50:
        print 'which is 50'
elif var < 50:
    print 'could not find true expression'

print 'Good Bye'

# for Statement
print '****'

words = ['word', 'door', 'house']
for w in words:
    print w, len(w)

print "===="

# change this code

number = 16
second_number = 10
first_array = [1]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 3:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
