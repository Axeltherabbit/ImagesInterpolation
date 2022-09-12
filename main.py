import pygame


pygame.display.init()
startImg = pygame.image.load("images/self-portrait-without-beard.bmp")
startImg = startImg.convert(32) # converts the pixel depth to 32 to support surfarray.pixels2d

targetImg = pygame.image.load("images/spring-summer-van-gogh-museum.bmp")
targetImg = targetImg.convert(32)

start_pixels_array = pygame.surfarray.pixels2d(startImg)
target_pixels_array = pygame.surfarray.pixels2d(targetImg)

print(len(start_pixels_array[0]))


del start_pixels_array #unlock the surface


window = pygame.display.set_mode(startImg.get_size())
while True:
    window.blit(startImg, (0,0)) 
    pygame.display.update()

    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            break
    
    


