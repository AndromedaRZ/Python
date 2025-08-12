# Konversi satuan temperatur

# Program konversi dari celcus ke satuan lain

print("\nPRORGAM KONVERSI TEMPERATUR\n")

# CELCIUS KE SATUAN LAIN
print("KONVERSI CELCIUS KE SATUAN LAIN")
celcius = float(input("Masukkan suhu dalam celcius: "))
print(f"Suhu dalam celcius: {celcius} C")

# celcius ke reamur = 4/5 * C
reamur = (4/5) * celcius
print(f"Suhu dalam reamur: {reamur} R")

# celcius ke fahrenheit = (9/5 * C) + 32
fahrenheit = (9/5) * celcius + 32
print(f"Suhu dalam fahrenheit: {fahrenheit} F")

# celcius ke kelvin = C + 273
kelvin = celcius + 273
print(f"Suhu dalam kelvin: {kelvin} K")

# REAMUR KE SATUAN LAIN
print("\nKONVERSI REAMUR KE SATUAN LAIN")

reamur = float(input("Masukkan suhu dalam reamur: "))
print(f"Suhu dalam celcius: {reamur} C")

# reamur ke celcius = 5/4 * R
celcius = (5/4) * reamur
print(f"Suhu dalam celcius: {celcius} C")

# reamur ke fahrenheit = (9/4 * R) + 32
fahrenheit = (9/4) * reamur + 32
print(f"Suhu dalam fahrenheit: {fahrenheit} F")

# reamur ke kelvin = (5/4 * R) + 273
kelvin = (5/4) * reamur + 273
print(f"Suhu dalam kelvin: {kelvin} K")

# FAHRENHEIT KE SATUAN LAIN
print("\nKONVERSI FAHRENHEIT KE SATUAN LAIN")
fahrenheit = float(input("Masukkan suhu dalam fahrenheit: "))
print(f"Suhu dalam fahrenheit: {fahrenheit} F")

# fahrenheit ke celcius = (5/9 * (F - 32))
celcius = (5/9) * (fahrenheit - 32)
print(f"Suhu dalam celcius: {celcius} C")

# fahrenheit ke reamur = (4/9 * (F - 32))
reamur = (4/9) * (fahrenheit - 32)
print(f"Suhu dalam reamur: {reamur} R")

# fahrenheit ke kelvin = (5/9 * (F - 32)) + 273
kelvin = (5/9) * (fahrenheit - 32) + 273
print(f"Suhu dalam kelvin: {kelvin} K")

# KELVIN KE SATUAN LAIN
print("\nKONVERSI KELVIN KE SATUAN LAIN")
kelvin = float(input("Masukkan suhu dalam kelvin: "))
print(f"Suhu dalam kelvin: {kelvin} K")

# kelvin ke celcius = K - 273
celcius = kelvin - 273
print(f"Suhu dalam celcius: {celcius} C")

# kelvin ke reamur = (4/5 * (K - 273))
reamur = (4/5) * (kelvin - 273)
print(f"Suhu dalam reamur: {reamur} R")

# kelvin ke fahrenheit = (9/5 * (K - 273)) + 32
fahrenheit = (9/5) * (kelvin - 273) + 32
print(f"Suhu dalam fahrenheit: {fahrenheit} F")

# Akhir program konversi temperatur
print("\nProgram konversi temperatur selesai.")
# Program selesai
print("Terima kasih telah menggunakan program ini.")