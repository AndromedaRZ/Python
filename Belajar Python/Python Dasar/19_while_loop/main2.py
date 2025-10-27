# contoh soal while loop

import time

# Proram pertama
# Print angka 1 sampai 5
print("\n===Program pertama===")
i = 1 # nilai awal dari variabel 'i'
while i <= 5: # selama nilai i <= 5, maka while akan tetap True dan loop akan tetap berjalan
    print(f"Nilai i adalah {i}") # print nilai saat ini dari variabel 'i'
    i += 1 # saat perulangan berjalan 1 kali, nilai dalam variabel 'i' akan bertambah +1 

# Program kedua
# Hitung mundur dari n ke 1
print("\n===Program kedua===")
n = int(input("Masukkan n: ")) # meminta user untuk memasukkan nilai darimanakah hitung mundurnya dimulai
print("Hitung mundur dimulai dalam...")
while n >= 1: # selama variabel n >= 1, maka while akan terus melakukan perulangan dan terus menjalankan program di bawahnya
    print(n)
    time.sleep(1) # akan melakukan jeda selama 1 detik sebelum ke perintah di bawahnya
    n -= 1 # selama proses perulangan, nilai dalam variabel 'n' akan berkurang -1
    
print("Hitung mundur selesai") # perulangan while akan berhenti jika n < 1 dan perintah ini pun akan berjalan karena while sudah keluar dari perulangannya atau loopnya





