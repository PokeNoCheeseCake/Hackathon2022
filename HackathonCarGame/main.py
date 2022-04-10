import pygame, sys
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

# create a text surface object,
# on which text is drawn on it.
#text = font.render('You make me proud son', True, green, blue)

# create a rectangular object for the
# text surface object
#textRect = text.get_rect()

# set the center of the rectangular object.
#textRect.center = (X // 2, Y // 2)

screen = pygame.display.set_mode((800, 600))

# running = True

BG = pygame.image.load("C:\MyPrograming\hakaton\gradient.png")

def play():
    pass

def options():
    pass

def displayMenu():
    pygame.display.set_caption("Menu")
    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = font.render('Welcome!', True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("C:\MyPrograming\hakaton\Play Rect.png"), pos=(400, 200),
                             text_input="PLAY", font=font, base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("C:\MyPrograming\hakaton\Play Rect.png"), pos=(400, 350),
                                text_input="or yarok", font=font, base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("C:\MyPrograming\hakaton\Play Rect.png"), pos=(400, 500),
                             text_input="about", font=font, base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
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
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


displayMenu()
