# program fungsi menampilkan seluruh kontak yang telah ditambahkan pada manajemen kontak 

def display_kontak(data):
    '''fungsi untuk melihat seluruh kontak yang telah ditambahkan'''
    if not data:
        title = f"│ Daftar kontak anda masih kosong! │"
        print(f"\n┌{'─'* (len(title) - 2)}┐")
        print(title)
        print(f"└{'─'* (len(title) - 2)}┘")
    
    else:
        print(f'\n┌{'─'*4}┬{'─'*15}┬{'─'*16}┬{'─'*30}┐')
        print(f'│ {"No":<2} │ {"Nama":<13} │ {"Nomor":<14} │ {"Email":<28} │')
        print(f'├{'─'*4}┼{'─'*15}┼{'─'*16}┼{'─'*30}┤')
        for i, key in enumerate(data):
            NAMA = data[key]['nama']
            NOMOR = data[key]['nomor']
            EMAIL = data[key]['email']
            
            print(f'│ {i + 1:<2} │ {NAMA:<13} │ {NOMOR:<14} │ {EMAIL:<28} │')
        print(f'└{'─'*4}┴{'─'*15}┴{'─'*16}┴{'─'*30}┘')
        
