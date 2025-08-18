
print("KONVERSI SATUAN WAKTU")

while True:
    print("""\n
Satuan waktu mana yang ingin anda konversi?
1) Hari
2) Jam
3) Menit
4) Detik""")
    pilihan_waktu = int(input("Jawaban anda [1-4]: "))

    while pilihan_waktu > 4:
        pilihan_waktu = int(input("Pilih di antara 1 sampai 4: "))
        
    if pilihan_waktu == 1:
        waktu_hari = int(input("Masukkan nilai waktu dalam satuan Hari: "))
        hasil_jam = waktu_hari * 24
        hasil_menit = waktu_hari * 24 * 60
        hasil_detik = waktu_hari * 24 * 60 * 60
        
        print(f"{waktu_hari} hari = {hasil_jam} jam")
        print(f"{waktu_hari} hari = {hasil_menit} menit")
        print(f"{waktu_hari} hari = {hasil_detik} detik")
        
    elif pilihan_waktu == 2:
        waktu_jam = int(input("Masukkan nilai waktu dalam satuan Jam: "))
        hasil_hari = waktu_jam / 24
        hasil_menit = waktu_jam * 60
        hasil_detik = waktu_jam * 60 * 60
        
        print(f"{waktu_jam} jam = {hasil_hari} hari")
        print(f"{waktu_jam} jam = {hasil_menit} menit")
        print(f"{waktu_jam} jam = {hasil_detik} detik")
        
    elif pilihan_waktu == 3:
        waktu_menit = int(input("Masukkan nilai waktu dalam satuan Menit: "))
        hasil_hari = waktu_menit / 60 / 24
        hasil_jam = waktu_menit / 60
        hasil_detik = waktu_menit * 60
        
        print(f"{waktu_menit} menit = {hasil_hari} hari")
        print(f"{waktu_menit} menit = {hasil_jam} jam")
        print(f"{waktu_menit} menit = {hasil_detik} detik")
        
    elif pilihan_waktu == 4:
        waktu_detik = int(input("Masukkan nilai waktu dalam satuan Detik: "))
        hasil_hari = waktu_detik / 60 / 60 / 24
        hasil_jam = waktu_detik / 60 / 60
        hasil_menit = waktu_detik / 60
        
        print(f"{waktu_detik} detik = {hasil_hari} hari")
        print(f"{waktu_detik} detik = {hasil_jam} jam")
        print(f"{waktu_detik} detik = {hasil_menit} menit")
        
    decide = input("\nApakah masih ingin mengonversi? [y/n]")
    
    if decide == "n":
        break
    
print("Program selesai")
    