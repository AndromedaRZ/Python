'''Type hints pada fungsi'''

# bentuk standar fungsi yang sudah dipelajari
'''
def fungsi(parameter):
    print(parameter)

fungsi(1)
fungsi("ucup")
fungsi(True)
'''

# penggunaan type hints

# argument bisa kita artikan juga sebagai parameter
# jadi kedua itu adalah satu hal yang sama

def sepuluh_pangkat(argument:int) -> int:
    '''fungsi dengan hints'''
    # pada (argument:int) menunjukkan bahwa nilai dari argument atau parameter harus bertipe integer
    # dan tanda panah -> menunjukkan bahwa hasil dari eksekusi fungsi tersebut atau 'return'-nya berupa integer (jika tidak ditambahkan manual defaultnya akan berupa 'any')
    # dan jika kita tidak menambahkan return di dalam fungsinya maka hasilnya akan terlihat menjadi 'none'
    output = 10 ** argument
    return output

hasil = sepuluh_pangkat(2)
print(hasil)

import string

def display(argument:string):
    '''fungsi string'''
    # (argument:string) berguna untuk menunjukkan bahwa input dari argument atau nilai dari argument harus bertipe string
    print(argument)
    
display(1)

'''
rangkuman type hints

1. type hints digunakan untuk menentukan nilai atau tipe data dari argument suatu fungsi yang kita buat
2. ketika membuat fungsi, setelah kurung argument kita bisa menambahkan tanda panah -> lalu memasukkan tipe data tertentu yang nantinya akan menjadi tipe data dari output fungsi tersebut (atau hasil dari return)
'''