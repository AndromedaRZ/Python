# **kwargs pada fungsi
'''keyword args'''

def fungsi(nama, tinggi, berat):
    '''fungsi biasa'''
    print(f'Nama = {nama}, Tinggi = {tinggi}, Berat = {berat}')
    
fungsi("Vince", 190, 80)

# penggunaan kwargs, kwargs menggunakan dua simbol bintang pada kalimat depannya dan hasil dari kwargs adalah berupa dictionary
def fungsi(**kwargs):
    '''fungsi kwargs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f'Nama = {nama}, Tinggi = {tinggi}, Berat = {berat}')
    
fungsi(nama="ucup", tinggi=165, berat=50)

# studi kasus

def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    elif kwargs["option"] == "kurang":
        for angka in args:
            output -= angka
    elif kwargs["option"] == "bagi":
        output = 1
        for angka in args:
            output /= angka
    else:
        print("operasi tidak valid")
    
    return output

hasil = math(1,3,5,option="tambah")
print(f"hasil jumlah {hasil}")
hasil = math(1,3,5,option="kali")
print(f"hasil kali {hasil}")
hasil = math(1,3,5,option="kurang")
print(f"hasil kali {hasil}")
hasil = math(1,3,5,option="bagi")
print(f"hasil kali {hasil}")