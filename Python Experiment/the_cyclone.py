# Program ini berisi sistem gerbang otomatis pada sebuah gerbang masuk yang ada sebelum kita bisa menaiki roller coaster, program ini membantu petugas roller coaster untuk memastikan apakah seseorang yang ingin naik roller coaster tersebut memenuhi syarat atau tidak.

print("roller coaster entrance")
print('''Min requirements
Height: 137 cm
kredit: 10''')
height = float(input("How tall are you? "))
kredit = int(input("How much credit do you have? "))

if height >= 137 and kredit >= 10:
  print("Enjoy the ride!")
elif height < 137 and kredit >= 10:
  print("You are not tall enough to ride")
elif height >= 137 and kredit < 10:
  print("You don't have enough credits")
else:
  print("You have not met requirement to ride")