import pygame;

pygame.init();

# hehe - itay also laughed
pygame.display.set_caption('אין מנוס');

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# assigning values to X and Y variable
X = 400
Y = 400

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)

# create a text surface object,
# on which text is drawn on it.
text = font.render('You make me proud son', True, green, blue)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (X // 2, Y // 2)


screen = pygame.display.set_mode((800, 600));

running = True;
while running:
    display_surface.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;

    # Draws the surface object to the screen.
    pygame.display.update()
