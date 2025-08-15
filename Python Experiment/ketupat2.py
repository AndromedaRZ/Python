print("=====Program pembuat belah ketupat=====")
sisi = 10

count = 1
spasi = int(sisi / 2)

while True:
    if count % 2:
        print(" " * spasi, "+" * count)
        count += 1
        spasi -= 1

    else:
       count += 1
       continue
    
    if count > sisi:
        break

spasi += 1

while True:
    if count % 2:
        count -= 2
        spasi += 1
        print(" " * spasi, "+" * count)

    else:
       count -= 1
       continue
    
    if count < 0:
        break
 
