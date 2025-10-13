from . import Operasi

def delete_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor buku yang ingin didelete")
        no_buku = int(input("Nomor buku: ")) # meminta user untuk memasukan no urut buku yang ingin diupdate
        data_buku = Operasi.read(index=no_buku) # mendeteksi suatu keyword menggunakan 'index' dan 'kwargs' pada fungsinya
        
        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]
            
            # Data yang ingin diubah/diupdate
            print("\n"+"="*100)
            print('Silahkan pilih data yang ingin anda hapus')
            print(f'1. Judul\t: {judul:.40}')
            print(f'2. penulis\t: {penulis:.40}')
            print(f'3. tahun\t: {tahun:.4}')
            
            isDone = input("Apakah anda yakin delete data tersebut? [y/n]: ").lower()
            if isDone == 'y':
                Operasi.delete(no_buku)
                break
        else:
            print('Nomor tidak valid, silahkan masukan lagi!')
            
    print("Data berhasil dihapus")
   
def update_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor buku yang ingin diupdate")
        no_buku = int(input("Nomor buku: ")) # meminta user untuk memasukan no urut buku yang ingin diupdate
        data_buku = Operasi.read(index=no_buku) # mendeteksi suatu keyword menggunakan 'index' dan 'kwargs' pada fungsinya
        
        if data_buku:
            break
        else:
            print('Nomor tidak valid, silahkan masukan lagi!')
    
    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]
    
    while(True):
        # Data yang ingin diubah/diupdate
        print("\n"+"="*100)
        print('Silahkan pilih data yang ingin anda ubah')
        print(f'1. Judul\t: {judul:.40}')
        print(f'2. penulis\t: {penulis:.40}')
        print(f'3. tahun\t: {tahun:.4}')
        
        # memilih data yang ingin diubah/diupdate (judul/penulis/tahun)
        user_option = input("Pilih data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case '1': judul = input('Judul\t: ').capitalize()
            case '2': penulis = input('penulis\t: ').title()
            case '3': 
                while(True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print('Silahkan masukan tahun lagi')   
                    except:
                        print('Tahun harus berupa angka, silahkan masukan tahun lagi')
            
            case _: print("Input tidak cocok!")
        
        print('Data baru anda')
        print(f'1. Judul\t: {judul:.40}')
        print(f'2. penulis\t: {penulis:.40}')
        print(f'3. tahun\t: {tahun:.4}')
        isDone = input("Apakah update data selesai? [y/n]: ").lower()
        if isDone == 'y':
            break
    
    Operasi.update(no_buku, pk, data_add, tahun, judul, penulis)


def create_console():
    print('\n\n'+'='*100)
    print("Silahkan tambah data buku\n")
    judul = input("Judul\t: ").capitalize()
    penulis = input("Penulis\t: ").title()
    
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print('Silahkan masukan tahun lagi')   
        except:
            print('Tahun harus berupa angka, silahkan masukan tahun lagi')
    
    Operasi.create(judul, penulis, tahun)
    print("\nBerikut adalah data baru anda")
    read_console()
        

def read_console():
    data_file = Operasi.read()
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"
    
    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)
    
    # Data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:<4} | {judul:.40} | {penulis:.40} | {tahun:4}", end='')
            
    # Footer
    print('='*100+"\n")

    