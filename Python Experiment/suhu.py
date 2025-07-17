# Konversi satuan suhu dalam python

celcius = 0
reamur = 0
fahrenheit = 0
kelvin = 0

print('''
Satuan suhu mana yang ingin anda konversikan?:
1) Celcius 
2) Reamur
3) Fahrenheit
4) Kelvin
''')
decide = int(input('Jawaban anda [1-4]: '))

while decide > 4:
    decide = int(input('Jawaban anda [1-4]: '))
if decide == 1:
    celc = float(input('Berapa derajat suhu yang ingin anda masukkan dalam satuan Celcius? '))
    celcius = celcius + celc
    print('''
Ingin dikonversikan ke satuan apa?
1) Reamur
2) Fahrenheit
3) Kelvin''')
    decided_celc = int(input('Jawaban anda [1-3]: '))
    while decided_celc > 3:
        decided_celc = int(input('Jawaban anda [1-3]: '))
    if decided_celc == 1:
        reamur = 4 / 5 * celcius
        print(f'\nJadi, suhu {celcius} C bila dikonversikan menjadi Reamur akan menjadi:')
        print(f'{reamur} R')
        
    if decided_celc == 2:
        fahrenheit = 9 / 5 * celcius + 32
        print(f'\nJadi suhu {celcius} C bila dikonversikan menjadi Fahrenheit akan menjadi:')
        print(f'{fahrenheit} F')
        
    if decided_celc == 3:
        kelvin = celcius + 273
        print(f'\nJadi suhu {celcius} C bila dikonversikan menjadi Kelvin akan menjadi:')
        print(f'{kelvin} K')
        
if decide == 2:
    ream = float(input('Berapa derajat suhu yang ingin anda masukkan dalam satuan Reamur? '))
    reamur = reamur + ream
    print('''
Ingin dikonversikan ke satuan apa?
1) Celcius
2) Fahrenheit
3) Kelvin''')
    decided_ream = int(input('Jawaban anda [1-3]: '))
    while decided_ream > 3:
        decided_ream = int(input('Jawaban anda [1-3]: '))
    if decided_ream == 1:
        celcius = 5 / 4 * reamur
        print(f'\nJadi suhu {reamur} bila dikonversikan menjadi Celcius akan menjadi:')
        print(f'{celcius} C')
        
    if decided_ream == 2:
        fahrenheit = 9 / 4 * reamur + 32
        print(f'\nJadi suhu {reamur} bila dikonversikan menjadi Fahrenheit akan menjadi:')
        print(f'{fahrenheit} F')
        
    if decided_ream == 3:
        kelvin = 5 / 4 * reamur + 273
        print(f'\nJadi suhu {reamur} bila dikonversikan menjadi Kelvin akan menjadi:')
        print(f'{kelvin} K')
        
if decide == 3:
    fah = float(input('Berapa derajat suhu yang ingin anda masukkan dalam satuan Fahrenheit? '))
    fahrenheit = fahrenheit + fah
    print('''
Ingin dikonversikan ke satuan apa?
1) Celcius
2) Reamur
3) Kelvin''')
    decided_fah = int(input('Jawaban anda [1-3]: '))
    while decided_fah > 3:
        decided_fah = int(input('Jawaban anda [1-3]: '))
    if decided_fah == 1:
        celcius = 5 / 9 * (fahrenheit - 32)
        print(f'\nJadi, suhu {fahrenheit} F bila dikonversikan menjadi Celcius akan menjadi:')
        print(f'{celcius} C')
        
    if decided_fah == 2:
        reamur = 4 / 9 * (fahrenheit - 32)
        print(f'\nJadi suhu {fahrenheit} F bila dikonversikan menjadi Reamur akan menjadi:')
        print(f'{reamur} R')
        
    if decided_fah == 3:
        kelvin = 5 / 9 * (fahrenheit - 32) + 273
        print(f'\nJadi suhu {fahrenheit} F bila dikonversikan menjadi Kelvin akan menjadi:')
        print(f'{kelvin} K')
        
if decide == 4:
    kelv = float(input('Berapa derajat suhu yang ingin anda masukkan dalam satuan Kelvin? '))
    kelvin = kelvin + kelv
    print('''
Ingin dikonversikan ke satuan apa?
1) Celcius
2) Reamur
3) Fahrenheit''')
    decided_kelv = int(input('Jawaban anda [1-3]: '))
    while decided_kelv > 3:
        decided_kelv = int(input('Jawaban anda [1-3]: '))
    if decided_kelv == 1:
        celcius = kelvin - 273
        print(f'\nJadi, suhu {kelvin} K bila dikonversikan menjadi Celcius akan menjadi:')
        print(f'{celcius} C')
        
    if decided_kelv == 2:
        reamur = 4 / 5 * (kelvin - 273)
        print(f'\nJadi suhu {kelvin} K bila dikonversikan menjadi Reamur akan menjadi:')
        print(f'{reamur} R')
        
    if decided_kelv == 3:
        fahrenheit = 9 / 5 * (kelvin - 273) + 32
        print(f'\nJadi suhu {kelvin} K bila dikonversikan menjadi Fahrenheit akan menjadi:')
        print(f'{fahrenheit} K')