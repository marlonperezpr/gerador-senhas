import random
import string

min_length = 8
max_length = 16
use_uppercase = True
use_numbers = True
use_special_chars = True

chars  = string.ascii_letters + string.digits + string.punctuation

password = ''

for _ in range(random.randint(min_length, max_length)):
    password += random.choice(chars)

if use_uppercase and not any(c.isupper() for c in password):
    print("Senha não possui letras maiúsculas")
    exit()

if use_numbers and not any(c.isdigit() for c in password):
    print("Senha não contém números")
    exit()

if use_special_chars and not any(c in string.punctuation for c in password):
    print("Senha não contém caracteres especiais")
    exit()

print("senha gerada: ", password)