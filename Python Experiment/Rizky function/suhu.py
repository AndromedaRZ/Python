# fungsi konversi suhu untuk projek konversi satuan

# celcius to another
def celcius_to_fahrenheit(nilai):
    return (nilai * 9/5) + 32 

def celcius_to_reamur(nilai):
    return nilai * 4/5

def celcius_to_kelvin(nilai):
    return nilai + 273

def celcius_conv():
    value = float(input("Masukan nilai suhu yang ingin dikonversikan ?°C: "))
    print('\n=== Pilih tujuan satuan suhu ===')
    print('''1. Fahrenheit
2. Reamur
3. Kelvin''')
    choice = input("Pilih [1-3]: ")
    if choice == '1':
        hasil = celcius_to_fahrenheit(value)
        print(f'Jadi, {value}°C apabila dikonversikan ke fahrenheit akan menjadi {hasil}°F')
        
    elif choice == '2':
        hasil = celcius_to_reamur(value)
        print(f'Jadi, {value}°C apabila dikonversikan ke reamur akan menjadi {hasil}°R')
    
    if choice == '3':
        hasil = celcius_to_kelvin(value)
        print(f'Jadi, {value}°C apabila dikonversikan ke kelvin akan menjadi {hasil}°K')
        
# fahrenheit to another
def fahrenheit_to_celcius(nilai):
    return (nilai - 32) * 5/9

def fahrenheit_to_reamur(nilai):
    return (nilai - 32) * 4/9

def fahrenheit_to_kelvin(nilai):
    return (nilai - 32) * 5/9 + 273

def fahrenheit_conv():
    value = float(input("Masukan nilai suhu yang ingin dikonversikan ?°F: "))
    print('\n=== Pilih tujuan satuan suhu ===')
    print('''1. Celcius
2. Reamur
3. Kelvin''')
    choice = input("Pilih [1-3]: ")
    if choice == '1':
        hasil = fahrenheit_to_celcius(value)
        print(f'Jadi, {value}°F apabila dikonversikan ke celcius akan menjadi {hasil}°C')
        
    elif choice == '2':
        hasil = fahrenheit_to_reamur(value)
        print(f'Jadi, {value}°F apabila dikonversikan ke reamur akan menjadi {hasil}°R')
    
    if choice == '3':
        hasil = fahrenheit_to_kelvin(value)
        print(f'Jadi, {value}°F apabila dikonversikan ke kelvin akan menjadi {hasil}°K')
        
# reamur to another
def reamur_to_celcius(nilai):
    return nilai * 5/4

def reamur_to_fahrenheit(nilai):
    return (nilai * 9/4) + 32

def reamur_to_kelvin(nilai):
    return (nilai * 5/4) + 273
    
def reamur_conv():
    value = float(input("Masukan nilai suhu yang ingin dikonversikan ?°R: "))
    print('\n=== Pilih tujuan satuan suhu ===')
    print('''1. Celcius
2. Fahrenheit
3. Kelvin''')
    choice = input("Pilih [1-3]: ")
    if choice == '1':
        hasil = reamur_to_celcius(value)
        print(f'Jadi, {value}°R apabila dikonversikan ke celcius akan menjadi {hasil}°C')
        
    elif choice == '2':
        hasil = reamur_to_fahrenheit(value)
        print(f'Jadi, {value}°R apabila dikonversikan ke fahrenheit akan menjadi {hasil}°F')
    
    if choice == '3':
        hasil = reamur_to_kelvin(value)
        print(f'Jadi, {value}°R apabila dikonversikan ke kelvin akan menjadi {hasil}°K')
    
# kelvin to another
def kelvin_to_celcius(nilai):
    return nilai - 273

def kelvin_to_fahrenheit(nilai):
    return (nilai - 273) * 9/5 + 32

def kelvin_to_reamur(nilai):
    return (nilai - 273) * 4/5

def kelvin_conv():
    value = float(input("Masukan nilai suhu yang ingin dikonversikan ?°K: "))
    print('\n=== Pilih tujuan satuan suhu ===')
    print('''1. Celcius
2. Fahrenheit
3. Reamur''')
    choice = input("Pilih [1-3]: ")
    if choice == '1':
        hasil = kelvin_to_celcius(value)
        print(f'Jadi, {value}°K apabila dikonversikan ke celcius akan menjadi {hasil}°C')
        
    elif choice == '2':
        hasil = kelvin_to_fahrenheit(value)
        print(f'Jadi, {value}°K apabila dikonversikan ke fahrenheit akan menjadi {hasil}°F')
    
    if choice == '3':
        hasil = kelvin_to_reamur(value)
        print(f'Jadi, {value}°K apabila dikonversikan ke reamur akan menjadi {hasil}°R')
