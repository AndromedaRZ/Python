# perulangan

# perulangan atau (loop) adalah cara untuk menjalankan kode yang sama berulang-ulang
# dengan menggunakan perulangan, kita bisa menghemat waktu dan membuat kode lebih efisien
# daripada menulis kode yang sama berkali-kali

'''for loop'''
# digunakan untuk mengulang sejumlah kode tertentu atau mengiterasi melalui sekumpulan data
# biasanya menggunakan function range() untuk membuat urutan angka untuk perulangannya

# mencetak angka 0 sampai 4
for i in range(5):
    print(i) # maksud i disini adalah index
    # function range() kita isi dengan angka 5
    # artinya kita mengulang sebanyak 5 kali
    # dan perintah print akan jalan sebanyak 5 kali
    # sehingga hasilnya adalah index 0, 1, 2, 3, dan 4
    
# mencetak angka 1 sampai 5
for i in range(1, 6): # range(<dari index ke->, <sampai index ke->)
    print('range', i)
    
# menampilkan "Hello" sebanyak 3 kali
for i in range(3):
    print("Hello")
    
# menghitung mundur
for i in range(5, 0, -1): # range(<dari index ke->, <sampai index ke->, <jarak>)
    print('turun', i)
    
for i in range(1, 100, 10): # contoh lain
    print(i)
    
    
# for loop juga bisa mengiterasi karakter dalam string
nama = 'Python'

for huruf in nama:
    print(huruf)
    

kata = input("Masukkan kata: ")
print('Huruf-huruf dalam kata')

for huruf in kata:
    print(huruf)
    
'''while loop'''
# while loop akan mengulang kode selama kondisi tertentu masih True
# jika kondisinya berubah menjadi False, maka perulangan pada 'while loop' akan berhenti

# mencetak angka 1 sampai 5
angka = 1
while angka <= 5:
    print(angka)
    angka += 1 # jika kita tidak membuat angkanya bertambah
    # maka variabel angka akan tetap bernilai kurang dari 5 dan perulangan akan terus terjadi
    # sehingga menyebabkan infinity loop
    
    # pada saat kita melakukan infinity loop
    # kita bisa menekan ctrl + c untuk berhenti dari infinity loop pada terminal
    
# input sampai benar
password = ''
while password != '123':
    password = input("Masukkan password: ")
    if password != '123':
        print("Password salah, coba lagi!")
        
print("Password benar")
# baris program di atas akan tetap mengulang jika kita selalu memasukkan password yang salah

'''break dan continue'''
# break digunakan untuk menghentikan perulangan, meskipun kondisinya masih True
# continue digunakan untuk membuat agar kode melanjutkan ke iterasi berikutnya (dalam perulangan, continue digunakan untuk melewati perulangan saat ini dan langsung melanjutkan untuk perulangan berikutnya)

# break
angka_rahasia = 7
while True:
    tebakan = int(input("Tebak angka: "))
    
    if tebakan == 7:
        print('Selamat, anda benar!')
        break # break akan langsung menghentikan looping (perulangan)
    else:
        print('Salah!, coba lagi.')
        
# continue
# mencetak hanya angka ganjil
for i in range(10):
    if i % 2 == 0:  # Jika i memunculkan angka genap
        continue    # Lewati, lanjut ke angka berikutnya
    print(i)        # Hasilnya hanya akan mencetak angka ganjil
    
# break berguna untuk menghentikan perulangan, sedangkan continue hanya akan melewati perulangan saat ini dan lanjut ke perulangan berikutnya

'''loop dengan else'''
# loop pada Python bisa memiliki clause else yang dieksekusi jika loop selesai secara normal (tidak dengan break)

# contoh
# mencari huruf dalam kata
kata = input('Masukkan kata: ')
huruf_dicari = input("Masukkan huruf yang dicari: ")

for huruf in kata:
    if huruf == huruf_dicari:
        print(f"Huruf {huruf_dicari} ditemukan dalam kata!")
        break
else:
    print(f"Huruf {huruf_dicari} tidak ditemukan dalam kata!")
    
'''loop dengan while'''
# mencari password yang benar dengan batas percobaan

password_benar = '123'
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    password = input("Masukkan pasword: ")
    percobaan += 1
    
    if password == password_benar:
        print("Login berhasil")
        break
    else:
        print("Password salah, sisa percobaan", max_percobaan - percobaan)
else:
    print("Terlalu banyak percobaan gagal, akses ditolak!")
     
     
'''perulangan bersarang (nested loop)'''
# kita bisa menempatkan perulangan di dalam perulangan

print("Tabel perkalian 1-5:")
for i in range(1, 6):
    for j in range(1, 6):
        hasil = i * j
        print(f"{i} x {j} = {hasil}")
    print("======")