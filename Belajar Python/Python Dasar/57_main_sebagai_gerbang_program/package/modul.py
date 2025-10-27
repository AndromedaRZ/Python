def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

# program di bawah ini akan berjalan jika dijalankan pada file ini, tetapi jika dari file lain atau lewat impor function maka program ini tidak akan berjalan
if __name__ == '__main__':
    input_1 = int(input('Masukan angka pertama: '))
    input_2 = int(input('Masukan angka kedua: '))
    print(f'hasil {input_1} + {input_2} = {tambah(input_1, input_2)}')
    print(f'hasil {input_1} - {input_2} = {kurang(input_1, input_2)}')
    
