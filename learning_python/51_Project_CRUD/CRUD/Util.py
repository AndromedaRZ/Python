import random, string

def random_string(panjang: int) -> str:
    hasil = ''.join(random.choice(string.ascii_letters) for i in range(6)) # untuk generate prime key random
    return hasil