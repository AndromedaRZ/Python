# exception terjadi saat program mengalami error  saat runtime atau saat program dijalankan

from math import nan

# input_user = int(input('Masukan angka: '))
# hasil = nan

# try: # jika tidak mengalami runtime error maka program ini akan tetap berjalan dan lanjut secara normal
#     hasil = 10 / input_user
    
# except: # jika mengalami runtime error, maka program ini akan berjalan dan tidak lanjut ke program berikutnya
#     print('input tidak boleh 0')
    
# print(f'hasil = {hasil}')

# contoh aplikasi
while (True):
    angka = int(input('Masukan angka pembagi: '))
    try:
        hasil = 10 / angka
        print(f'hasil = {hasil}')
        isDone = input('Lanjutkan? [y/n]: ')
        if isDone == 'n':
            break
    except:
        print('Pembagi nol, silahkan input ulang angka pembagi')
        
print('Program ke-1 selesai')

# contoh aplikasi untuk membuat file data.txt
try:
    with open('data.txt', 'r') as file:
        print(file.read())
except:
    print('file data.txt tidak dapat ditemukan, membuat file baru')
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.write('file baru')
            
            
print('Program ke-2 selesai')

