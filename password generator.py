from random import randint
my_password = ''
num = input('enter the numbers of your new password')
num = int(num)
for x in range(num):
    my_password += chr(randint(33,126))

c = type(my_password)
print(c)
print(my_password)
#p8r*6n\b