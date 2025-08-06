# Latihan perulangan membuat ketupat

sisi = 10
spasi = int(sisi/2)

count = 1
while True:
    if count % 2:
        print(" "*spasi, "+"*count)
        count += 1
        spasi -= 1
        
    else:
        count += 1
        continue

    if count == sisi:
        break
    

count += 2

while True:
    if count % 2:
        print(" "*spasi,"+"*count)
        count -= 1
        spasi += 1
    
    else:
        count -= 1
        continue
    
    if count == 0:
        break