# Continue, pass, break
# continue, pass

'''
pass --> dia berfungsi sebagai dummy, tidak akan dieksekusi
'''

angka = 0 # nilai awal dari variabel 'angka'

# while angka < 5: # while akan terus melakukan loop selama angka < 5. 
#     angka += 1 # setiap while melakukan loop, maka nilai variabel angka akan bertambah +1
#     if angka == 3: # perintah if tambahan, jika nilai dalam variabel angka adalah 3, maka akan menjalankan program if ini
#         print("check") # aksi dari program if di atas, perintah ini akan print kata 'check' di atas angka 3
#     print(f"Nilai angka {angka}") # print setiap angka yang keluar dari perulangan while

while angka < 6:
    angka += 1
    if angka == 3:
        pass # ini tidak akan dieksekusi, ada tetapi tidak dianggap
    print(f"Nilai angka {angka}")


'''
continue --> jika digunakan, maka perintah di bawahnya tidak akan dieksekusi karena 'continue' akan langsung kembali ke awal loop
''' 

while angka < 12: 
    angka += 1
    print(f'Angka sekarang {angka}') # aksi 1
    if angka == 10:
        print("Nice!!")
        continue # akan membuat loop loncat ke step loop berikutnya, atau akan melewati atau skip aksi di bawahnya (dalam kasus ini print("Whassup!!")) jika kondisi if nya terpenuhi
    
    print("Whassup!!") # aksi 2
    
print("Program selesai")

'''
seluruh while adalah loop utamanya, dan continue adalah loop kecilnya
'''