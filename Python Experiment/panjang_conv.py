
print("""\nMasukkan satuan panjang yang ingin dikonversi
1) Kilometer (Km)
2) Hektometer (Hm)
3) Dekameter (Dam)
4) Meter (M)
5) Desimeter (Dm)
6) Centimeter (Cm)
7) Milimeter (Mm)""")
choice = int(input("Jawaban anda [1-7]: "))

if choice == 1:
    nilai_awal = float(input("\nMasukkan panjang dalam Kilometer (Km): "))
    if nilai_awal.is_integer():
        nilai_awal = int(nilai_awal)
    print("""\nIngin dikonversi menjadi satuan apa?
1) Hektometer (Hm)
2) Dekameter (Dam)
3) Meter (M)
4) Desimeter (Dm)
5) Centimeter (Cm)
6) Milimeter (Mm)""")
    choice = int(input("Jawaban anda [1-7]: "))
    
    if choice == 1:
        hasil = nilai_awal * 10
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Km jika dikonversi menjadi Hektometer")
        print(f"Hasilnya adalah {hasil} Hm")
        
    if choice == 2:
        hasil = nilai_awal * 100
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Km jika dikonversi menjadi Dekameter")
        print(f"Hasilnya adalah {hasil} Dam")
        
    if choice == 3:
        hasil = nilai_awal * 1000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Km jika dikonversi menjadi Meter")
        print(f"Hasilnya adalah {hasil:,} M")
        
    if choice == 4:
        hasil = nilai_awal * 10000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Km jika dikonversi menjadi Desimeter")
        print(f"Hasilnya adalah {hasil:,} Dm")
        
    if choice == 5:
        hasil = nilai_awal * 100000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Km jika dikonversi menjadi Centimeter")
        print(f"Hasilnya adalah {hasil:,} Cm")
        
    if choice == 6:
        hasil = nilai_awal * 1000000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Km jika dikonversi menjadi Milimeter")
        print(f"Hasilnya adalah {hasil:,} Mm")
        
        
#
        
if choice == 2:
    nilai_awal = float(input("\nMasukkan panjang dalam Hektometer (Hm): "))
    if nilai_awal.is_integer():
        nilai_awal = int(nilai_awal)
    print("""\nIngin dikonversi menjadi satuan apa?
1) Kilometer (Km)
2) Dekameter (Dam)
3) Meter (M)
4) Desimeter (Dm)
5) Centimeter (Cm)
6) Milimeter (Mm)""")
    choice = int(input("Jawaban anda [1-7]: "))
    
    if choice == 1:
        hasil = nilai_awal / 10
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Hm jika dikonversi menjadi Kilometer")
        print(f"Hasilnya adalah {hasil} Hm")
        
    if choice == 2:
        hasil = nilai_awal * 10
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Hm jika dikonversi menjadi Dekameter")
        print(f"Hasilnya adalah {hasil} Dam")
        
    if choice == 3:
        hasil = nilai_awal * 100
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Hm jika dikonversi menjadi Meter")
        print(f"Hasilnya adalah {hasil:,} M")
        
    if choice == 4:
        hasil = nilai_awal * 1000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Hm jika dikonversi menjadi Desimeter")
        print(f"Hasilnya adalah {hasil:,} Dm")
        
    if choice == 5:
        hasil = nilai_awal * 10000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Hm jika dikonversi menjadi Centimeter")
        print(f"Hasilnya adalah {hasil:,} Cm")
        
    if choice == 6:
        hasil = nilai_awal * 100000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Hm jika dikonversi menjadi Milimeter")
        print(f"Hasilnya adalah {hasil:,} Mm")
        
#
        
if choice == 3:
    nilai_awal = float(input("\nMasukkan panjang dalam Dekameter (Dam): "))
    if nilai_awal.is_integer():
        nilai_awal = int(nilai_awal)
    print("""\nIngin dikonversi menjadi satuan apa?
1) Kilometer (Km)
2) Hektometer (Hm)
3) Meter (M)
4) Desimeter (Dm)
5) Centimeter (Cm)
6) Milimeter (Mm)""")
    choice = int(input("Jawaban anda [1-7]: "))
    
    if choice == 1:
        hasil = nilai_awal / 100
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Dam jika dikonversi menjadi Kilometer")
        print(f"Hasilnya adalah {hasil} Km")
        
    if choice == 2:
        hasil = nilai_awal / 10
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Dam jika dikonversi menjadi Hektometer")
        print(f"Hasilnya adalah {hasil} Hm")
        
    if choice == 3:
        hasil = nilai_awal * 10
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Dam jika dikonversi menjadi Meter")
        print(f"Hasilnya adalah {hasil:,} M")
        
    if choice == 4:
        hasil = nilai_awal * 100
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Dam jika dikonversi menjadi Desimeter")
        print(f"Hasilnya adalah {hasil:,} Dm")
        
    if choice == 5:
        hasil = nilai_awal * 1000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Dam jika dikonversi menjadi Centimeter")
        print(f"Hasilnya adalah {hasil:,} Cm")
        
    if choice == 6:
        hasil = nilai_awal * 10000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Dam jika dikonversi menjadi Milimeter")
        print(f"Hasilnya adalah {hasil:,} Mm")
        
#
        
if choice == 4:
    nilai_awal = float(input("\nMasukkan panjang dalam Meter (M): "))
    if nilai_awal.is_integer():
        nilai_awal = int(nilai_awal)
    print("""\nIngin dikonversi menjadi satuan apa?
1) Kilometer (Km)
2) Hektometer (Hm)
3) Dekameter (Dam)
4) Desimeter (Dm)
5) Centimeter (Cm)
6) Milimeter (Mm)""")
    choice = int(input("Jawaban anda [1-7]: "))
    
    if choice == 1:
        hasil = nilai_awal / 1000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} M jika dikonversi menjadi Kilometer")
        print(f"Hasilnya adalah {hasil} Km")
        
    if choice == 2:
        hasil = nilai_awal / 100
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} M jika dikonversi menjadi Hektometer")
        print(f"Hasilnya adalah {hasil} Hm")
        
    if choice == 3:
        hasil = nilai_awal / 10
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} M jika dikonversi menjadi Dekameter")
        print(f"Hasilnya adalah {hasil:,} Dam")
        
    if choice == 4:
        hasil = nilai_awal * 10
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} M jika dikonversi menjadi Desimeter")
        print(f"Hasilnya adalah {hasil:,} Dm")
        
    if choice == 5:
        hasil = nilai_awal * 100
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} M jika dikonversi menjadi Centimeter")
        print(f"Hasilnya adalah {hasil:,} Cm")
        
    if choice == 6:
        hasil = nilai_awal * 1000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} M jika dikonversi menjadi Milimeter")
        print(f"Hasilnya adalah {hasil:,} Mm")
        
#
        
if choice == 5:
    nilai_awal = float(input("\nMasukkan panjang dalam Desimeter (Dm): "))
    if nilai_awal.is_integer():
        nilai_awal = int(nilai_awal)
    print("""\nIngin dikonversi menjadi satuan apa?
1) Kilometer (Km)
2) Hektometer (Hm)
3) Dekameter (Dam)
4) Meter (M)
5) Centimeter (Cm)
6) Milimeter (Mm)""")
    choice = int(input("Jawaban anda [1-7]: "))
    
    if choice == 1:
        hasil = nilai_awal / 10000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Dm jika dikonversi menjadi Kilometer")
        print(f"Hasilnya adalah {hasil} Km")
        
    if choice == 2:
        hasil = nilai_awal / 1000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Dm jika dikonversi menjadi Hektometer")
        print(f"Hasilnya adalah {hasil} Hm")
        
    if choice == 3:
        hasil = nilai_awal / 100
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Dm jika dikonversi menjadi Dekameter")
        print(f"Hasilnya adalah {hasil:,} Dam")
        
    if choice == 4:
        hasil = nilai_awal / 10
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Dm jika dikonversi menjadi Meter")
        print(f"Hasilnya adalah {hasil:,} M")
        
    if choice == 5:
        hasil = nilai_awal * 10
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Dm jika dikonversi menjadi Centimeter")
        print(f"Hasilnya adalah {hasil:,} Cm")
        
    if choice == 6:
        hasil = nilai_awal * 100
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Dm jika dikonversi menjadi Milimeter")
        print(f"Hasilnya adalah {hasil:,} Mm")

#
        
if choice == 6:
    nilai_awal = float(input("\nMasukkan panjang dalam Centimeter (Cm): "))
    if nilai_awal.is_integer():
        nilai_awal = int(nilai_awal)
    print("""\nIngin dikonversi menjadi satuan apa?
1) Kilometer (Km)
2) Hektometer (Hm)
3) Dekameter (Dam)
4) Meter (M)
5) Desimeter (Dm)
6) Milimeter (Mm)""")
    choice = int(input("Jawaban anda [1-7]: "))
    
    if choice == 1:
        hasil = nilai_awal / 100000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Cm jika dikonversi menjadi Kilometer")
        print(f"Hasilnya adalah {hasil} Km")
        
    if choice == 2:
        hasil = nilai_awal / 10000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Cm jika dikonversi menjadi Hektometer")
        print(f"Hasilnya adalah {hasil} Hm")
        
    if choice == 3:
        hasil = nilai_awal / 1000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Cm jika dikonversi menjadi Dekameter")
        print(f"Hasilnya adalah {hasil:,} Dam")
        
    if choice == 4:
        hasil = nilai_awal / 100
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Cm jika dikonversi menjadi Meter")
        print(f"Hasilnya adalah {hasil:,} M")
        
    if choice == 5:
        hasil = nilai_awal / 10
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Cm jika dikonversi menjadi Desimeter")
        print(f"Hasilnya adalah {hasil:,} Dm")
        
    if choice == 6:
        hasil = nilai_awal * 10
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Cm jika dikonversi menjadi Milimeter")
        print(f"Hasilnya adalah {hasil:,} Mm")
        
#
        
if choice == 7:
    nilai_awal = float(input("\nMasukkan panjang dalam Milimeter (Mm): "))
    if nilai_awal.is_integer():
        nilai_awal = int(nilai_awal)
    print("""\nIngin dikonversi menjadi satuan apa?
1) Kilometer (Km)
2) Hektometer (Hm)
3) Dekameter (Dam)
4) Meter (M)
5) Desimeter (Dm)
6) Centimeter (Cm)""")
    choice = int(input("Jawaban anda [1-7]: "))
    
    if choice == 1:
        hasil = nilai_awal / 1000000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Mm jika dikonversi menjadi Kilometer")
        print(f"Hasilnya adalah {hasil} Km")
        
    if choice == 2:
        hasil = nilai_awal / 100000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Mm jika dikonversi menjadi Hektometer")
        print(f"Hasilnya adalah {hasil} Hm")
        
    if choice == 3:
        hasil = nilai_awal / 10000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Mm jika dikonversi menjadi Dekameter")
        print(f"Hasilnya adalah {hasil:,} Dam")
        
    if choice == 4:
        hasil = nilai_awal / 1000
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Mm jika dikonversi menjadi Meter")
        print(f"Hasilnya adalah {hasil:,} M")
        
    if choice == 5:
        hasil = nilai_awal / 100
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Mm jika dikonversi menjadi Desimeter")
        print(f"Hasilnya adalah {hasil:,} Dm")
        
    if choice == 6:
        hasil = nilai_awal / 100
        if hasil.is_integer():
            hasil = int(hasil)
        print(f"{nilai_awal} Mm jika dikonversi menjadi Centimeter")
        print(f"Hasilnya adalah {hasil:,} Cm")