# Program lempar dadu

import random

while True:
    input("Tekan Enter untuk melempar dadu...")
    
    dadu = random.randint(1,6)
    print(f"kamu mendapatkan angka dadu {dadu}")

    ulang = input("ingin lempar dadu lagi? [y/n]: ").lower()
    if ulang != 'y':
        print("program lempar dadu selesai.")
        break


