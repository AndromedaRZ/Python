# GUI --> Graphical User Interface

# Menggunakan library tkinter untuk membuat outputnya menjadi gui

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
window = tk.Tk()
window.configure(bg='white') # mengubah background guinya
window.geometry("400x200") # mengubah ukuran guinya, lebar x panjang
window.resizable(False, False) # untuk mengatur apakah lebar atau panjang guinya bisa diatur saat dijalankan atau tidak
window.title("Hello Friend!")

# variabel dan fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_klik():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, pintar!"
    showinfo(title='pesan', message=pesan)

# frame input
input_frame = ttk.Frame(window)

# ada 3 penempatan dalam frame, Grid, Pack, dan Place
input_frame.pack(padx=10, pady=10, fill='x', expand=True)

# komponen - komponen
# 1. label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan")
nama_depan_label.pack(padx=10, fill='x', expand=True)

# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill='x', expand=True)

# 3. label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang")
nama_belakang_label.pack(padx=10, fill='x', expand=True)

# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill='x', expand=True)

# 5. Tombol
tombol_sapa = ttk.Button(input_frame, text='Sapa', command=tombol_klik)
tombol_sapa.pack(fill='x', expand=True, padx=10, pady=10)

# Main loop window
window.mainloop()