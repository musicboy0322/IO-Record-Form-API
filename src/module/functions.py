import secrets
import string

def yield_random_identifier():
    characters = string.ascii_lowercase + string.digits
    identifier = ''
    for i in range(10):
        identifier += secrets.choice(characters)
    return identifier
