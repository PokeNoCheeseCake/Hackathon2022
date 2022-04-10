# # import pygame module in this program
import pygame
import PIL
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.

pygame.init()

# define the RGB value
# for white colour
white = (255, 255, 255)
  
# assigning values to X and Y variable
X = 370
Y = 370
  
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))
  
# set the pygame window name
pygame.display.set_caption('Image')
  
# create a surface object, image is drawn on it.
image = pygame.image.load('images/4-side-road.jpg')

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

number1 = Number(1)
number2 = Number(2)
number3 = Number(3)
number_group = pygame.sprite.Group()
number_group.add(number1, number2, number3)

# infinite loop
while True :
    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    # ^^^^^^ display_surface.blit(image, (0, 0))
  
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get() :
  
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT :
  
            # deactivates the pygame library
            pygame.quit()
  
            # quit the program.
            quit()
  
        # Draws the surface object to the screen.  
        pygame.display.update()
        pygame.display.flip()
        display_surface.blit(image, (0, 0))
        number_group.draw(display_surface)

# import pygame, sys
# from pygame.locals import *
# import random
 
# pygame.init()
 
# FPS = 60
# FramePerSec = pygame.time.Clock()
 
# BLUE  = (0, 0, 255)
# RED   = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
 
# # Screen information
# SCREEN_WIDTH = 400
# SCREEN_HEIGHT = 600
 
# DISPLAYSURF = pygame.display.set_mode((400,600))
# DISPLAYSURF.fill(BLACK)
# pygame.display.set_caption("Game")
 
# class Enemy(pygame.sprite.Sprite):
#       def __init__(self):
#         super().__init__() 
#         self.image = pygame.image.load("Enemy.png")
#         self.rect = self.image.get_rect()
#         self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
 
#       def move(self):
#         self.rect.move_ip(0,10)
#         if (self.rect.bottom > 600):
#             self.rect.top = 0
#             self.rect.center = (random.randint(30, 370), 0)
 
#       def draw(self, surface):
#         surface.blit(self.image, self.rect) 
 
 
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__() 
#         self.image = pygame.image.load("Player.png")
#         self.rect = self.image.get_rect()
#         self.rect.center = (160, 520)
 
#     def update(self):
#         pressed_keys = pygame.key.get_pressed()
#        #if pressed_keys[K_UP]:
#             #self.rect.move_ip(0, -5)
#        #if pressed_keys[K_DOWN]:
#             #self.rect.move_ip(0,5)
         
#         if self.rect.left > 0: 
#               if pressed_keys[K_LEFT]:
#                   self.rect.move_ip(-5, 0)
#         if self.rect.right < SCREEN_WIDTH:        
#               if pressed_keys[K_RIGHT]:
#                   self.rect.move_ip(5, 0)
 
#     def draw(self, surface):
#         surface.blit(self.image, self.rect)     
 
         
# P1 = Player()
# E1 = Enemy()
 
# while True:     
#     for event in pygame.event.get():              
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     P1.update()
#     E1.move()
     
#     DISPLAYSURF.fill(BLACK)
#     P1.draw(DISPLAYSURF)
#     E1.draw(DISPLAYSURF)
         
#     pygame.display.update()
#     FramePerSec.tick(FPS)






















# pygame.init()
# screen = pygame.display.set_mode((128, 128))
# clock = pygame.time.Clock()

# counter, text = 0, '0'.rjust(3)
# pygame.time.set_timer(pygame.USEREVENT, 1000)
# font = pygame.font.SysFont('Consolas', 30)

# run = True
# while run:
#     for e in pygame.event.get():
#         if e.type == pygame.USEREVENT: 
#             counter += 1
#             text = str(counter).rjust(3) if counter > 0 else 'boom!'
#         if e.type == pygame.QUIT: 
#             run = False

#     screen.fill((255, 255, 255))
#     screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
#     pygame.display.flip()
#     clock.tick(60)

# screen = pygame.display.set_mode((640, 480))
# player = pygame.image.load(r'car 1.png').convert()
# background = pygame.image.load(r'4-side-road.jpg').convert()
# screen.blit(background, (0, 0))
# objects = []
# for x in range(10):                    #create 10 objects</i>
#     o = GameObject(player, x*40, x)
#     objects.append(o)
# while 1:
#     for event in pygame.event.get():
#         if event.type in (pygame.QUIT, pygame.KEYDOWN):
#             sys.exit()
#     for o in objects:
#         screen.blit(background, o.pos, o.pos)
#     for o in objects:
#         o.move()
#         screen.blit(o.image, o.pos)
#     pygame.display.update()
#     pygame.time.delay(100)

    