'''
5) TYPEHINTS PADA FUNGSI

Typehints adalah cara memberi petunjuk tipe data yang kita ingin untuk parameter dan hasil return suatu fungsi, ini juga berguna jika ada orang lain melihat kode kita agar tau tipe data yang kita inginkan dari input argumen suatu fungsi
'''

# cara menggunakan typehints
# kita bisa memasukan type hints disebelah kanan parameter dengan menambahkan titik dua (:) seperti contoh berikut

def pangkat_dua(angka:int): # di sebelah kanan parameter, kita tambahkan type hints dengan menambahkan titik dua (:) dan tipe data dari input yang nanti dimasukan user, dalam kasus ini, kita memberitahu bahwa inputnya harus bertipe data integer
    '''fungsi untuk mempangkatkan 2 suatu bilangan'''
    output = angka ** 2
    return output

hasil = pangkat_dua(5)
print(f"5^2 = {hasil}")

def say_hi(nama:str): # pada fungsi ini, kita memberitahu bahwa inputnya harus bertipe data string
    '''fungsi untuk mengucapkan salam'''
    print(f"Selamat pagi {nama}")
    
say_hi("Rizky")

# jika kita input tipe data selain yang kita inginkan, programnya akan tetap berjalan normal karena fungsi typehints hanyalah memberi petunjuk
say_hi(12)

'''
selain petunjuk untuk input yang kita inginkan, kita juga bisa memberi petunjuk untuk output yang kita inginkan dengan cara menambahkan tanda panah (->) lalu memasukan tipe data yang kita inginkan pada bagian kanan parameter seperti contoh di bawah ini
'''
def pangkat_dua(angka:int) -> int:
    '''fungsi untuk memangkatkan dua suatu bilangan'''
    output = angka ** 2
    return output

print(f"4^2 = {pangkat_dua(4)}")