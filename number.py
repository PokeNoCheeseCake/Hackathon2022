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
            self.rect[0] = 27
            self.rect[1] = 40
        if num == 3:
            self.rect[0] = 52
            self.rect[1] = 3
        print(self.rect)

    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)