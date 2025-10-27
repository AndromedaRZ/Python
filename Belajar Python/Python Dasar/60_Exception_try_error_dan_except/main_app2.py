# contoh membuat exception

# modul Number berfungsi untuk memeriksa apakah angka yang ingin di cek benar-benar angka atau bukan
from numbers import Number

def tambah(a, b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise 'input harus angka' # print ini akan berjalan jika programnya mengalami runtime error
    return a + b
    
print(tambah(9 ,4))

angka = 0

# try:
#     hasil = 10 / angka
    
# except Exception as error_message:
#     print(error_message)
    
try:
    hasil = 10 / angka
    
except ZeroDivisionError as error_message:
    print(error_message)