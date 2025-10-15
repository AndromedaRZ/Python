import json

DB = 'data_transaksi.json'

# membaca data transaksi saat programnya pertama kali berjalan
def init_console():
    '''membaca data transaksi saat programnya pertama kali berjalan'''
    try: # jika file jsonnya ada, maka akan langsung membacanya
        with open(DB, 'r') as f:
            pass
    except: # jika file jsonnya belum ada, maka progam ini akan membuat file jsonnya secara otomatis
        with open(DB, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=4)
    
# menyimpan data baru ke file json setiap kali ada perubahan        
def save_data(data):
    '''menyimpan data yang berubah ke file json'''
    with open(DB, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

# membaca data file json eksternal
def read():
    '''membaca data file json'''
    with open(DB, 'r') as f:
        data = json.load(f)
        return data
    
# cek nomor urut transaksi
def check(nomor):
    data = read()
    if len(data) > 0:
        if 1 <= nomor <= len(data):
            return nomor
        else:
            return False