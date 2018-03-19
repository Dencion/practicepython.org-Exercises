import random
import string

def passwordGenerator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

passwordLength = int(input("How long would you like your password to be?"))
print(passwordGenerator(size=passwordLength))
