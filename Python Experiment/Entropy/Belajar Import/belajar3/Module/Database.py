import json

DB_NAME = "database_pengeluaran.json"

def simpan_data(data):
    '''Menyimpan data ke file json'''
    with open(DB_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def baca_database():
    '''Membaca data dari file json'''
    with open(DB_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def init_console():
    '''Mengecek apakah database tersedia atau tidak'''
    try:
        with open(DB_NAME, 'r') as file:
            data = json.load(file)
            if len(data) > 0:    
                print("Database tersedia, init selesai!")
    except:
        print("Database tidak ditemukan, membuat database baru...")
        with open(DB_NAME, 'w', encoding='utf-8') as file:
            file.write('[]')