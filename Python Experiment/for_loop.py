# Program lempar dadu menggunakan for n in range()

import random

# Minta jumlah lemparan dari user
jumlah_lempar = int(input("Mau lempar dadu berapa kali? "))

# Loop sebanyak jumlah lemparan
for i in range(jumlah_lempar):
    hasil = random.randint(1, 6)
    print(f"Lemparan ke-{i+1}: 🎲 {hasil}")