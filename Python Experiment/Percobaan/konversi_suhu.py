# Program konversi satuan suhu

celcius = 0
fahrenheit = 0
kelvin = 0
reamur = 0

print("===== Program konversi satuan suhu menggunakan python =====")
print('''Pilih satuan suhu yang ingin anda konversikan.
1) Celcius
2) Fahrenheit
3) Kelvin
4) Reamur''')
pilihan = int(input("Jawaban anda [1-4]: "))

while pilihan > 4:
    pilihan = int(input("Jawaban anda [1-4]: "))

if pilihan == 1:
    celcius = float(input("\nBerapa derajat Celcius yang ingin anda konversikan?: "))
    
    print('''\nIngin dikonversikan ke satuan suhu apa?
1) Fahrenheit
2) Kelvin
3) Reamur''')
    pilihan2 = int(input("Jawaban anda [1-3]: "))
    while pilihan2 > 3:
        pilihan2 = int(input("Jawaban anda [1-3]: "))
    
    if pilihan2 == 1:
        fahrenheit = (celcius * 9/5) + 32
        print(f'Jadi, suhu {celcius} C jika dikonversikan ke Fahreheit akan menjadi {fahrenheit} F')
    elif pilihan2 == 2:
        kelvin = celcius + 273
        print(f'Jadi, suhu {celcius} C jika dikonversikan ke Kelvin akan menjadi {kelvin} K')
    elif pilihan2 == 3:
        reamur = celcius * 4/5
        print(f"Jadi, suhu {celcius} C jika dikonversikan ke Reamur akan menjadi {reamur} R")
    
if pilihan == 2:
    fahrenheit = float(input("\nBerapa derajat Fahrenheit yang ingin anda konversikan?: "))
    
    print('''\nIngin dikonversikan ke satuan suhu apa?
1) Celcius
2) Kelvin
3) Reamur''')
    pilihan2 = int(input("Jawaban anda [1-3]: "))
    while pilihan2 > 3:
        pilihan2 = int(input("Jawaban anda [1-3]: "))
        
    if pilihan2 == 1:
        celcius = (fahrenheit - 32) * 5/9
        print(f'Jadi, suhu {fahrenheit} F jika dikonversikan ke Fahreheit akan menjadi {celcius} C')
    elif pilihan2 == 2:
        kelvin = (fahrenheit - 32) * 5/9 + 273
        print(f'Jadi, suhu {fahrenheit} F jika dikonversikan ke Fahreheit akan menjadi {kelvin} K')
    elif pilihan2 == 3:
        reamur = (fahrenheit - 32) * 4/9
        print(f'Jadi, suhu {fahrenheit} F jika dikonversikan ke Fahreheit akan menjadi {reamur} R')
        
if pilihan == 3:
    kelvin = float(input("\nBerapa derajat Kelvin yang ingin anda konversikan?: "))
    
    print('''\nIngin dikonversikan ke satuan suhu apa?
1) Celcius
2) Fahrenheit
3) Reamur''')
    pilihan2 = int(input("Jawaban anda [1-3]: "))
    while pilihan2 > 3:
        pilihan2 = int(input("Jawaban anda [1-3]: "))
        
    if pilihan2 == 1:
        celcius = kelvin - 273
        print(f'Jadi, suhu {kelvin} K jika dikonversikan ke Fahreheit akan menjadi {celcius} C')
    elif pilihan2 == 2:
        fahrenheit = (kelvin - 273) * 9/5 + 32
        print(f'Jadi, suhu {kelvin} K jika dikonversikan ke Fahreheit akan menjadi {fahrenheit} F')
    elif pilihan2 == 3:
        reamur = (kelvin - 273) * 4/5
        print(f'Jadi, suhu {kelvin} K jika dikonversikan ke Fahreheit akan menjadi {reamur} R')
        
if pilihan == 4:
    reamur = float(input("\nBerapa derajat Reamur yang ingin anda konversikan?: "))

    print('''\nIngin dikonversikan ke satuan suhu apa?
1) Celcius
2) Fahrenheit
3) Kelvin''')
    pilihan2 = int(input("Jawaban anda [1-3]: "))
    while pilihan2 > 3:
        pilihan2 = int(input("Jawaban anda [1-3]: "))
    
    if pilihan2 == 1:
        celcius = reamur * 5/4
        print(f'Jadi, suhu {reamur} R jika dikonversikan ke Fahreheit akan menjadi {celcius} C')
    elif pilihan2 == 2:
        fahrenheit = (reamur * 9/4) + 32
        print(f'Jadi, suhu {reamur} R jika dikonversikan ke Fahreheit akan menjadi {fahrenheit} F')
    elif pilihan2 == 3:
        kelvin = (reamur * 5/4) + 273
        print(f'Jadi, suhu {reamur} R jika dikonversikan ke Fahreheit akan menjadi {kelvin} K')
    
    