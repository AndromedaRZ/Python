# contoh membuat exception

from numbers import Number

def tambah(a, b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise 'Input harus angka'
    return a + b

print(tambah(1,5))

# contoh program membuat exception sendiri
# fungsinya adalah mendeteksi apakah input yang masuk adalah angka atau bukan
# ketika input yang masuk ke dalam perhitungan bukan berupa angka
# maka 'except' atau lebih tepatnya 'raise' sebagai 'except' akan tereksekusi dan menampilkan runtime error

# contoh mengambil error message atau exception pada runtime error
angka = 0
try:
    hasil = 10 / angka
except Exception as error_message:
    print(error_message)
    
try:
    hasil = 10 / angka
except ZeroDivisionError as error_message:
    print(error_message)
    