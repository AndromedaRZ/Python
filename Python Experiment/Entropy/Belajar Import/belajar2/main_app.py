# Program konversi suhu dan berat

from konversi import suhu, berat

while True:
    print("""\n=== Program konversi ===
1. Konversi Suhu
2. Konversi Berat
3. Keluar""")
    
    choice = input("Apa yang ingin anda lakukan? [1-3]: ")
    if choice == '1':
        suhu_awal = suhu.suhu_awal()
        if int(suhu_awal) > 4:
            print("\nInput tidak valid!")
            continue
        
        suhu_akhir = suhu.suhu_akhir(nilai = suhu_awal)
        if int(suhu_akhir) > 3:
            print("\nInput tidak valid!")
            continue
            
        suhu.suhu_conv(suhu_awal = suhu_awal, suhu_akhir = suhu_akhir)
        
    elif choice == '2':
        berat_awal = berat.berat_awal()
        if int(berat_awal) > 3:
            print("\nInput tidak valid!")
            continue
            
        berat_akhir = berat.berat_akhir(nilai = berat_awal)
        if int(berat_akhir) > 2:
            print("\nInput tidak valid!")
            continue
         
        berat.berat_conv(berat_awal = berat_awal, berat_akhir = berat_akhir)
        
        
    elif choice == '3':
        print("\nProgram selesai.")
        break
    