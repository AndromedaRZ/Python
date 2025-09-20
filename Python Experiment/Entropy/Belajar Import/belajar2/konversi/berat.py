def berat_awal():
    print("""
=== Konversi Berat ===
1. Kilogram (kg)
2. Gram (g)
3. Pon (lb)""")
    choice = input("Pilih satuan berat yang ingin dikonversi [1-3]: ")
    
    return choice

def berat_akhir(nilai):
    print("\n=== Konversi Berat ===")
    if nilai == '1':
        print("""1. Gram (g)
2. Pon (lb)""")
        
    elif nilai == '2':
        print("""1. Kilogram (kg)
2. Pon (lb)""")
        
    elif nilai == '3':
        print("""1. Kilogram (kg)
2. Gram (g)""")
        
    else:
        print("\nInput tidak valid!")
        return
    
    choice = input("Ingin dikonveri ke satuan apa? [1-2]: ")
    return choice

def berat_conv(berat_awal, berat_akhir):
    if berat_awal == '1':
        satuan_awal = 'kg'
        nilai = float(input("Masukkan nilai dalam Kilogram: "))
        if berat_akhir == '1':
            hasil = nilai * 1000
            satuan_akhir = 'g'
            nama_satuan_akhir = 'Gram'
        elif berat_akhir == '2':
            hasil = nilai * 2.20462
            satuan_akhir = 'lb'
            nama_satuan_akhir = 'Pon'
        
    elif berat_awal == '2':
        satuan_awal = 'g'
        nilai = float(input("Masukkan nilai dalam Gram: "))
        if berat_akhir == '1':
            hasil = nilai / 1000
            satuan_akhir = 'kg'
            nama_satuan_akhir = 'Kilogram'
        elif berat_akhir == '2':
            hasil = nilai / 453.592
            satuan_akhir = 'lb'
            nama_satuan_akhir = 'Pon'
        
    elif berat_awal == '3':
        satuan_awal = 'lb'
        nilai = float(input("Masukkan nilai dalam Pon: "))
        if berat_akhir == '1':
            hasil = nilai * 0.453592
            satuan_akhir = 'kg'
            nama_satuan_akhir = 'Kilogram'
        elif berat_akhir == '2':
            hasil = nilai * 453.592
            satuan_akhir = 'g'
            nama_satuan_akhir = 'Gram'
        
    else:
        print("\nInput tidak valid")
        return
    
    print(f"{nilai:,.1f} {satuan_awal} bila dikonversi ke {nama_satuan_akhir} akan menjadi: {hasil:,.1f} {satuan_akhir}")