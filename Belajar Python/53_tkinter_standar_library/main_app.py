# GUI --> Graphical User Interface

# Menggunakan library tkinter untuk membuat outputnya menjadi gui

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(bg='white') # mengubah background guinya
window.geometry("400x200") # mengubah ukuran guinya, lebar x panjang
window.resizable(False, False) # untuk mengatur apakah lebar atau panjang guinya bisa diatur saat dijalankan atau tidak
window.title("Hello Friend!")

# frame input
input_frame = ttk.Frame(window)

# ada 3 penempatan dalam frame, Grid, Pack, dan Place
input_frame.pack(padx=10, pady=10, fill='x', expand=True)

# komponen - komponen
# 1. label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan")
nama_depan_label.pack(padx=10, pady=10, fill='x', expand=True)

# 2. Entry nama depan
NAMA_DEPAN = tk.StringVar()
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, pady=10, fill='x', expand=True)

window.mainloop()