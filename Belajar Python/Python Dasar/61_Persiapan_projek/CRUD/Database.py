from . import Operasi

DB_NAME = 'data.txt'

# template dictionary
TEMPLATE = {
    'pk': 'xxxxxx',
    'date_add': 'dd-mm-yyyy',
    'judul': 40*' ',
    'penulis': 40*' ',
    'tahun': 'yyyy'
}

# untuk mengantisipasi jika databasenya sudah atau atau belum
def init_console():
    try: # jika databasenya sudah ada, maka program ini akan berjalan dan tidak terjadi apa-apa
        with open(DB_NAME, 'r') as file:
            print('Database tersedia, init done')
    except: # jika databasenya belum ada, maka program ini akan berjalan dan user diminta menginput data untuk membuat database yang baru
        print('Database tidak ditemukan, membuat database yang baru')
        Operasi.create_first_data()
        
        