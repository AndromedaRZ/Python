# Latihan perulangan membuat segitiga

sisi = 10

# 1. Menggunakan for
# dummy variabel
print("Awal for")
count = 1
for i in range(sisi): # for i sebanyak yang ada di dalam variabel sisi
    print("*"*count) # string "*" akan dikalikan sebanyak nilai yang ada di variabel count
    count += 1 # setiap perulangan jumlah nilai variabel count akan bertambah 1
    # yang artinya setiap perulangan akan menghasilkan print yang berbeda karena jumlah count akan berbeda setiap perulangannya
print("Akhir for\n")


# 2. Menggunakan while

print("Awal while")
count = 1

while True: 
    print("*"*count) # karena di atas terdapat indentasi while maka perintah ini akan terus dieksekusi
    count += 1 # nanti string "*" akan bertambah seiringnya perulangan yang terjadi
    if count > sisi: # dan ketika jumlah count ataupun jumlah "*" sudah melebihi variabel sisi 
        break # maka perintah break ini akan terkesekusi sehingga mengentikan looping dan keluar dari while
    
print("Akhir while\n") # lalu langsung menjalankan perintah yang ada di bawahnya
    
# 3. Hanya ganjil saja
    
print("Awal ganjil")
count = 1
while True: # hampir mirip seperti perintah sebelumnya
    if count % 2: # jika jumlah count tidak habis dibagi modulus 2 (berarti count adalah bilangan ganjil)
        print("*"*count) # maka akan terprint "*"
        count += 1 # lalu jumlah count ditambah 1
    else: # tetapi jika jumlah count habis dibagi modulus 2 (kali ini jika count adalah bilangan genap)
        count += 1 # maka hanya ada perintah untuk menambah jumlah count sebanyak 1
        continue # dan langsung lanjut ke perulangan berikutnya
        
    if count > sisi: # sampai jumlah count lebih besar dari variabel sisi
        break # maka akan tereksekusi perintah untuk menghancurkan perulangannya
    
print("Akhir ganjil\n")

# 4. Hanya ganjil saja dan dibuat seperti piramida

print("Awal piramida ganjil")
count = 1
spasi = int(sisi/2) # nilai sisi akan dibagi 2 dan dibulatkan dengan integer lalu dimasukkan ke dalam variabel spasi

while True: # hampir sama seperti perintah di atas hanya saja ada sedikit perbedaaan
    if count % 2:
        print(" "*spasi, "+"*count) # spasi juga akan ikut ter-print
        spasi -= 1 # tetapi akan dikurangi 1 setiap kali tereksekusi
        count += 1 # sehingga membuat hasilnya seperti piramida
    else:
        count += 1
        continue
    
    if count > sisi:
        break
    
print("Akhir piramida ganjil")