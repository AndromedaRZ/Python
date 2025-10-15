

class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        
        
    def info(self):
        print('\n=== INFO MAHASISWA ===')
        print(f'Nama\t: {self.nama}')
        print(f'NIM\t: {self.nim}')
        print(f'Jurusan\t: {self.jurusan}')
        
    def ubah_jurusan(self, jurusan):
        self.jurusan = jurusan
                

mhs1 = Mahasiswa('Joko', 1020, 'Pertanian')
mhs1.info()

mhs2 = Mahasiswa('Luna', 2890, 'Akuntansi')
mhs2.info()

mhs1.jurusan = 'Teknik Sipil'
mhs1.info()
