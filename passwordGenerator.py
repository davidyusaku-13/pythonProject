import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+"

length = int(input("Password Length: "))

password = ""
for i in range(length):
	password += random.choice(chars)

print(password)