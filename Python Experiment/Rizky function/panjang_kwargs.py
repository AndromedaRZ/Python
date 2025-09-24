# konversi satuan panjang menggunakan kwargs pada function

# Dictionary konversi satuan ke meter
satuan_ke_meter = {
    "km": 1000,
    "hm": 100,
    "dam": 10,
    "m": 1,
    "dm": 0.1,
    "cm": 0.01,
    "mm": 0.001
}

def konversi_panjang(**kwargs):
    '''Fungsi konversi panjang menggunakan kwargs
    keterangan:
    - nilai : angka atau nilai yang ingin dikonversi
    - dari  : satuan asal (km, hm, dam, m, dm, cm, mm)
    - ke    : satuan akhir (km, hm, dam, m, dm, cm, mm)'''
    
    # nilai = kwargs['nilai']
    # dari = kwargs['dari']
    # ke = kwargs['ke']
    
    nilai = kwargs.get('nilai', 0) # variabel untuk menyimpan nilai hasil dari mengakses nilai di dalam kwargs
    dari = kwargs.get('dari', 'm') # variabel untuk menyimpan nilai hasil dari mengakses satuan awal di dalam kwargs
    ke = kwargs.get('ke', 'cm') # variabel untuk menyimpan nilai hasil dari mengakses satuan akhir di dalam kwargs
    
    if dari not in satuan_ke_meter or ke not in satuan_ke_meter:
        print(f'Satuan tidak valid!')
        return 
    
    # konversi ke satuan meter terlebih dahulu
    meter = nilai * satuan_ke_meter[dari] # mengakses dictionary 'satuan_ke_meter' menggunakan salah satu key yang ada di dalam kwargs fungsi ini untuk mengambil valuenya berdasarkan satuan awal nya
    
    # konversi ke satuan tujuan
    hasil = meter / satuan_ke_meter[ke]  # mengakses dictionary 'satuan_ke_meter' menggunakan salah satu key yang ada di dalam kwargs fungsi ini untuk mengambil valuenya berdasarkan satuan akhir nya
    
    print(f"{nilai} {dari} = {hasil} {ke}")
    
    
def menu_konversi_panjang():
    print("\n==== Satuan Panjang ====")
    print("Pilih satuan berikut:")
    print("1. Kilometer (km)")
    print("2. Hektometer (hm)")
    print("3. Dekameter (dam)")
    print("4. Meter (m)")
    print("5. Desimeter (dm)")
    print("6. Centimeter (cm)")
    print("7. Milimeter (mm)")
    
    pilihan = {
        "1": "km",
        "2": "hm",
        "3": "dam",
        "4": "m",
        "5": "dm",
        "6": "cm",
        "7": "mm"
    }


    # pilih satuan awal
    awal = input("Pilih satuan awal [1-7]: ")
    satuan_awal = pilihan.get(awal, None) # mengakses key dari dictionary 'pilihan' menggunakan nilai dari variabel 'awal' agar bisa dicocokan dengan key yang ada di dalam dictionary 'pilihan'
    
    # input nilai berat
    nilai = float(input("Masukan nilai awal: "))
    
    # pilih satuan tujuan
    akhir = input("Pilih satuan tujuan [1-7]: ")
    satuan_akhir = pilihan.get(akhir, None) # mengakses key dari dicitonary 'pilihan' menggunakan nilai dari variabel 'akhir' agar bisa dicocokan dengan key yang ada di dalam dictionary 'pilihan'
    
    konversi_panjang(nilai=nilai, dari=satuan_awal, ke=satuan_akhir)

menu_konversi_panjang()