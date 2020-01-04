l1 = [8, 8, 8, 10]
l2 = [10 + 10]


l1.count(1)
l1.append(20)

print (l1)

l1.reverse()
l1.remove(8)
l1.remove(8)

print (l1)

lst1 = [1,2,3]
lst2 = [7,0,'o']

print cmp(lst1, lst2)
print max(lst2)
print max(l1)
print min(lst1)

## Local vs. Global

money = 2000
def addMoney():
    money = money + 1
