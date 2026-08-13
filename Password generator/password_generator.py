import random
import string

def generate_password(length):
    # define characters
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # combine all characters
    all_characters = letters + digits + symbols

    # generate password
    password = ''.join(random.choice(all_characters) for i in range(length))

    return password

# user input
length = int(input("Enter password length: "))

# generate and print password
password = generate_password(length)
print("Generated Password:", password)