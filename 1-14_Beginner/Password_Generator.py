import random

print("Welcome to the password generator.")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

g_letters = int(input("How many letters would you like in your password?\n"))
g_symbols = int(input("How many symbols would you like?\n"))
g_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for _ in range(g_letters):
    password_list.append(random.choice(letters))
for _ in range(g_symbols):
    password_list.append(random.choice(symbols))
for _ in range(g_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your password is {password}")
