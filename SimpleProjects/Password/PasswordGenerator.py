# import the random module
import random
import time 

print("Hello! Welcome to Password Generator!\n")
# setup list of characters we want in our password
character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$*.,;?()[]"
time.sleep(0.8) # a break before printing other statements

# Get the number of passwords and the required length wanted

number = 0
while number <= 0: # continue iteration until a positive number is received
    try:
        number = int(input("Enter the number of passwords you would like to generate (>= 1): "))
    except:
        continue

length = 0
while length <= 4: # continue iteration until a proper length is received
    try:
        length = int(input("Enter your password length (>=5): "))
    except:
        continue

print("\nHere are your passwords: ")
# Using a nested loop, we get passwords with randomly picked character
for num in range(number):
    password = ''
    for l in range(length):
        password += random.choice(character) # get a random character as part of the password
    time.sleep(0.5)
    print(password) # Password is created
