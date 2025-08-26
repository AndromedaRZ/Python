# Program pengeolaan nilai siswa

nilai_template = {
    'nama':'nama',
    'nilai':100
}

data_nilai = {}

while True:
    nilai = {} # dict kosong untuk menyimpan data sementara, karena ini berupa while loop, ketika perulangan terjadi maka isi dari data yang ini akan tertimpa dengan data yang baru
    
    print("""
1) Tambah siswa
2) Lihat semua siswa
3) Cari & ubah nilai siswa
4) Hapus siswa
5) Hitung statistik nilai
6) Keluar""")
    choice = input("Apa yang ingin anda lakukan?: ")
    
    if choice == '1':
        nilai['nama'] = input("Masukkan nama siswa: ").capitalize()
        if nilai['nama'] in data_nilai:
            print("\nData sudah ada!")
            continue
        
        nilai['nilai'] = int(input("Masukkan nilai siswa: "))
        if nilai['nilai'] > 100:
            print("\nNilai tidak bisa lebih dari 100!")
            continue
        KEY = nilai['nama'] # KEY ini digunakan untuk menjadikan 'nama' yang kita input sebagai key unik
        
        data_nilai[KEY] = nilai.copy() # berikutnya kita menggunakan fungsi .copy() agar datanya dipindahkan ke dictionary yang ada di luar looping
        # dan dictionary 'nilai' tadi bisa menyimpan data yang baru lalu menyalinnya ke dalam dict 'data_nilai' secara berulang
        # sehingga dict 'data_nilai' bisa menyimpan semua input nilai yang kita masukkan tanpa tertimpa satu sama lain
        
    elif choice == '2':
        if len(data_nilai) == 0:
            print("\nBelum ada data siswa dan nilai yang ditambahkan")
        else:
            print("\nDaftar nilai seluruh siswa")
            print(f"{'No':<3} {'Nama':<10} {'Nilai':<6}")
            for i,KEY in enumerate(data_nilai):
                NAMA = data_nilai[KEY]['nama']
                NILAI = data_nilai[KEY]['nilai']
                print(f"{i+1:<3} {NAMA:<10} {NILAI:<6}")
            
    elif choice == '3':
        if len(data_nilai) == 0:
            print("\nBelum ada data siswa dan nilai yang ditambahkan")
        else:
            cari_nama = input("Cari nama siswa: ").capitalize()
            if cari_nama in data_nilai:
                print("\nNama ditemukan!")
                print(f"Nama : {cari_nama}")
                print(f"Nilai: {data_nilai[cari_nama]['nilai']}")
                konfirmasi = input("Mau mengubah nilainya? (y/n): ").lower()
                if konfirmasi == 'y':
                    nilai_baru = int(input("Masukkan nilai baru: "))
                    if nilai_baru > 100:
                        print("\nNilai tidak bisa lebih dari 100")
                    else:
                        data_nilai[cari_nama]['nilai'] = nilai_baru
                else:
                    print("\nNilai tidak diubah")
                
            else:
                print("\nNama tidak ditemukan")
            
    elif choice == '4':
        if len(data_nilai) == 0:
            print("\nBelum ada data siswa dan nilai yang ditambahkan")
        else:
            print("\nDaftar nilai seluruh siswa")
            print(f"{'No':<3} {'Nama':<10} {'Nilai':<6}")
            for i,KEY in enumerate(data_nilai):
                NAMA = data_nilai[KEY]['nama']
                NILAI = data_nilai[KEY]['nilai']
                print(f"{i+1:<3} {NAMA:<10} {NILAI:<6}")
                
            hapus_nama = input("Masukkan nama siswa yang ingin dihapus: ").capitalize()
            if hapus_nama in data_nilai:
                del data_nilai[hapus_nama]
                print(f"\nNama siswa '{hapus_nama}' berhasil dihapus!")
            else:
                print("\nNama tidak valid!")
    
    elif choice == '5':
        if len(data_nilai) == 0:
            print("\nBelum ada data siswa dan nilai yang ditambahkan")
        else:
            print("\nIngin menghitung statistika apa?")
            print("1) Nilai tertinggi")
            print("2) Nilai terendah")
            print("3) Rata-rata nilai")
            opsi = input("Jawaban anda [1/2/3]: ")
            nilai_list = [siswa['nilai'] for siswa in data_nilai.values()]
            if opsi == '1':
                max_nilai = max(nilai_list)
                siswa_max = [siswa['nama'] for siswa in data_nilai.values() if siswa['nilai'] == max_nilai]
                print(f"\nNilai tertinggi: {max_nilai} oleh {', '.join(siswa_max)}")
            elif opsi == '2':
                min_nilai = min(nilai_list)
                siswa_min = [siswa['nama'] for siswa in data_nilai.values() if siswa['nilai'] == min_nilai]
                print(f"\nNilai terendah: {min_nilai} oleh {', '.join(siswa_min)}")
            elif opsi == '3':
                rata_rata = sum(nilai_list) / len(nilai_list)
                print(f"\nRata-rata nilai: {rata_rata:.2f}")
            else:
                print("\nPilihan tidak valid!")
    
    elif choice == '6':
        print("Program selesai")
        break
    
    else:
        continue