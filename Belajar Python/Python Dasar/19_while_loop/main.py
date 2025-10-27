# while loop

# while kondisi:
#     aksi sekian
#     aksi sekian
#
# akhir dari program

'''
program while akan terus berjalan jika kondisinya 'True'
'''

angka = 0
print(f"angka sekarang {angka}")

while angka < 5: # selama angka < 5, maka program while ini akan tetap menjalankan loopnya dan program dibawahnya akan terus berjalan juga sampai while menjadi False
    angka += 1 # saat kondisi while True berjalan sebanyak 1 kali, maka variabel angka akan bertambah 1, dari perintah while di atas, while akan False jika angka == 5, dan perintah while akan berhenti dari loopnya
    print(f"angka sekarang {angka}")
    print("otong ganteng maksimal!")
    
print("Cukup") # program ini akan berjalan jika program while di atas menjadi False, yaitu jika variabel angka == 5

