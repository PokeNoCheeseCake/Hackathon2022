import pygame
from constants import Constants

# assigning values to X and Y variable
X = Constants.GAME_WIDTH.value
Y = Constants.GAME_HEIGHT.value

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

class Number(pygame.sprite.Sprite):

    def __init__(self, num):
        super().__init__()
        self.image = pygame.image.load("images/% sdigitcol.png" % num).convert_alpha(display_surface)
        self.rect = self.image.get_rect()
        if num == 1:
            self.rect[0] = 5
            self.rect[1] = 5
        if num == 2:
            self.rect[0] = 35
            self.rect[1] = 4
        if num == 3:
            self.rect[0] = 68
            self.rect[1] = 5

    def update(self, rel):
        self.rect.move_ip(rel)

    def draw(self, surface):
        surface.blit(self.image, self.rect) 