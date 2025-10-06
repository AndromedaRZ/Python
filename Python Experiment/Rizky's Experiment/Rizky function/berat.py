# fungsi konversi berat untuk projek konversi satuan

# satuan berat awal
def berat_awal():
    print('''\n==== Satuan Berat ====
1. Kilogram (kg)
2. Gram (g)
3. Pound (lbs)''')
    choice = input("Pilih satuan awal [1-3]: ")
    return choice

def berat_akhir(value):
    if value == '1':
        print('''\n==== Satuan Berat ====
1. Gram (g)
2. Pound (lbs)''')
    if value == '2':
        print('''\n==== Satuan Berat ====
1. Kilogram (kg)
2. Pound (lbs)''')
    if value == '3':
        print('''\n==== Satuan Berat ====
1. Kilogram (kg)
2. Gram (g)''')
    
    choice2 = input("Pilih satuan tujuan [1-2]: ")
    return choice2

def berat_conv(berat_awal, berat_akhir):
    if berat_awal == '1':
        satuan_awal = 'kg'
        nilai = float(input("Masukan berat dalam kilogram: "))
        if berat_akhir == '1':
            hasil = nilai * 1000
            nama_satuan_akhir = 'gram'
            satuan_akhir = 'g'
        elif berat_akhir == '2':
            hasil = nilai * 2.20462
            nama_satuan_akhir = 'pound'
            satuan_akhir = 'lbs'
    elif berat_awal == '2':
        satuan_awal = 'g'
        nilai = float(input("Masukan berat dalam gram: "))
        if berat_akhir == '1':
            hasil = nilai / 1000
            nama_satuan_akhir = 'kilogram'
            satuan_akhir = 'kg'
        elif berat_akhir == '2':
            hasil = nilai / 453.592
            nama_satuan_akhir = 'pound'
            satuan_akhir = 'lbs'
    elif berat_awal == '3':
        satuan_awal = 'lbs'
        nilai = float(input("Masukan berat dalam pound: "))
        if berat_akhir == '1':
            hasil = nilai / 0.453592
            nama_satuan_akhir = 'kilogram'
            satuan_akhir = 'kg'
        elif berat_akhir == '2':
            hasil = nilai * 453.592
            nama_satuan_akhir = 'gram'
            satuan_akhir = 'g'
            
    else:
        print('Input tidak valid!')
        
    print(f'Jadi, {nilai:,.1f} {satuan_awal} apabila dikonversikan ke {nama_satuan_akhir} akan menjadi {hasil:,.1f} {satuan_akhir}')
            
            
    