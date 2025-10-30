# pygame digunakan untuk membuat game pada bahasa pemrograman Python

# sebelum itu kita akan menginstall package pygame menggunakan pip
# pip install pygame

# ada beberapa hal yang perlu diperhatikan ketika ingin membuat game
# 1. init -> atau inisialisasi dan strukturnya
# 2. user input, database input -> mengambil data dari user dan menyimpannya ke database
# 3. update asset
# 4. render ke display -> render ini melakukan pekerjaan yang paling berat dari semua step-nya

import pygame

# 1. init
pygame.init() # menjalankan game engine

# variabel running game
isRun = True

# membuat display surface object (membuat windownya)
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang)) # lebar dan panjang tab diatur menjadi 500

# object game
# posisi (koordinat)
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 10

# loop di bawah berfungsi agar program tidak langsung menutup sendiri
while isRun:
    pygame.time.delay(20)
    # 2. user Input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    
    # ambil semua keyboard press
    keys = pygame.key.get_pressed()
    
    # ambil ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
        
    if keys[pygame.K_RIGHT] and x < window_lebar - lebar:
        x += speed
           
    if keys[pygame.K_DOWN] and y < window_panjang - panjang:
        y += speed
    
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    # pada titik ini, pygame sudah bisa berjalan
    
    # game dynamic
    # 3. update asset
    window.fill((255,255,255)) # (r,g,b)
    pygame.draw.rect(window, (255,120,0),(x,y,lebar,panjang))
    
    # 4. render ke display
    pygame.display.update()


pygame.QUIT()