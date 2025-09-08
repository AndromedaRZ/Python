# Pengenalan fungsi

'''
Function dalam python adalah sekumpulan kode yang dibuat untuk menjalankan tugas tertentu, dan bisa dipakai berulang-ulang tanpa perlu menulis ulang kodenya, jadi bisa kita manfaatkan untuk kode yang akan dijalankan berulang kali

'''

''' Membuat fungsi '''
# cara membuat fungsi adalah diawali dengan 'def' yang artinya 'definition'

'''
def nama_function(): <- 
    # bisa ditambahkan catatan untuk fungsinya
    print("Hello World!") <- isi kode function 
'''


def hello_world():
    'fungsi menampilkan Hello World!' # sebagai note atau catatan fungsi dari function yang kita buat
    print("Hello World!")
    print("Kepada user")
    print("Dan juga kepada para programer")

# Kita juga bisa menambahkan beberapa kode di dalam function di atas

# cara menjalankan function adalah dengan memasukan kode sebelah kanan 'def'
hello_world() # inputnya akan sama dengan hello_world() yang tadi dibuat pada function

# fungsi() # akan error karena fungsi ini baru didefinisikan di bawah kode ini

def fungsi():
    '''pemanggilan fungsi atau function harus setelah dibuat atau didefinisikan'''
    print("Ini adalah fungsi")

# kita panggil function-nya
fungsi()

