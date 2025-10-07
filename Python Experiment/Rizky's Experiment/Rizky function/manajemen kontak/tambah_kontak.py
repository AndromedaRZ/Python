
dict_kontak = []

def tambah_kontak(dict_kontak,**sementara):
    nama = sementara['nama']
    nomor = sementara['nomor']
    email = sementara['email']
    print(sementara)
    # nama = input("Masukan nama kontak: ")
    # nomor = input("Masukan nomor kontak: ")
    # email = input("Masukan email kontak: ")
    dict_kontak.append(sementara)
    print(dict_kontak)

data = tambah_kontak(dict_kontak, nama='rizky', nomor='088212382177', email='rizkyricky859@gmail.com')
print(dict_kontak)

