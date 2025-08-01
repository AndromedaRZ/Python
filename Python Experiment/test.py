# program pengecek bilangan prima

print("====Memeriksa Angka Prima Atau Bukan====")
angka = int(input("Masukkan angka yang ingin diperiksa [0 untuk keluar]: "))

while True:
    if angka == 0:
        print("Hentikan program")
        break
    elif angka < 2:
        print("Bukan Bilangan prima")
        break
    else:
        for i in range(2, angka):
            if angka % i == 0:
                print("Bukan Bilangan Prima")
                break
            else:
                print("Bilangan prima")
                break
    