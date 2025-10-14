from .Operasi import read, create, check, update, delete

# fungsi untuk melihat data inventaris
def read_data():
    '''fungsi untuk melihat data inventaris'''
    data = read()
    # Header
    print("\n"+"-"*90)
    print(f"{" No":3} | {"Kode Barang":12} | {"Nama Barang":20} | {"Harga Satuan Barang (Rp)":25} | {"Stok Barang":10}")
    print("-"*90)
    # Data
    for i, key in enumerate(data):
        NAMA = data[key]['nama']
        HARGA = data[key]['harga']
        STOK = data[key]['stok']
        print(f"{i+1:^3} | {key:12} | {NAMA:<20} | {HARGA:25} | {STOK:^10}")
    # Footer
    print("-"*90+"\n")
    
# fungsi untuk menambah data inventaris
def create_data():
    '''fungsi untuk menambah data inventaris'''
    print("\n"+"="*50)
    print("Silahkan masukan data barang")
    data = read()

    while True:
        nama = input("Nama barang: ")
        lolos = False
        for key, value in data.items():
            if nama == value['nama']:
                print("Barang tersebut sudah ada!")
                lolos = True
                break
        
        if not lolos:
            break
        
    while True:
        try:
            harga = int(input("Harga satuan barang (Rp): "))
            break
        except:
            print("Harga barang harus berupa angka!")
    
    while True:
        try:
            stok = int(input("Stok barang: "))
            break
        except:
            print("Stok barang harus berupa angka!")
    
    create(nama, harga, stok)
    
# fungsi untuk mengupdate data inventaris
def update_data():
    '''fungsi untuk mengupdate data inventaris'''
    read_data()
    while True:
        kode = input("Masukan kode barang yang ingin diupdate: ")
        cek_kode = check(kode)
        if cek_kode:
            break
        else:
            print("Kode barang tidak ditemukan!")
    
    while True:
        data = read()
        print()
        # Header
        print("-"*90)
        print(f" {"Kode Barang":12} | {"Nama Barang":20} | {"Harga Satuan Barang (Rp)":25} | {"Stok Barang":10}")
        print("-"*90)
        # Data
        NAMA = data[kode]['nama']
        harga = data[kode]['harga']
        stok = data[kode]['stok']
        print(f" {kode:12} | {NAMA:<20} | {harga:25} | {stok:^10}")
        # Footer
        print("-"*90)
        print("1. Harga")
        print("2. Stok")
        print("3. Keluar")
        choice = input("Pilih data yang ingin diupdate: ")
        
        match choice:
            case '1': harga = int(input("Harga satuan terbaru (Rp): "))
            case '2': stok = int(input("Stok terbaru: "))
            case '3': break
            case _: print("Input salah!")
        
        update(kode, harga, stok)
        
# fungsi untuk menghapus salah satu data inventaris
def delete_data():
    read_data()
    while True:
        kode = input("Masukan kode barang yang ingin dihapus: ")
        cek_kode = check(kode)
        if cek_kode:
            break
        else:
            print("Kode barang tidak ditemukan!")
    
    data = read()
    # Header
    print("-"*90)
    print(f" {"Kode Barang":12} | {"Nama Barang":20} | {"Harga Satuan Barang (Rp)":25} | {"Stok Barang":10}")
    print("-"*90)
    # Data
    NAMA = data[kode]['nama']
    harga = data[kode]['harga']
    stok = data[kode]['stok']
    print(f" {kode:12} | {NAMA:<20} | {harga:25} | {stok:^10}")
    # Footer
    print("-"*90)
    choice = input("Ingin menghapus data ini? [y/n]: ")
    if choice == 'y':
        return delete(kode)
    else:
        return
         
    
    
    
        
    
    

        
        
    
    
    