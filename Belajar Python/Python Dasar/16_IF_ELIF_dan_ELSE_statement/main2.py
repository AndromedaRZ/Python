# ELIF = else if statement

# ELIF adalah kondisi ELSE IF, hampir mirip dengan ELSE tetapi digunakan pada kondisi sebelum ELSE, ELSE jika bisa digunakan sebanyak mungkin tidak terbatas hanya 1

nama = input("Nama kamu siapa? ")

if nama == "ucup": # kondisi 1
    print("Halo ucup ganteng!") # aksi 1 jika kondisi 1 true
elif nama == "otong": # kondisi 2
    print("Kamu ngapain otong?!") # aksi 2 jika kondisi 2 true
elif nama == "mario": # kondisi 3
    print("Hai mario si humories!") # aksi 3 jika kondisi 3 true       
else: 
    print("Kamu tidak dikenal!") # aksi false
    
print("Program berhenti")