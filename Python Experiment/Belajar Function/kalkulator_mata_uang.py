'''Kalkulator mata uang'''

from decimal import Decimal, ROUND_HALF_UP

# kurs terhadap IDR (1 unit FX = x Rupiah)
kurs = {
    "USD": 16400, # 1 dolar amerika = Rp16.400
    "EUR": 19100, # 1 euro = Rp19.100
    "JPY": 110, # 1 yen jepang = Rp110
    "SGD": 12700, # 1 dolar singapura = Rp12.700
}

# metadata mata uang (untuk format dan validasi)
mata_uang = {
    "IDR": {"nama": "Rupiah", "simbol": "Rp", "desimal": 0},
    "USD": {"nama": "US Dollar", "simbol": "$", "desimal": 2},
    "EUR": {"nama": "Euro", "simbol": "€", "desimal": 2},
    "JPY": {"nama": "Yen", "simbol": "¥", "desimal": 0},
    "SGD": {"nama": "Singapore Dollar", "simbol": "S$", "desimal": 2},
}

def idr_to_fx(jumlah_idr: float, kode_fx: str) -> float:
    '''fungsi mengubah idr ke fx'''
    hasil = jumlah_idr / kurs[kode_fx]
    return hasil
        
# def bulatkan(nominal: float, desimal: int) -> float:
    '''fungsi membulatkan fx'''
    q = Decimal(10) ** -desimal
    return float(Decimal(nominal).quantize(q, rounding=ROUND_HALF_UP))

def format_idr(nominal):
    '''fungsi mengatur format idr'''
    return f"Rp{nominal:,}".replace(",",".")

def fx_to_idr(jumlah_fx: float, kode_fx: str):
    '''fungsi mengubah fx ke idr'''
    hasil = int(jumlah_fx * kurs[kode_fx])
    return hasil

def format_fx(nominal, simbol, desimal):
    '''fungsi mengatur format fx'''
    nilai = round(nominal, desimal)
    nilai = f"{nilai:.{desimal}f}".rstrip('0').rstrip('.')
    return f"{nilai}{simbol}"


while True:
    print('''
=== KALKULATOR MATA UANG ===
1. Lihat daftar kurs
2. Konversi Rupiah ke mata uang lain
3. Konversi mata uang lain ke Rupiah
4. Konversi antar mata uang asing
5. Keluar''')
    choice = input("Apa yang ingin anda lakukan? [1-5]: ")
    
# ================================================================================
# 1. Melihat dafar kurs
    if choice == '1':
        for KEY, money in kurs.items():
            print(f"{KEY}: 1 {KEY} = {money}")
            
# ================================================================================
# 2. Konversi rupiah ke fx         
    if choice == '2':
        jumlah_idr = int(input("Masukkan nilai mata uang dalam Rupiah: "))
        while jumlah_idr < 500:
            print("Nilai Rupiah tidak boleh lebih kecil dari 500!")
            jumlah_idr = int(input("Masukkan nilai mata uang dalam Rupiah: "))
        
        print("\n======================")  
        print("1. USD (US Dollar)")
        print("2. EUR (Euro)")
        print("3. JPY (Yen)")
        print("4. SGD (Singapore Dollar)")  
        conv = input("Pilih mata uang tujuan [1/2/3/4]: ")
        
        if conv == '1':
            kode_fx = "USD"
        elif conv == '2':
            kode_fx = "EUR"
        elif conv == '3':
            kode_fx = "JPY"
        elif conv == '4':
            kode_fx = "SGD"
                  
        hasil = idr_to_fx(jumlah_idr, kode_fx)
        jumlah_idr = format_idr(jumlah_idr)
        # hasil = bulatkan(hasil, mata_uang[kode_fx]['desimal'])
        hasil = format_fx(hasil, mata_uang[kode_fx]['simbol'], mata_uang[kode_fx]['desimal'])

        print(f"{jumlah_idr} bila dikonversi ke {kode_fx} akan menjadi {hasil}")


# ================================================================================
# 3. Konversi fx ke rupiah     
    if choice == '3':
        print("\n======================")  
        print("1. USD (US Dollar)")
        print("2. EUR (Euro)")
        print("3. JPY (Yen)")
        print("4. SGD (Singapore Dollar)")
        conv = input("Pilih mata uang yang ingin dikonversi [1/2/3/4]: ")
        
        if conv == '1':
            kode_fx = "USD"
        elif conv == '2':
            kode_fx = "EUR"
        elif conv == '3':
            kode_fx = "JPY"
        elif conv == '4':
            kode_fx = "SGD"
        
        jumlah_fx = float(input(f"Masukkan nilai uang mata uang dalam {kode_fx}: "))
        
        while jumlah_fx <= 0:
            print("Nilai mata uang tidak boleh 0 atau kurang dari 0!")
            jumlah_fx = float(input(f"Masukkan nilai uang mata uang dalam {kode_fx}: "))
        
        hasil = fx_to_idr(jumlah_fx, kode_fx)
        jumlah_fx = format_fx(jumlah_fx, mata_uang[kode_fx]['simbol'], mata_uang[kode_fx]['desimal'])
        hasil = format_idr(hasil)
        # jumlah_fx = bulatkan(jumlah_fx, mata_uang[kode_fx]['desimal']) 
            
        print(f"{jumlah_fx} bila dikonversi ke IDR akan menjadi: {hasil}")
            
# ================================================================================
# 4. Konversi antar fx
    if choice == '4':
        print("\n======================")  
        print("1. USD (US Dollar)")
        print("2. EUR (Euro)")
        print("3. JPY (Yen)")
        print("4. SGD (Singapore Dollar)")
        conv = input("Pilih mata uang yang ingin dikonversi [1/2/3/4]: ")
        
        
        
        if conv == '1':
            kode_fx_awal = "USD"
            jumlah_fx = float(input(f"Masukkan nilai mata uang dalam {kode_fx_awal}: "))
            
            while jumlah_fx <= 0:
                print("Nilai mata uang tidak boleh 0 atau kurang dari 0!")
                jumlah_fx = float(input(f"Masukkan nilai uang mata uang dalam {kode_fx_awal}: "))
            
            print("\n======================")
            print("1. EUR (Euro)")
            print("2. JPY (Yen)")
            print("3. SGD (Singapore Dollar)")
            conv = input("Pilih mata uang tujuan [1/2/3]: ")
            
            if conv == '1':
                kode_fx = "EUR"
            elif conv == '2':
                kode_fx = "JPY"
            elif conv == '3':
                kode_fx = "SGD"
                
        elif conv == '2':
            kode_fx_awal = "EUR"
            jumlah_fx = float(input(f"Masukkan nilai mata uang dalam {kode_fx_awal}: "))
            
            while jumlah_fx <= 0:
                print("Nilai mata uang tidak boleh 0 atau kurang dari 0!")
                jumlah_fx = float(input(f"Masukkan nilai uang mata uang dalam {kode_fx_awal}: "))
            
            print("\n======================")
            print("1. USD (US Dollar)")
            print("2. JPY (Yen)")
            print("3. SGD (Singapore Dollar)")
            conv = input("Pilih mata uang tujuan [1/2/3]: ")
            
            if conv == '1':
                kode_fx = "USD"
            elif conv == '2':
                kode_fx = "JPY"
            elif conv == '3':
                kode_fx = "SGD"
            
        elif conv == '3':
            kode_fx_awal = "JPY"
            jumlah_fx = float(input(f"Masukkan nilai mata uang dalam {kode_fx_awal}: "))
            
            while jumlah_fx <= 0:
                print("Nilai mata uang tidak boleh 0 atau kurang dari 0!")
                jumlah_fx = float(input(f"Masukkan nilai uang mata uang dalam {kode_fx_awal}: "))
            
            print("\n======================")
            print("1. USD (US Dollar)")
            print("2. EUR (Euro)")
            print("3. SGD (Singapore Dollar)")
            conv = input("Pilih mata uang tujuan [1/2/3]: ")
            
            if conv == '1':
                kode_fx = "USD"
            elif conv == '2':
                kode_fx = "EUR"
            elif conv == '3':
                kode_fx = "SGD"
            
        elif conv == '4':
            kode_fx_awal = "SGD"
            jumlah_fx = float(input(f"Masukkan nilai mata uang dalam {kode_fx_awal}: "))
            
            while jumlah_fx <= 0:
                print("Nilai mata uang tidak boleh 0 atau kurang dari 0!")
                jumlah_fx = float(input(f"Masukkan nilai uang mata uang dalam {kode_fx_awal}: "))
            
            print("\n======================")
            print("1. USD (US Dollar)")
            print("2. EUR (Euro)")
            print("3. JPY (Yen)")
            conv = input("Pilih mata uang tujuan [1/2/3]: ")
        
            if conv == '1':
                kode_fx = "USD"
            elif conv == '2':
                kode_fx = "EUR"
            elif conv == '3':
                kode_fx = "JPY"
        
        jadi_idr = fx_to_idr(jumlah_fx, kode_fx_awal)
        jumlah_fx = format_fx(jumlah_fx, mata_uang[kode_fx_awal]['simbol'], mata_uang[kode_fx_awal]['desimal'])
        hasil = idr_to_fx(jadi_idr, kode_fx)
        hasil = format_fx(hasil, mata_uang[kode_fx]['simbol'], mata_uang[kode_fx]['desimal'])
        
        print(f"{jumlah_fx} bila dikonversi ke {kode_fx} akan menjadi: {hasil}")
              
# ================================================================================
# 5. Keluar program
    elif choice == '5':
        print("Program kalkulator mata uang selesai")
        break