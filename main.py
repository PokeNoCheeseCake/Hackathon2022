import pygame, sys
from car import Car
from car import Vector
from MenuButton import Button

pygame.init()

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
font1 = pygame.font.Font('freesansbold.ttf', 64)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Rush Hour')
img_path = 'images/'
car = Car(pygame.image.load(img_path + "red_car.png"), Vector(0.0, 0.0), 0.0)
car.accelerate(Vector(1, 1))

screen = pygame.display.set_mode((800, 600))

BG = pygame.image.load(img_path + "car.png")


def play():
    running = True
    while running:

        screen.fill((0, 0, 0))
        screen.blit(car.img, (car.position.get_x(), car.position.get_y()))
        car.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draws the surface object to the screen.
        pygame.display.update()
        clock.tick(40)


def options():
    pass


def about():
    pass


def displayMenu():
    while True:
        screen.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = font1.render('Welcome!', True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        PLAY_BUTTON = Button(image=pygame.image.load(img_path + "Play Rect.png"), pos=(400, 200),
                             text_input="PLAY", font=font, base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load(img_path + "Play Rect.png"), pos=(400, 350),
                                text_input="or yarok", font=font, base_color="#d7fcd4", hovering_color="White")
        ABOUT_BUTTON = Button(image=pygame.image.load(img_path + "Play Rect.png"), pos=(400, 500),
                              text_input="ABOUT", font=font, base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, ABOUT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if ABOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    about()

        pygame.display.update()


displayMenu()
