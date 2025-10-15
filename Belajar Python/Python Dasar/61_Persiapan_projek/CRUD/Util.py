import random
import string

def random_string(panjang:int) -> str:
    strings = ''.join(random.choice(string.ascii_letters) for i in range(6))
    return strings