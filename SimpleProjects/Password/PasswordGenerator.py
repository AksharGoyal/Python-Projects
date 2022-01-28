# import the random module
import random

print("Hello! Welcome to Password Generator!")
# setup list of characters we want in our password
character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$*.,;?()[]"

# Get the number of passwords and the required length wanted
number = int(input("Enter the number of passwords you would like to generate: "))
while number <= 0:
    number = int(input("Enter the number of passwords you would like to generate (>= 1): "))
length = 0
while length <= 4:
    length = int(input("Enter your password length (>=5): "))

print("\nHere are your passwords: ")

# Using a nested loop, we get passwords with randomly picked character
for num in range(number):
    password = ''
    for l in range(length):
        password += random.choice(character)
    print(password)