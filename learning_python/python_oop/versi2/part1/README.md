OOP (Object Oriented Programming)

Object-Oriented Programming (OOP) adalah paradigma programming yang mengorganisir code berdasarkan objects dan classes
Bayangkan OOP seperti cara kita berpikir dalam kehidupan nyata:
setiap benda memiliki karakteristik (properties) dan kemampuan (behaviors)

Contoh sederhana:
- mobil memiliki karakteristik  : warna, merk, tahun
- mobil memiliki kemampuan      : maju, mundur, belok, klakson
--> mobil adalah sebuah object


Jika dalam OOP:
- Karakteristik = Attributes (variables dalam object)
- Kemampuan     = Methods (function dalam object)


Apa keuntungan menggunakan Object-Oriented Programming?
- Data dan Behavior tergabung dalam satu unit (jadi memudahkan kita untuk memaintain setiap variabel agar tidak berantakan)
- Lebih mudah dipahaim dan dimaintain
- Reusable: bisa buat multiple instances
- Data protection: tidak mudah corrupt
- Scalable untuk sistem yang kompleks

4 Pilar dalam Object-Oriented Programming

1. Encapsulation (pembungkusan), yaitu menggabungkan data dan methods dalam satu unit (class), dan menyembunyikan detail implementasi
2. Inheritance (pewarisan), child class mewarisi properties dan methods dari parent class (atau bisa juga disebut sub class mewarisi dari super class)
3. Polymorphism (banyak bentuk), object yang berbeda bisa merespon method call yang sama dengan cara yang berbeda
4. Abstraction (abstraksi), menyembunyikan complexity dan hanya menampilkan interface yang penting


Real-World Analogies (analogi pada kehidupan nyata)

Pabrik mobil

class   = blueprint/cetakan mobil
nantinya class ini digunakan untuk mendapat data mobil, dari class ini kita memiliki sebuah object

object  = mobil yang diproduksi dari blueprint
kita cukup membuat 1 class, maka kita bisa membuat banyak object (mobil) dengan karakteristik yang sama tanpa perlu mengisi datanya satu per satu

attributes = warna, mesin, roda
attribute ini digunakan di dalam class agar semua object bisa memiliki karakteristik yang sama, jadi kita hanya perlu membuat object baru maka datanya akan sama dengan yang lain

mehtods = maju, mundur, klakson
bisa dikatakan ini adalah semacam fitur apa yang kita inginkan dari object (mobil) tersebut
dengan menggunakan class, maka kita bisa membuat banyak mobil sekaligus dengan methods (fitur) yang sama tanpa perlu menambahkannya ke dalam object secara manual satu per satu




