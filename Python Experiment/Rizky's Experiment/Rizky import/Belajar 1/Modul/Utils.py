import random, string

def random_string(n):
    key = 'F' + ''.join(random.choices(string.digits, k = n))
    return key