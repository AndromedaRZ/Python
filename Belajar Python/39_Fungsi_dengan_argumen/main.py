# Fungsi dengan argumen (input)

# dalam kurung setelah definition fungsi, disebut parameter atau ada yang menyebutnya juga sebagai input atau argumen
'''
def nama_fungsi(argumen): 
    print("Hello World")
'''

def hello_world(nama):
    '''fungsi hello world menerima input dengan variabel nama'''
    print(f'Selamat datang dunia wahai {nama}')
    
hello_world("rizky") # jika kita mengisi parameter atau argumennya, maka isinya akan masuk ke dalam functionnya
hello_world("Yusuf")

# program tambah

def tambah(angka_1, angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")
    
tambah(1,5) # jika kita menyesuaikan isi parameter atau argumennya, maka kita bisa memanfaatkan function yang kita buat di atas

def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy() 
    for peserta in data_peserta:
        print(f'Yang terhormat {peserta}')
    
anggota_boyband = ['ucup', 'doni', 'jibril']

say_hi(anggota_boyband)
