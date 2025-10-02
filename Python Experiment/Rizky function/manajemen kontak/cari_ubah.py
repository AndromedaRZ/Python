# program fungsi mencari dan mengubah kontak pada manajemen kontak

# data = {
#     'rizky':{
#         'nama':'rizky',
#         'nomor':'088212382177',
#         'email':'rizky@gmail.com'
#     }
# }

def cari_ubah(data): 
    if not data:
        title = f"│ Daftar kontak anda masih kosong! │"
        print(f"\n┌{'─'* (len(title) - 2)}┐")
        print(title)
        print(f"└{'─'* (len(title) - 2)}┘")
    
    else:
        cari_nama = input("Masukan nama kontak yang ingin dicari: ") # menggunakan key unik sebagai referensi untuk mencari suatu kontak
        if cari_nama not in data:
            title = f"│ Kontak yang anda cari tidak ada │"
            print(f"\n┌{'─'* (len(title) - 2)}┐")
            print(title)
            print(f"└{'─'* (len(title) - 2)}┘")
            
        else:
            NAMA = data[cari_nama]['nama']
            NOMOR = data[cari_nama]['nomor']
            EMAIL = data[cari_nama]['email']
            
            title = f"│ {'Kontak Ditemukan':^61} │"
            title2 = f"│ {NAMA:<13} │ {NOMOR:<14} │ {EMAIL:<28} │"
            print(f"\n┌{'─'*(len(title2) - 2)}┐")
            print(title)
            print(f"├{'─'*15}┬{'─'*16}┬{'─'*30}┤")
            print(title2)
            print(f"└{'─'*15}┴{'─'*16}┴{'─'*30}┘")
            
            confirm = input("Ingin mengubah kontak ini? [y/n]: ")
            if confirm == 'y':
                print('''1. Nama
2. Nomor
3. Email''')
                choice = input("Pilih yang ingin anda ubah [1-3]: ")
                if choice == '1': # jika user ingin mengubah nama kontak
                    nama_baru = input("Masukan nama baru: ")
                    if nama_baru in data:
                        title = "│ Kontak dengan nama tersebut sudah ada! │"
                        print(f"\n┌{'─'*(len(title) - 2)}┐")
                        print(title)
                        print(f"└{'─'*(len(title) - 2)}┘")
                    else:
                        # menyimpan data lama terlebih dahulu
                        nomor_lama = data[cari_nama]['nomor'] 
                        email_lama = data[cari_nama]['email']
                        
                        # membuat data baru untuk mengganti key unik dan nama nya tetapi tidak dengan nomor dan emailnya
                        data[nama_baru] = {
                            'nama': nama_baru,
                            'nomor': nomor_lama,
                            'email': email_lama
                        }
                        
                        del data[cari_nama] # menghapus data lama
                        
                        title = "│ Nama kontak berhasil diubah │"
                        print(f"\n┌{'─'*(len(title) - 2)}┐")
                        print(title)
                        print(f"└{'─'*(len(title) - 2)}┘")
        
                elif choice == '2': # jika user ingin mengubah nomor kontak
                    nomor_baru = input("Masukan nomor baru: ")
                    if nomor_baru in data:
                        title = "│ Kontak dengan nomor tersebut sudah ada! │"
                        print(f"\n┌{'─'*(len(title) - 2)}┐")
                        print(title)
                        print(f"└{'─'*(len(title) - 2)}┘")
                    else:
                        data[cari_nama]['nomor'] = nomor_baru
                        title = "│ Nomor kontak berhasil diubah │"
                        print(f"\n┌{'─'*(len(title) - 2)}┐")
                        print(title)
                        print(f"└{'─'*(len(title) - 2)}┘")
                            
                elif choice == '3': # jika user ingin mengubah email kontak
                    email_baru = input("Masukan nomor baru: ")
                    if email_baru in data:
                        title = "│ Kontak dengan email tersebut sudah ada! │"
                        print(f"\n┌{'─'*(len(title) - 2)}┐")
                        print(title)
                        print(f"└{'─'*(len(title) - 2)}┘")
                    else:
                        data[cari_nama]['email'] = email_baru
                        title = "│ Email kontak berhasil diubah │"
                        print(f"\n┌{'─'*(len(title) - 2)}┐")
                        print(title)
                        print(f"└{'─'*(len(title) - 2)}┘")
                            
            elif confirm == 'n':
                return
            else:
                title = "│ Pilihan tidak valid! │"
                print(f"\n┌{'─'*(len(title) - 2)}┐")
                print(title)
                print(f"└{'─'*(len(title) - 2)}┘")
        
# cari_ubah(data)