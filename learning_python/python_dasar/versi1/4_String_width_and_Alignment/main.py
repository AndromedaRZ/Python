# Width and Multiline

data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 160.2
data_nomor_sepatu = 41

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+"="*5) 
print(data_string)

# string multiline (dengan menggunakan enter, newline, (\n))
data_string = f"nama = {data_nama} \numur = {data_umur} \ntinggi = {data_tinggi} \nsepatu = {data_nomor_sepatu}"
print("\n"+6*"="+"Data String"+"="*6) 
print(data_string)

# String multiline (kutip triplets)

data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""

print("\n"+6*"="+"Data String"+"="*6) 
print(data_string)

# mengatur lebar
data_nama = "Ucup"
data_string = f"""
nama   = {data_nama:>8} # simbol (:>) berguna untuk mengatur indentasi, dan sejauh mana kita mengaturnya tergantung
umur   = {data_umur:>8} # angka yang ditempatkan setelahnya, pada kasus ini kita menulis (:>8) yang berarti
tinggi = {data_tinggi:>8} # akan membuat indentasi sejauh 8 huruf, dan isi dari stringnya juga termasuk ke dalam indentasinya
sepatu = {data_nomor_sepatu:>8}
"""

print("\n"+6*"="+"Data String"+"="*6) 
print(data_string)

