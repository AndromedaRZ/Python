'''**kwargs (Keyword Arguments)'''

def fungsi(nama, tinggi, berat):
    '''fungsi biasa'''
    print(f"{nama} punya tinggi {tinggi} cm dan berat {berat} kg")

fungsi("ucup", 180, 60)

def fungsi(**kwargs):
    '''fungsi kwargs'''
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="ucup", tinggi=180, berat=60) # menjadi dictionary

# studi kasus

def math(*args, **kwargs): # mengambil data berupa dictionary
    output = 0
    if kwargs['option'] == 'tambah':
        for angka in args:
            output += angka
    elif kwargs['option'] == 'kali':
        output = 1
        for angka in args:
            output *= angka
    else:
        print("Tidak ada operasi")

    return output

hasil = math(1,2,3,4,5,6, option = 'tambah')
print(f"hasil jumlah {hasil}")

hasil = math(1,2,3,4, option = 'kali')
print(f"hasil kali {hasil}")
