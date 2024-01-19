import random

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = upper_case.lower()
digits = "1234567890"
symbols = "!@#$%^&*()_+={}?/.<>,|\? "

upper,lower,nums,sym = True, True, True, True
all = " "

if upper:
    all += upper_case
if lower:
    all += lower_case
if nums:
    all += digits
if sym:
    all += symbols
    
length = 20 
amount = 10 

print("These are the list of passwords you can choose from!: \n")
for x in range(amount):
    password = "".join(random.sample(all, length)) #here we are using all the characters mentioned 
                                                    #and mentioned the length for the password
    
    print(password)
    