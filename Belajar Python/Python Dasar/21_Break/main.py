# Break

import time

data_int = int(input("Hitung sampai = "))
angka = 0

while True:
     angka += 1
     time.sleep(1) # function time.sleep() ini akan memberikan jeda sebelum menjalankan baris program berikutnya selama 1 detik
     print(f"Angka sekarang {angka}")
     if angka == data_int:
         print("Nice!!!")
         break # Perintah 'break' ini akan langsung mengentikan loop dari while apapun yang terjadi
     print("Wassup!!")

print("Program selesai")

