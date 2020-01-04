x = [20, 30, 40]
y = []

for v in x:
    y += [v * 2]
assert x == [20, 30, 40]
assert y == [40, 60, 80]


x = [2, 3, 4]
y = [v * 2 for v in x]

x = [2, 3, 4]
y = map(lambda v: v * 2, x)
print(y)
