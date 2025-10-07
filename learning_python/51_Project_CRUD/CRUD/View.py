from . import Operasi

def delete_console():
    read_console()
    while True:
        print("Silahkan pilih nomor buku yang ingin didelete")
        no_buku = int(input("Nomor buku: "))
        data_buku = Operasi.read(index = no_buku)
        
        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]
            
            # data yang ingin didelete
            print("\n"+"="*100)
            print("Data yang ingin anda hapus")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")
            
            isDone = input("Apakah anda yakin? (y/n) ").lower()
            if isDone == 'y':
                Operasi.delete(no_buku)
                break
        else:
            print("Nomor tidak valid, silahkan masukkan lagi")
    
    print("Data berhasil dihapus")
    

def update_console():
    read_console()
    while True:
        print("Silahkan pilih nomor buku yang ingin diupdate")
        no_buku = int(input("Nomor buku: "))
        data_buku = Operasi.read(index = no_buku)
        
        data_break = data_buku.split(',')
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4][:-1]
        
        if data_buku:
            break
        else:
            print("Nomor tidak valid, silahkan masukkan lagi")
    
    while True:
        # data yang ingin diupdate
        print("\n"+"="*100)
        print("Silahkan pilih data apa yang ingin diubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        
        # memilih mode untuk update
        user_option = input("Pilih data [1-3]: ")
        print("\n"+"="*100)
        match user_option:
            case '1': judul = input("Judul\t: ")
            case '2': penulis = input("Penulis\t: ")
            case '3':
                while True:
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")
                    except ValueError:
                        print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")
            case _: print("index tidak cocok")
        
        print("Data baru anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        isDone = input("Apakah data sudah sesuai? (y/n) ").lower()
        if isDone == 'y':
            break
    
    Operasi.update(no_buku, pk, date_add, tahun, judul, penulis)
    

def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data buku\n")
    penulis = input("Masukkan nama penulis\t: ")
    judul = input("Masukkan judul buku\t: ")
    while True:
        try:
            tahun = int(input("Masukkan tahun terbit\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")
        except ValueError:
            print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")
            
    Operasi.create(tahun, judul, penulis)
    print('\nBerikut adalah data baru anda')
    read_console()

def read_console():
    '''Membaca daftar buku'''
    data_file = Operasi.read()
    index = 'No'
    judul = 'Judul'
    penulis = 'Penulis'
    tahun = 'Tahun'
    
    # header
    print('\n'+'='*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print('-'*100)
    
    # data
    for index, data in enumerate(data_file):
        data_break = data.split(',') # untuk mengubah kumpulan datanya menjadi list agar kita bisa mengaksesnya satu-per-satu
        pk = data_break[0]
        date_add = data_break[1]
        penulis  = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}", end="")
    # footer
    print('='*100+'\n')