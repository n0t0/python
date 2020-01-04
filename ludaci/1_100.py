"""
Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary
numbers as its input
and then check whether they are divisible by 5 or not. The numbers that are
divisible by 5
are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

"""

# seq = input('Enter a comma separated 4 digit binary numbers: ').split(',')

# # print([number for number in seq if int(number, 2) % 5 == 0])
# print([number for number in seq if int(number, 2) % 5 == 0])

# # for number in seq:
# #     if (int(number, 2 ) % 5 == 0 ):
# #         print(number)


"""

Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both
included)
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a
single line.

"""

# print([number for number  in range(1000,3001) if number % 2 == 0])

# result = []

# for number in range(2000, 2021):
#     result.append(str(number))

# even_numbers = []

# for x in result:
#     odd_found = False
#     for i in x:
#         if int(i) % 2 != 0:
#             odd_found = True
#     if odd_found:
#         continue
#     even_numbers.append(x)

# print(even_numbers)

"""

Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

# digit = input('Enter a value: ' )

# result = []
# for a in range(1,5):
#     result.append(a)

# for n, i in enumerate(result):
#     if i == 1:
#         result[n] = digit
#         result[n+1] = digit*2
#         result[n+2] = digit*3
#         result[n+3] = digit*4

# x = [int(a) for a in result]
# print(sum(x))

"""

Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is
input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

"""
# seq = input('Enter a seq of comma-separated numberts: ').split(',')

# result = [x for x in seq if int(x) % 2 !=0]
# print(','.join(result))

"""

Question:
Write a program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format
is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

"""

# print("Enter/Paste your content. Ctrl-D to save it.")
# contents = []
# while True:
#     try:
#         line = input()
#     except EOFError:
#         break
#     contents.append(line)
#     # 'Choose transaction {} or {} and amount {x}\n'.format('D', 'W', x))

# print(contents)

# D = [int(i[1:]) for i in contents if i[0] == 'D']
# W = [int(i[1:]) for i in contents if i[0] == 'W']

# NET = [n - m for n, m in zip(D, W)]
# print(NET)

"""
Question 18
Level 3

Question:
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords 
and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

Hints:
In case of input data being supplied to the question, 
it should be assumed to be a console input.
"""

import string

print("Enter your password. Ctrl-D to save it.")
passwords = []
while True:
    try:
        password = input()
    except EOFError:
        break
    passwords.append(password)

print(passwords)

for i in passwords:
    c = i.split(',')
    print(c)

    # if i == string.ascii_lowercase:
    # print(i)


def pass_check(string):
    pass
