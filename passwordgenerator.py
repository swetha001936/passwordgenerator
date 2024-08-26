
import random

print("------PASSWORD GENERATOR------")

pwd_count=int(input("Enter the Number of password do you  needed :"))
pwd_chars=int(input("Enter the length of your  password :"))


password='''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&'''

print("\nThe Password is :-")
print("-----------------------")


for i in range(pwd_count):
    pwd=""
   
    for x in range(pwd_chars):
        pwd=pwd+random.choice(password)

    print("Password#"+str(i+1)+": "+pwd)    

print("-----------------------")
print("your password is successfully generated :) \n")