#Random password generator

import random
import string

# print(string.ascii_letters)
# print(string.digits)

pass_len = 12

charValues = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(pass_len):
    password += random.choice(charValues)

print("your password string is : ",password)





