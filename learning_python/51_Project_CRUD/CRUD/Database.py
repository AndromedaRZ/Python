
from . import Operasi

DB_NAME = 'database.txt'
TEMPLATE = {
    'pk': 'XXXXXX', # prime key atau key unik
    'date_add': 'yyyy-mm-dd',
    'judul': 255*' ',
    'penulis': 255*' ',
    'tahun': 'yyyy',
}

def init_console():
    try:
        with open(DB_NAME, 'r') as file:
            print("Database tersedia, init done!")
    except:
        print("Database tidak ditemukan, silahkan membuat Database baru")
        with open(DB_NAME, 'w', encoding='utf-8') as file:
            Operasi.create_first_data()

            
        