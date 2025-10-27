# Width and Multiline

# Data
data_nama = "Ucup Surucup"
data_umur = 18
data_tinggi = 160.1
data_nomor_sepatu = 42

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, no sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# string multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur},\ntinggi = {data_tinggi},\nno sepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String Multiline"+5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""Nama      = {data_nama}
Umur      = {data_umur}
Tinggi    = {data_tinggi}
No Sepatu = {data_nomor_sepatu}"""
print("\n"+5*"="+"Data String Multiline (kutip)"+5*"=")
print(data_string)

# mengatur lebar
data_nama = "ucup"
data_string = f"""Nama      = {data_nama:>5}
Umur      = {data_umur:>5} 
Tinggi    = {data_tinggi}
No Sepatu = {data_nomor_sepatu}"""
print("\n"+5*"="+"Data String Multiline (kutip)"+5*"=")
print(data_string)

# pada perintah print di atas terdapat penggunaan perintah tambahan pada sebelah kanan variabel yang ingin diprint (data_nama:>5), angka 5 berfungsi untuk menentukan berada jumlah string dalam variabel tersebut, misal jumlah string dalam variabel 'data_nama' adalah 4 dengan isi nya yaitu 'ucup', maka angka 5 akan membuat isi stringnya menjadi 5 dan mengatur stringnya agar menjadi rata kanan dengan perintah '>' sebelum memasukkan angka 5 nya.
