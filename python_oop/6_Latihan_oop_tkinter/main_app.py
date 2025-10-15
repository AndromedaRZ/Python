# beberapa package misalnya tkinter, menggunakan oop untuk membangun library-nya

import tkinter as tk

main_window = tk.Tk() # 'Tk()' ini adalah sebuah object, yang artinya Tk ini terbuat dari oop di dalamnya
# main_window kita jadikan sebagai object

label1 = tk.Label(main_window, text = 'label1') # memasukkan 'main_window' yang juga merupakan object sebagai argument
label2 = tk.Label(main_window, text = 'label2')

tombol1 = tk.Button(main_window, text = 'tombol1')
tombol2 = tk.Button(main_window, text = 'tombol2')

# method positioning
label1.pack()
label2.pack()
tombol1.pack()


# method menampilkan GUI-nya
main_window.mainloop()

# pada bahasa pemrogramman Python
# setiap 'class' diawali dengan huruf kapital
# contohnya seperti 'Label' dan 'Button' di atas
# sedangkan jika tidak diawali dengan huruf kapital
# maka itu adalah method-nya
# kedua hal itu berlaku ketika kita membuat class dan juga berlaku kepada libray lain (contoh di atas adalah ketika kita mengimport library tkinter)