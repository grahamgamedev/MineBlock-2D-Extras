import pygame
pygame.init()
size = (100, 100)
screen = pygame.display.set_mode(size)
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            
pygame.quit()
