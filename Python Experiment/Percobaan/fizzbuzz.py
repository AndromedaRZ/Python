# Fizzbuzz adalah permainan kata kelompok untuk anak-anak yang belajar operasi pembagian dalam matematika, permainan berhitung secara bertahap dimulai dari angka 1 lalu mengganti angka yang habis jika dibagi dengan angka 3 dengan kata "Fizz", mengganti angka yang habis jika dibagi dengan angka 5 dengan kata "Buzz" ,dan mengganti angka apa pun yang habis jika dibagi angka 3 dan 5 dengan kata "Fizzbuzz".

for n in range(1, 101): # melakukan perulangan angka dari angka 1 hingga 100
    if n % 3 == 0 and n % 5 == 0: # Mengecek apakah angka yang keluar (n) akan habis dibagi 3 dan 5 
         print("FizzBuzz") # Jika iya, maka akan diganti dangan kata "FizzBuzz"
    elif n % 3 == 0: # Jika tidak, cek apakah hanya habis dibagi 3
        print("Fizz") # Jika iya, maka akan diganti dengan kata "Fizz"
    elif n % 5 == 0: # Jika tidak, cek apakah hanya habis dibagi 5
        print("Buzz") # Jika iya, maka akan diganti dengan kata "Buzz"
    else: # Jika angka nya tidak habis dibagi 3 dan 5
        print(n) # Maka angka nya akan muncul secara normal
