import pygame


pygame.display.init()
mapImg = pygame.image.load("images/self-portrait-without-beard.bmp")
mapImg = mapImg.convert(32) # converts the pixel depth to 32 to support surfarray.pixels2d

pixels_array = pygame.surfarray.pixels2d(mapImg)

print(pixels_array[0])


del pixels_array #unlock mapImg
window = pygame.display.set_mode(mapImg.get_size())
while True:
    window.blit(mapImg, (0,0)) 
    pygame.display.update()

    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            break
    
    


