import pygame

pygame.init()

pygame.display.set_caption('Lomda')
clock = pygame.time.Clock()

# define the RGB value for white
lightBlue = (137, 219, 236)

# should be relative
bg = pygame.image.load("C:/Users/jacob vider/Desktop/bg.png")

# size of screen
X = 800
Y = 600

# create the display surface object of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# create a font object.
font = pygame.font.Font('freesansbold.ttf', 64)

# זכותי, סימני דרך, road-it
lomdaNameText = font.render('Road Safety lomda', True,  lightBlue)
# The current alpha value of the surface.
alpha = 255
# To get a 20 frame delay.
timer = 20

# create a rectangular object for the text surface object
textRect = lomdaNameText.get_rect()

screen = pygame.display.set_mode((800, 600))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if timer > 0:
        timer -= 1
    else:
        if alpha > 0:
            # Reduce alpha each frame, but make sure it doesn't get below 0.
            alpha = max(0, alpha-4)
            # Create a copy so that the original surface doesn't get modified.
            lomdaNameText.fill((25, 25, 25, alpha),
                               special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(bg, (0, 0))
        screen.blit(lomdaNameText, (X//7, Y//2.5))
        clock.tick(40)
        pygame.time.wait(60)

        pygame.display.flip()
    # Draws the surface object to the screen.
    pygame.display.update()
