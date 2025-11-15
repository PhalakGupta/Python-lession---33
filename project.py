import pygame

#Initilize Pygame and screen dimensions
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
clock = pygame.time.Clock()
#Initilize display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('My First Game Screen')
GREY = (58, 58, 58)
bg = pygame.image.load("pexels-goumbik-669502.jpg")
SIZE = (300, 300)
image = pygame.transform.scale(bg, SIZE)
while True:
    display_surface.fill(GREY)
    display_surface.blit(image, (100, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()
    clock.tick(30)