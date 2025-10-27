# Latihan program menggunakan for loop

# menghitung faktorial dari suatu nilai yang diinput user

print("\n====Prorgam menghitung faktorial suatu bilangan====")
angka = int(input("Masukan bilangan: "))

faktorial = 1
for i in range(1, angka + 1):
    faktorial *= i

print(f"Faktorial {angka} = {faktorial}")

