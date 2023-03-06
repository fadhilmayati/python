# Created by Fadhil Mayati
# Date 26 February 2023

import sys
import string
import random

def generate_password(length, special_chars):
    # Define the character set to use for the password
    chars = string.ascii_letters + string.digits
    if special_chars:
        chars += string.punctuation

    # Generate the password
    password = ''.join(random.choice(chars) for i in range(length))
    return password

# Get user input
length = int(sys.argv[1])
special_chars = sys.argv[2].lower() == 'y'

# Generate the password
password = generate_password(length, special_chars)

# Print the password
print("Your password is:", password)

