import pygame, sys
from MenuButton import Button
from constants import Constants
import level1

pygame.init()
pygame.display.set_caption(Constants.PROJECT_NAME.value)

screen = pygame.display.set_mode((Constants.GAME_WIDTH.value, Constants.GAME_HEIGHT.value))
font = pygame.font.Font(Constants.MENU_TEXT_FONT.value, 32)
font1 = pygame.font.Font(Constants.MENU_TEXT_FONT.value, 64)
BG = pygame.image.load(Constants.MENU_BACKGROUND.value)
BG = pygame.transform.scale(BG, (Constants.GAME_WIDTH.value, Constants.GAME_HEIGHT.value))


def laws():
    BG2 = pygame.image.load(Constants.LAW.value)
    BG2 = pygame.transform.scale(BG2, (Constants.GAME_WIDTH.value, Constants.GAME_HEIGHT.value))
    running = True
    while running:
        screen.blit(BG2, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


def about():
    BG2 = pygame.image.load(Constants.ABOUT.value)
    BG2 = pygame.transform.scale(BG2, (Constants.GAME_WIDTH.value, Constants.GAME_HEIGHT.value))
    running = True
    while running:
        screen.blit(BG2, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


def display_menu():
    while True:
        screen.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = font1.render('Welcome!', True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(Constants.GAME_WIDTH.value / 2, Constants.GAME_HEIGHT.value / 10))

        PLAY_BUTTON = Button(image=pygame.image.load(Constants.BUTTON_RECT.value),
                             pos=(Constants.GAME_WIDTH.value / 2, Constants.GAME_HEIGHT.value / 3.5),
                             text_input="PLAY", font=font, base_color="#d7fcd4", hovering_color="White")
        LAWS_BUTTON = Button(image=pygame.image.load(Constants.BUTTON_RECT.value),
                              pos=(Constants.GAME_WIDTH.value / 2, Constants.GAME_HEIGHT.value / 2.1),
                              text_input="or yarok", font=font, base_color="#d7fcd4", hovering_color="White")
        ABOUT_BUTTON = Button(image=pygame.image.load(Constants.BUTTON_RECT.value),
                              pos=(Constants.GAME_WIDTH.value / 2, Constants.GAME_HEIGHT.value / 1.5),
                              text_input="ABOUT", font=font, base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, LAWS_BUTTON, ABOUT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # play()
                    level1.play_level()
                if LAWS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    laws()
                if ABOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    about()

        pygame.display.update()


display_menu()
