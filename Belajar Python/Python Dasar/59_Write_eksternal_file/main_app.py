# Tutorial write eksternal file

# 1. mode write, akan membuat file baru jika beluma ada filenya dan akan menimpa isi di dalam filenya setiap kali programnya berjalan (akan menimpa isi sebelumnya)
with open('data.txt', mode='w', encoding='utf-8') as file:
    file.write("John si Johnny")
    
with open('data.txt', mode='w', encoding='utf-8') as file:
    file.write("Ucup surucup") # akan menimpa write yang di atas (overwrite)
    
# 2. mode append, akan membuat file yang baru jika belum ada filenya dan akan menambah isi di dalam filenya setiap kali programnya berjalan (tidak menimpa isinya)
with open('data_2.txt', mode='a', encoding='utf-8') as file:
    file.write("Nama pertama\n")
    
with open('data_2.txt', mode='a', encoding='utf-8') as file:
    file.write("Nama kedua\n")
    
with open('data_2.txt', mode='a', encoding='utf-8') as file:
    file.write("Nama ketiga\n")

# mode r+
with open('data_3.txt', mode='w', encoding='utf-8') as file:
    file.write("baris pertama")

with open('data_3.txt', mode='r+', encoding='utf-8') as file:
    file.write('baris pertama\n')
    file.write('baris kedua\n')
    file.write('baris ketiga\n')
    
with open('data_3.txt','r+', encoding='utf-8') as file:
    data = file.read()
    print(data)

# akan menimpa isi filenya sesuai dengan panjang data (bukan seluruh isinya)
with open('data_3.txt', 'r+', encoding='utf-8') as file:
    file.write('timpa') 
    
    