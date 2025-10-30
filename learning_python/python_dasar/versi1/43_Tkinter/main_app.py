# GUI -> Graphical User Interface

# untuk informasi lebih dalam lagi
# kita bisa mengakses website dari tkinter ini
# https://docs.python.org/3/library/tkinter.html
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk() # membuat variabel window menjadi sebuah object
# tapi harusnya floating window sudah bisa muncul, namun sistem langsung menutupnya kembali setelah mengeksekusinya

# init
window.configure(bg = "white") # mengatur warna background
window.geometry("300x200") # mengatur ukuran window
window.resizable(False, False) # mengatur floating window apakah ukuran windownya bisa di resize atau tidak (x: False, y: false)
window.title("Sapa dia!") # mengatur judul atau nama yang muncul pada floating windownya

# variabel dan fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Ganteeeng!!"
    showinfo(title="Whazzup!", message=pesan)

# frame input
input_frame = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(padx=10, pady=10, fill='x', expand=True)

# komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text='Nama depan:')
nama_depan_label.pack(padx=10, fill='x', expand=True)
# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill='x', expand=True)
# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text='Nama belakang:')
nama_belakang_label.pack(padx=10, fill='x', expand=True)
# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill='x', expand=True)
# 5. Tombol
tombol_sapa = ttk.Button(input_frame, text= 'Sapa!', command=tombol_click)
tombol_sapa.pack(fill='x', expand=True, padx=10, pady=10)

# mainloop window
window.mainloop() # mainloop() berfungsi agar floating window tetap standby sampai kita tutup secara manual 