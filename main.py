import pygame, sys

import utils
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
    back_img = pygame.image.load(Constants.BUTTON_BACK.value)
    back_img = pygame.transform.scale(back_img, (50, 50))

    while True:
        screen.blit(BG2, (0, 0))
        screen.blit(back_img, (Constants.GAME_WIDTH.value - 60, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # back button: top = 0, bot = 45, left = 968, right = 1011
                if 0 <= mouse_y <= 45 and 968 <= mouse_x <= 1011:
                    # return to menu
                    return

        pygame.display.update()


def about():
    BG2 = pygame.image.load(Constants.ABOUT.value)
    BG2 = pygame.transform.scale(BG2, (Constants.GAME_WIDTH.value, Constants.GAME_HEIGHT.value))

    while True:
        screen.blit(BG2, (0, 0))
        back_img = pygame.image.load(Constants.BUTTON_BACK.value)
        back_img = pygame.transform.scale(back_img, (50, 50))
        screen.blit(back_img, (Constants.GAME_WIDTH.value - 60, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # top = 0, bot = 45, left = 968, right = 1011
                if 0 <= mouse_y <= 45 and 968 <= mouse_x <= 1011:
                    # return to menu
                    return

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
                             text_input="TRAFFIC LAWS", font=font, base_color="#d7fcd4", hovering_color="White")
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
                    success = level1.play_level()

                    if success:
                        # play level 2!
                        success_image = pygame.image.load(Constants.LEVEL_1_SUCCESS.value)
                        screen.blit(success_image, (Constants.GAME_WIDTH.value / 4,
                                                    Constants.GAME_HEIGHT.value / 4))
                        pygame.display.update()
                if LAWS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    laws()
                if ABOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    about()

        pygame.display.update()


display_menu()
