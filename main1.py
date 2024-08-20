import random
import string 

pass_len = 10
Charvalues = string.ascii_letters + string.digits + string.punctuation

password =""
for i in range(pass_len):
    password += random.choice(Charvalues)

print("Your Password is :",password)