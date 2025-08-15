# Konversi satuan panjang

def format_awal(num):
    """Mengubah float menjadi int jika nilai desimalnya 0"""
    if isinstance(num, float) and num.is_integer():
        return int(num)
    return num

def format_number(num):
    """Mengubah float menjadi int jika desimalnya 0, 
       jika tidak maka dibulatkan ke 2 angka di belakang koma"""
    if isinstance(num, float):
        if num.is_integer():
            return int(num)
        else:
            return round(num, 2)
    return num

print('''
Pilih satuan ukuran panjang awal yang ingin dikonversi
1) Kilometer \t(Km)
2) Hektometer \t(Hm)
3) Dekameter \t(Dam)
4) Meter \t(M)
5) Desimeter \t(Dm)
6) Centimeter \t(Cm)
7) Milimeter \t(Mm)''')
satuan_awal = int(input(("Jawaban anda [1-7]: ")))

if satuan_awal == 1:
    nilai = format_awal(float(input("Masukkan angka dalam Kilometer(Km): ")))
    print('''
Ingin dikonversi menjadi satuan apa?
1) Hektometer \t(Hm)
2) Dekameter \t(Dam)
3) Meter \t(M)
4) Desimeter \t(Dm)
5) Centimeter \t(Cm)
6) Milimeter \t(Mm)''')
    satuan_akhir = int(input(("Jawaban anda [1-6]: ")))

    if satuan_akhir == 1:
        hasil = format_number(float(nilai * 10))
        print(f"{nilai:,} Km jika dikonversi menjadi Hektometer hasilnya adalah\n{hasil:,} Hm")

    elif satuan_akhir == 2:
        hasil = format_number(float(nilai * 100))
        print(f"{nilai} Km jika dikonversi menjadi Dekameter hasilnya adalah\n{hasil} Dam")

    elif satuan_akhir == 3:
        hasil = format_number(float(nilai * 1000))
        print(f"{nilai} Km jika dikonversi menjadi Meter hasilnya adalah\n{hasil} M")

    elif satuan_akhir == 4:
        hasil = format_number(float(nilai * 10000))
        print(f"{nilai} Km jika dikonversi menjadi Desimeter hasilnya adalah\n{hasil} Dm")

    elif satuan_akhir == 5:
        hasil = format_number(float(nilai * 100000))
        print(f"{nilai} Km jika dikonversi menjadi Centimeter hasilnya adalah\n{hasil} Cm")

    elif satuan_akhir == 6:
        hasil = format_number(float(nilai * 1000000))
        print(f"{nilai} Km jika dikonversi menjadi Milimeter hasilnya adalah\n{hasil} Mm")


elif satuan_awal == 2:
    nilai = format_awal(float(input("Masukkan angka dalam Hektometer(Hm): ")))

elif satuan_awal == 3:
    nilai = format_awal(float(input("Masukkan angka dalam Dekameter(Dam): ")))

elif satuan_awal == 4:
    nilai = format_awal(float(input("Masukkan angka dalam Meter (M): ")))

elif satuan_awal == 5:
    nilai = format_awal(float(input("Masukkan angka dalam Desimeter(Dm): ")))

elif satuan_awal == 6:
    nilai = format_awal(float(input("Masukkan angka dalam Centimeter(Cm): ")))

elif satuan_awal == 7:
    nilai = format_awal(float(input("Masukkan angka dalam Milimeter(Mm): ")))

else:
    print("Masukkan opsi yang sesuai, silahkan mulai ulang program")

