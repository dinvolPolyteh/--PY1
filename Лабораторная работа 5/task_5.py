from random import sample
import string

def get_random_password(n: int = 8) -> str:
    password_chars = string.ascii_letters.join(string.digits)
    return ''.join(sample(password_chars,n))


print(get_random_password())
