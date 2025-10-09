from . import Database
from .Util import random_string
import time

def create(tahun, judul, penulis):
    data = Database.TEMPLATE.copy()
    
    data['pk'] = random_string(6)
    data['date_add'] = time.strftime("%H-%M-%S-%d-%M-%Y%z",time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)
    
    data_str = f'{data['pk']}, {data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n'
    
    try:
        with open(Database.DB_NAME, 'a', encoding='utf-8') as file:
            file.write(data_str)
            
    except:
        print('Data gagal ditambahkan!')
    

def create_first_data():
    # mengambil key-value pair template dari dictionary 'TEMPLATE'

    penulis = input("Penulis: ").capitalize()
    judul = input('Judul: ').capitalize()
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print('Silahkan masukan tahun lagi')   
        except:
            print('Tahun harus berupa angka, silahkan masukan tahun lagi')
    
    data = Database.TEMPLATE.copy()
    
    data['pk'] = random_string(6)
    data['date_add'] = time.strftime("%H-%M-%S-%d-%M-%Y%z",time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)
    
    data_str = f'{data['pk']}, {data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n'
    print(data_str)
    
    try:
        with open(Database.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(data_str)
            
    except:
        print('Eksekusi Gagal!')


def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    
    except:
        print('Membaca database error')
        return False    