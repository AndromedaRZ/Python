# Latihan percabangan if elif else dengan membuat kalkulator sederhana

title = "KALKULATOR SEDERHANA"
sub_title = (len(title) + 8) * '*'

print(sub_title)
print(3*"*",title,3*"*")
print(sub_title)

angka_1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, x, /): ")
angka_2 = float(input("Masukkan angka kedua: "))

if operator == "+":
    hasil = angka_1 + angka_2
elif operator == "-":
    hasil = angka_1 - angka_2
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
elif operator == "/":
    if angka_2 != 0:
        hasil = angka_1 / angka_2
    else:
        hasil = "Error: Pembagi tidak boleh nol."
else:
    hasil = "Operator tidak dikenali."

print(f"Hasil: {hasil}")