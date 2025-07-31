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
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""

print("\n"+6*"="+"Data String"+"="*6) 
print(data_string)

