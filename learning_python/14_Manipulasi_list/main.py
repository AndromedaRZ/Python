## Operasi manipulasi data list

# di dalam sebuah list ada yang namanya index, urutan atau index biasanya diawali dari index ke-0 sampai tergantung banyak data yang ada di dalam list
# untuk mempermudah pengetikan dan pemahaman program, kita akan menggunakan index sebagai acuannya karena itu adalah hal yang dipahami oleh komputer

# index   0        1        2
data = ["Ryan","Zidane","Herman"]
# atau jika kita ingin memulainya dari index negatif bisa seperti ini:
# index   -3      -2       -1
data = ["Ryan","Zidane","Herman"]

# mengambil data dari list
data_0 = data[0]
print("Data pertama (index 0) =",data_0)
# atau kita juga bisa mempersingkat perintahnya dengan cara di bawah ini sehingga kita tidak perlu membuat variabel baru
print(f"data pertama (index 0) = {data[0]}")

# pada nama variabel list tersebut kita tambahkan kurung siku setelah variabelnya dan masukkan index data yang kita inginkan di dalam kurung siku tersebut
# contoh: data[0] -> maksudnya adalah kita mengambil data index ke-0 dari variabel data menggunakan kurung siku, kita tinggal menggunakan perintah print() untuk menampilkan isinya seperti baris perintah sebelumnya

# jika kita ingin mengambil data ke terakhir tapi tidak tahu seberapa banyak data yang dimiliki dari listnya
# maka alternatifnya kita bisa memasukkan index ke (-1) dari datanya, contoh:
print(f"Data terakhirnya adalah {data[-1]}")

# kita perlu memahami terlebih dahulu penggunaan dari kurung siku untuk list, dan kurung kurawal untuk f-string agar tidak membingungkan diri kita sendiri

# Ada kalanya kita tidak tahu panjang atau banyaknya data yang kita pegang, cara menghitungnya adalah dengan menggunakan perintah len()
print(f"Panjang data = {len(data)}")

# contoh data panjang
data_panjang_hobi = ["memasak","bermain game","membaca buku","mengetik","menulis","bermain bola","bermain bulutangkis","bersepeda","ngoding"]
print("Panjang data hobi adalah",len(data_panjang_hobi)) # kita hanya perlu menggunakan perintah len() untuk mengetahuinya

## Memanipulasi data list

# menambahkan item atau data baru ke dalam list sesuai posisi yang kita ingingkan
print(f"\nData sebelum ditambah:\n{data}") 

data.insert(1,"Farel") # kita bisa menggunakan .insert setelah variabelnya dan memasukkan data ke dalam index ke berapa sesuai keinginan kita
# rumusnya seperti ini .insert(index ke berapa, data atau nilai yang ingin dimasukkan)
# nantinya index tempat data sebelumnya ditempati akan bergeser ke index berikutnya begitupun hal yang sama berlaku untuk index yang lain
print(f"\nData sesudah ditambah:\n{data}")

# menambah di akhir list
data.append("Tono") # fungsinya hampir mirip seperti .insert hanya saja .append berfungsi untuk langsung menambahkan data yang kita inginkan ke dalam index ataupun urutan terakhir
# rumusnya: .append(data atau nilai yang kita ingin masukkan)
print(f"\nData ditambah lagi:\n{data}")

# menambah list dengan list (atau bisa dikatakan menggabungkan list)
data_baru = ["Luna","Ani","Tina"]

data.extend(data_baru) # .extend() berfungsi untuk memasukkan data list yang 1 dengan yang lain
# data list yang ingin kita tambahkan kita tempatkan di depan extend -> data.extend()
# dan isi dari kurung .extend adalah data list yang ingin kita ambil
# .extend(data list yang ingin diambil)

print(f"\nData gabungan :\n{data}")

# mengubah data
data[1] = "Fairuz" # index ke-1 pada variabel list 'data' diubah menjadi "Fairuz"
# kita bisa melakukan hal yang serupa pada index yang lain menggunakan kurung siku seperti di atas
print(f"\nData yang sudah diubah:\n{data}")

# menghapus data
data.remove("Tono") # tambahkan .remove() lalu isi kurung di dalam dengan data yang kita inginkan terhapus, fungsi ini juga bersifat case sensitif jadi pastikan data yang diketik di .remove() sesuai dengan data yang ada di list
print(f"\nData yang sudah dihapus:\n{data}")

# menghapus data terakhir
data_terakhir = data.pop() # data terakhir akan langsung terhapus ketika kita menambahkan .pop()
print(f"\nHasil data terakhir yang sudah dihapus:\n{data}")

print(f"Data terakhirnya adalah {data_terakhir}") # tapi sebenarnya datanya masih disimpan jika kita memasukkannya ke dalam variabel dan bisa kita tampilan dengan menggunakan perintah print()