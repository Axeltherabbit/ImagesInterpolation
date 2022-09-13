import pygame
import numpy as np

def concat_bits_to_int(r,g,b,a):
    return (r << 24) + (g << 16) + (b << 8) + (a)

def map_int_to_rgb(array):
    row_arr = []
    for line in array:
        line_arr = []
        for px in line:
            line_arr.append(list(pygame.Color(int(px))))
        row_arr.append(line_arr)
    return row_arr

def map_rgb_to_int(array):
    row_arr = []
    for line in array:
        line_arr = []
        for rgba in line:
            line_arr.append(concat_bits_to_int(*rgba))
        row_arr.append(line_arr)
    return row_arr
    

def show_on_pygame(startImg, interpolations):
    window = pygame.display.set_mode(startImg.get_size())
    for i, bitmap in enumerate(map(map_rgb_to_int, interpolations)):
        print("frame :", i)
        pygame.surfarray.blit_array(startImg, np.array(bitmap, dtype = np.uint32)) 
        window.blit(startImg, (0,0))
        pygame.display.update()
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                break

def write_on_disk(startImg, interpolations):
    for i, bitmap in enumerate(map(map_rgb_to_int, interpolations)):
        print("frame :", i)
        pygame.surfarray.blit_array(startImg, np.array(bitmap, dtype = np.uint32)) 
        pygame.image.save(startImg,f"out/{i}.jpg")


if __name__ == "__main__":
    pygame.display.init()
    startImg = pygame.image.load("images/bill-gates.bmp")
    startImg = startImg.convert(32) # converts the pixel depth to 32 to support surfarray.pixels2d

    targetImg = pygame.image.load("images/richard-stallman.bmp")
    targetImg = targetImg.convert(32)

    start_pixels = pygame.surfarray.pixels2d(startImg)
    start_pixels = np.array(map_int_to_rgb(start_pixels), dtype = np.uint8)
    target_pixels = pygame.surfarray.pixels2d(targetImg)
    target_pixels = np.array(map_int_to_rgb(target_pixels), dtype = np.uint8)

    interpolations = np.linspace(start_pixels, target_pixels, 30, dtype = np.uint8)
    
    show_on_pygame(startImg, interpolations)
