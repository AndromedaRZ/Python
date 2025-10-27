# elif = else if statement

# 1. if (kondisinya)
#       aksinya ketika kondisi if terpenuhi
# 2. elif (kondisi lain selain if)
#       aksinya ketika kondisi elif terpenuhi
# 3. else (else akan tereksekusi jika kondisi di if tidak terpenuhi)
#       aksinya

# kita bisa membuat lebih dari 1 ataupun 2 kondisi dengan menambah baris lagi menggunakan elif

nama = input("Nama kamu siapa? ")

if nama == "ucup": # kondisi 1
    print("Hai ganteeeng beuds!") # aksi True 1
elif nama == "otong": # kondisi 2
    print("Hai si kece badaiii!") # aksi True 2
else: # baris else akan tereksekusi ketika kondisi 1 dan kondisi 2 tidak terpenuhi
    print("Au ahh gak kenal!!") # aksi false
    
# jika kondisi 1 terpenuhi, maka perintah yang ada di baris indentasi setelahnya akan tereksekusi
# bergitupun hal yang sama berlaku pada konisi ke 2 (hasil dari kondisi 1, 2, maupun kondisi elif lainnya bersifat True)
# dan jika kedua kondisi di atas tidak terpenuhi, maka perintah else akan tereksekusi (hasil dari else bersifat False)

# kita bisa menambahkan elif sebanyak yang kita inginkan untuk membuat berbagai macam percabangan dan kondisi
print("Ini adalah akhir dari program")