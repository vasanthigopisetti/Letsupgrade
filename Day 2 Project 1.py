import random as r

import string

length = 8

otp = ''

characters = string.ascii_letters + string.digits 
print(characters)

for i in range (length):

 otp = otp + r.choice(characters)

print("OTP:", otp)
