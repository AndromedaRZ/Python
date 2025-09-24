# fungsi konversi panjang untuk projek konversi satuan

km = 'Kilometer (km)'
hm = 'Hektometer (hm)'
dam = 'Dekameter (dam)'
m = 'Meter (m)'
dm = 'Desimeter (dm)'
cm = 'Centimeter (cm)'
mm = 'Milimeter (mm)'

def panjang_awal():
    print(f'''\n==== Satuan Panjang ====
1. {km}
2. {hm}
3. {dam}
4. {m}
5. {dm}
6. {cm}
7. {mm}''')
    choice = input("Pilih satuan awal [1-7]: ")
    return choice

def panjang_akhir(value):
    if value == '1': # dari km
        global satuan_awal
        global nilai
        global akhir
        global nama_akhir
        
        satuan_awal = 'km'
        nilai = float(input("Masukan nilai dalam kilometer: "))
        print(f'''\n==== Satuan Panjang ====
1. {hm}
2. {dam}
3. {m}
4. {dm}
5. {cm}
6. {mm}''')
        choice2 = input("Pilih tujuan konversi [1-6]: ")
        if choice2 == '1':
            akhir = 'hm'
            nama_akhir = 'hektometer'
        elif choice2 == '2':
            akhir = 'dam'
            nama_akhir = 'dekameter'
        elif choice2 == '3':
            akhir = 'm'
            nama_akhir = 'meter'
        elif choice2 == '4':
            akhir = 'dm'
            nama_akhir = 'desimeter'
        elif choice2 == '5':
            akhir = 'cm'
            nama_akhir = 'sentimeter'
        elif choice2 == '6':
            akhir = 'mm'
            nama_akhir = 'milimeter'
        else:
            print("Satuan tidak valid!")
            
        
    elif value == "2": # dari hm
        satuan_awal = 'hm'
        nilai = float(input("Masukan nilai dalam hektometer: "))
        print(f'''\n==== Satuan Panjang ====
1. {km}
2. {dam}
3. {m}
4. {dm}
5. {cm}
6. {mm}''')
        choice2 = input("Pilih tujuan konversi [1-6]: ")
        if choice2 == '1':
            akhir = 'km'
            nama_akhir = 'kilometer'
        elif choice2 == '2':
            akhir = 'dam'
            nama_akhir = 'dekameter'
        elif choice2 == '3':
            akhir = 'm'
            nama_akhir = 'meter'
        elif choice2 == '4':
            akhir = 'dm'
            nama_akhir = 'desimeter'
        elif choice2 == '5':
            akhir = 'cm'
            nama_akhir = 'sentimeter'
        elif choice2 == '6':
            akhir = 'mm'
            nama_akhir = 'milimeter'
        else:
            print("Satuan tidak valid!")
            
            
    elif value == "3": # dari dam
        satuan_awal = 'dam'
        nilai = float(input("Masukan nilai dalam dekameter: "))
        print(f'''\n==== Satuan Panjang ====
1. {km}
2. {hm}
3. {m}
4. {dm}
5. {cm}
6. {mm}''')
        choice2 = input("Pilih tujuan konversi [1-6]: ")
        if choice2 == '1':
            akhir = 'km'
            nama_akhir = 'kilometer'
        elif choice2 == '2':
            akhir = 'hm'
            nama_akhir = 'hektometer'
        elif choice2 == '3':
            akhir = 'm'
            nama_akhir = 'meter'
        elif choice2 == '4':
            akhir = 'dm'
            nama_akhir = 'desimeter'
        elif choice2 == '5':
            akhir = 'cm'
            nama_akhir = 'sentimeter'
        elif choice2 == '6':
            akhir = 'mm'
            nama_akhir = 'milimeter'
        else:
            print("Satuan tidak valid!")
            
            
    elif value == "4": # dari m
        satuan_awal = 'm'
        nilai = float(input("Masukan nilai dalam meter: "))
        print(f'''\n==== Satuan Panjang ====
1. {km}
2. {hm}
3. {dam}
4. {dm}
5. {cm}
6. {mm}''')
        choice2 = input("Pilih tujuan konversi [1-6]: ")
        if choice2 == '1':
            akhir = 'km'
            nama_akhir = 'kilometer'
        elif choice2 == '2':
            akhir = 'hm'
            nama_akhir = 'hektometer'
        elif choice2 == '3':
            akhir = 'dam'
            nama_akhir = 'dekameter'
        elif choice2 == '4':
            akhir = 'dm'
            nama_akhir = 'desimeter'
        elif choice2 == '5':
            akhir = 'cm'
            nama_akhir = 'sentimeter'
        elif choice2 == '6':
            akhir = 'mm'
            nama_akhir = 'milimeter'
        else:
            print("Satuan tidak valid!")

        
    elif value == '5': # dari dm
        satuan_awal = 'dm'
        nilai = float(input("Masukan nilai dalam desimeter: "))
        print(f'''\n==== Satuan Panjang ====
1. {km}
2. {hm}
3. {dam}
4. {m}
5. {cm}
6. {mm}''')
        choice2 = input("Pilih tujuan konversi [1-6]: ")
        if choice2 == '1':
            akhir = 'km'
            nama_akhir = 'kilometer'
        elif choice2 == '2':
            akhir = 'hm'
            nama_akhir = 'hektometer'
        elif choice2 == '3':
            akhir = 'dam'
            nama_akhir = 'dekameter'
        elif choice2 == '4':
            akhir = 'm'
            nama_akhir = 'meter'
        elif choice2 == '5':
            akhir = 'cm'
            nama_akhir = 'sentimeter'
        elif choice2 == '6':
            akhir = 'mm'
            nama_akhir = 'milimeter'
        else:
            print("Satuan tidak valid!")
            
            
    elif value == '6': # dari cm
        satuan_awal = 'cm'
        nilai = float(input("Masukan nilai dalam sentimeter: "))
        print(f'''\n==== Satuan Panjang ====
1. {km}
2. {hm}
3. {dam}
4. {dm}
5. {m}
6. {mm}''')
        choice2 = input("Pilih tujuan konversi [1-6]: ")
        if choice2 == '1':
            akhir = 'km'
            nama_akhir = 'kilometer'
        elif choice2 == '2':
            akhir = 'hm'
            nama_akhir = 'hektometer'
        elif choice2 == '3':
            akhir = 'dam'
            nama_akhir = 'dekameter'
        elif choice2 == '4':
            akhir = 'dm'
            nama_akhir = 'desimeter'
        elif choice2 == '5':
            akhir = 'm'
            nama_akhir = 'meter'
        elif choice2 == '6':
            akhir = 'mm'
            nama_akhir = 'milimeter'
        else:
            print("Satuan tidak valid!")

                  
    elif value == '7': # dari mm
        satuan_awal = 'mm'
        nilai = float(input("Masukan nilai dalam milimeter: "))
        print(f'''\n==== Satuan Panjang ====
1. {km}
2. {hm}
3. {dam}
4. {m}
5. {dm}
6. {cm}''')
        choice2 = input("Pilih tujuan konversi [1-6]: ")
        if choice2 == '1':
            akhir = 'km'
            nama_akhir = 'kilometer'
        elif choice2 == '2':
            akhir = 'hm'
            nama_akhir = 'hektometer'
        elif choice2 == '3':
            akhir = 'dam'
            nama_akhir = 'dekameter'
        elif choice2 == '4':
            akhir = 'm'
            nama_akhir = 'meter'
        elif choice2 == '5':
            akhir = 'dm'
            nama_akhir = 'desimeter'
        elif choice2 == '6':
            akhir = 'cm'
            nama_akhir = 'sentimeter'
        else:
            print("Satuan tidak valid!")
    else:
        return "Satuan asal tidak dikenal!"
    
    return nilai, satuan_awal, nama_akhir, akhir

def konversi_panjang(**kwargs):
    nilai = kwargs.get("nilai", 0)
    dari = kwargs.get("dari", "m")
    ke = kwargs.get("ke", "cm")

    # Step 1: ubah ke meter (m)
    if dari == "km":
        m = nilai * 1000
    elif dari == 'hm':
        m = nilai * 100
    elif dari == 'dam':
        m = nilai * 10
    elif dari == "m":
        m = nilai
    elif dari == 'dm':
        m = nilai / 10
    elif dari == "cm":
        m = nilai / 100
    elif dari == "mm":
        m = nilai / 1000
    else:
        return "❌ Satuan asal tidak dikenal!"

    # Step 2: ubah dari meter ke satuan tujuan
    if ke == "km":
        hasil = m / 1000
    elif ke == 'hm':
        hasil = m / 100
    elif ke == 'dam':
        hasil = m / 10
    elif ke == "m":
        hasil = m
    elif ke == 'dm':
        hasil = m * 10
    elif ke == "cm":
        hasil = m * 100
    elif ke == "mm":
        hasil = m * 1000
    else:
        return "❌ Satuan tujuan tidak dikenal!"
    
    print(f"Jadi, {nilai} {satuan_awal} apabila dikonversikan ke {nama_akhir} akan menjadi {hasil} {akhir}")
    
