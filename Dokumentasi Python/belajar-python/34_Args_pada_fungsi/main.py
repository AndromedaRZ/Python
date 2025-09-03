'''*args'''

# memasukkan data/argument

def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg")

fungsi("ucup", 170, 60)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg")

fungsi(['otong', 160, 45]) # karena pada fungsi di atas kita menggunakan data list untuk menyimpan datanya
# maka ketika kita memanggil fungsi tersebut kita perlu menambahkan tanda kurung siku

# berikutnya adalah penggunaan dari *args, *args ini bisa berarti 'banyak argument'
# *args ini adalah sebuah konvensi, kita bisa menggunakan nama lain selain args


def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg")

fungsi('dudung', 180, 80)

# studi kasus

def tambah(*data):
    '''fungsi tambah dengan *args'''
    # tipe data pada *data adalah tuple
    # kita bisa melakukan iterasi pada *data
    # karena tipe data dari *data adalah tuple
    # maka kita bisa menggunakan for untuk melakukan iterasi pada *data
    output = 0
    for angka in data:
        output += angka

    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"Hasil = {hasil}")

print(f"Hasil = {tambah(10,5,15)}")