from . import matematika
from . import fisika

# simbol titik (.) maksudnya adalah direktori tempat file ini berada yaitu sains yang bisa kita jadikan nama package

# __all__ ini berguna untuk mengambil semua fungsi yang ada di dalam package ini
# dan cara memanggilnya dengan mengetik seperti ini 'from sains import *'
# dengan menggunakan (*) pada saat mengimport, artinya kita memanggil fungsi __all__ yang isinya adalah list dari berbagai macam module yang kita masukkan tadi

__all__ = [ 
    "matematika",
    "fisika"
]

# tetapi cara menggunakan __all__ di atas sangan tidak direkomendasikan karena bisa menyebabkan keambiguan sumber apalagi pada saat mengimport banyak package dan module