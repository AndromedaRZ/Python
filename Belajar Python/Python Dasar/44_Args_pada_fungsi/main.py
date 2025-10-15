# *args pada fungsi

# memasukan data/argument

def fungsi(nama, tinggi, berat):
    print(f"nama = {nama}, tinggi = {tinggi}, berat = {berat}")
    
fungsi("rizky", 160, 40)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"nama = {nama}, tinggi = {tinggi}, berat = {berat}")

# jika kita ingin memakai list di dalam fungsi maka perlu menaruh kurung persegi didalam fungsi yang sedang kita jalankan
fungsi(["Ucup", 170, 56])

# menggunakan args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"nama = {nama}, tinggi = {tinggi}, berat = {berat}")

# *args hampir mirip saat kita menggunakan list, tetapi saat pemanggilan fungsinya kita tidak perlu menambahkan kurung persegi lagi
fungsi("Doni", 180, 75)

# studi kasus menggunakan *args

# dalam *args, tidak harus menggunakan argumen args, bisa dengan argumen lain seperti contoh di bawah ini
def tambah(*data):
    # tipe data (data) adalah tuple dan ia bisa diiterasi
    output = 0
    for angka in data:
        output += angka
        
    return output

hasil = tambah(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"hasil = {hasil}")

hasil = tambah(5, 5, 10)
print(f"hasil = {hasil}")