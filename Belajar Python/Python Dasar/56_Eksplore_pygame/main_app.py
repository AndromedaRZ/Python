# mengeksplorasi package pygame pada python

import pygame
# membuat game sederhana menggunakan pygame

# init --> untuk menginisialisasi enginen game pythonya
pygame.init()

# variabel running game --> untuk menjaga aplikasi tetap berjalan menggunakan dummy variabel ini
isRun = True

# membuat display surface object --> untuk menaruh setiap asset gamenya atau background gamenya
window_panjang = 500
window_lebar = 500
window = pygame.display.set_mode((window_lebar, window_panjang))

# object game
# posisi
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 5

while isRun:
    pygame.time.delay(10)
    # user input, database input
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    
    # mengambil semua keyboard press
    keys = pygame.key.get_pressed()
    
    # ambil keyboard arrow kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    
    # ambil keyboard arrow kanan
    if keys[pygame.K_RIGHT] and x < window_lebar - lebar:
        x += speed 
    
    # ambil keyboard arrow atas
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    
    # ambil keyboard arrow bawah
    if keys[pygame.K_DOWN] and y < window_panjang - panjang:
        y += speed
    
    # update asset
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 120, 0), (x, y, lebar, panjang))
    # render dispay
    pygame.display.update()
    
    
pygame.quit()
            

    


