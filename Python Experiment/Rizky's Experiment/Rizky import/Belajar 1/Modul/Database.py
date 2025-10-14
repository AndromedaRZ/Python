import json
from . import Operasi

DB_NAME = 'inventaris.json'

def init_json():
    '''membaca data inventaris dari file json saat programnya pertama kali berjalan'''
    try: # jika file jsonnya ada, maka akan langusng membacanya
        with open(DB_NAME, 'r') as file:
            pass
    except: # jika file jsonnya belum ada, maka program ini akan membuat filenya terlebih dahulu
        print("Data inventaris kosong!, membuat data baru")
        with open(DB_NAME, 'w', encoding='utf-8') as file:
            json.dump({}, file, indent=4)
        Operasi.create_first_data()
     
# menyimpan data yang batu dibuat di dalam program ke file json eksternal
def save_json(data):
    '''menyimpan data ke file json'''
    with open(DB_NAME, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

# membaca file json eksternal
def read_json():
    '''membaca data inventaris'''
    with open(DB_NAME, 'r') as file:
        data = json.load(file)
        return data
