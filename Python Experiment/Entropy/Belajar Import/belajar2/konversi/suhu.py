def suhu_awal():
    print("""
=== Konversi Suhu ===
1. Celcius
2. Reamur
3. Fahrenheit
4. Kelvin""")
    choice = input("Pilih suhu yang ingin dikonversi [1-4]: ")
    return choice

def suhu_akhir(nilai):
    print("\n=== Konversi Suhu ===")
    if nilai == '1':
        print("""1. Reamur
2. Fahrenheit
3. Kelvin""")
        
    elif nilai == '2':
        print("""1. Celcius
2. Fahrenheit
3. Kelvin""")
        
    elif nilai == '3':
        print("""1. Celcius
2. Reamur
3. Kelvin""")
        
    elif nilai == '4':
        print("""1. Celcius
2. Reamur
3. Fahrenheit""")
    
    else:
        print("Input tidak valid!")
        return
    
    choice = input("Ingin dikonversi ke suhu apa? [1-3]: ")
    return choice
        
def suhu_conv(suhu_awal, suhu_akhir):
    
    if suhu_awal == '1':
        satuan_awal = 'C'
        nilai = float(input("Masukkan nilai dalam Celcius: "))
        if suhu_akhir == '1':
            hasil = nilai * 4 / 5
            satuan_akhir = 'R'
            nama_satuan_akhir = 'Reamur'
        elif suhu_akhir == '2':
            hasil = (nilai * 9 / 5) + 32
            satuan_akhir = 'F'
            nama_satuan_akhir = 'Fahreheit'
        elif suhu_akhir == '3':
            hasil = nilai + 273
            satuan_akhir = 'K'
            nama_satuan_akhir = 'Kelvin'

    elif suhu_awal == '2':
        satuan_awal = 'R'
        nilai = float(input("Masukkan nilai dalam Reamur: "))
        if suhu_akhir == '1':
            hasil = nilai * 5 / 4
            satuan_akhir = 'C'
            nama_satuan_akhir = 'Celcius'
        elif suhu_akhir == '2':
            hasil = (nilai * 9 / 4) + 32
            satuan_akhir = 'F'
            nama_satuan_akhir = 'Fahreheit'
        elif suhu_akhir == '3':
            hasil = nilai * 5 / 4 + 273
            satuan_akhir = 'K'
            nama_satuan_akhir = 'Kelvin'

    elif suhu_awal == '3':
        satuan_awal = 'F'
        nilai = float(input("Masukkan nilai dalam Fahrenheit: "))
        if suhu_akhir == '1':
            hasil = (nilai - 32) * 5 / 9
            satuan_akhir = 'C'
            nama_satuan_akhir = 'Celcius'
        elif suhu_akhir == '2':
            hasil = (nilai - 32) * 4 / 9
            satuan_akhir = 'R'
            nama_satuan_akhir = 'Reamur'
        elif suhu_akhir == '3':
            hasil = (nilai - 32) * 5 / 9 + 273
            satuan_akhir = 'K'
            nama_satuan_akhir = 'Kelvin'
     
    elif suhu_awal == '4':
        satuan_awal = 'K'
        nilai = float(input("Masukkan nilai dalam Kelvin: "))
        if suhu_akhir == '1':
            hasil = nilai - 273
            satuan_akhir = 'C'
            nama_satuan_akhir = 'Celcius'
        elif suhu_akhir == '2':
            hasil = (nilai - 273) * 4 / 5
            satuan_akhir = 'R'
            nama_satuan_akhir = 'Reamur'
        elif suhu_akhir == '3':
            hasil = (nilai - 273) * 9 / 5 + 32
            satuan_akhir = 'F'
            nama_satuan_akhir = 'Fahrenheit'
            
    else:
        print("\nInput tidak valid!")
        return
        
    print(f"{nilai:.1f} {satuan_awal} bila dikonversi ke {nama_satuan_akhir} akan menjadi: {hasil:.1f} {satuan_akhir}")
            
     

        
        
    
    
    
    