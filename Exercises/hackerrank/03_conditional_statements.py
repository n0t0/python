print "Enter a number"
n = input()

# If 'n'
# If is odd, print Weird
# If is even and in the inclusive range of  to, print Not Weird
# If is even and in the inclusive range of  to, print Weird
# If is even and greater than, print Not Weird

# print(range(2, 6))

if (n % 2) == 0:
    if n in range(2, 6):
        print('Not Weird')
    elif n in range(6, 21):
        print('Weird')
    elif n > 20:
        print('Not Weird')
else:
    print('Weird')

# elif (n % 2) == 0:
#     # elif (n % 2) == 0 and n == range(2, 5):
#     print('Not Weird')
# # elif n % == range(6, 20, 2):
# #     print('Weird')
# elif n % 2 == 0 and n > 20:
#     print('Not Weird')
