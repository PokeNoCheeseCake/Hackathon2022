import pygame
from car import Car
from car import Vector
from constants import Constants

pygame.init()
pygame.display.set_caption(Constants.PROJECT_NAME.value)
clock = pygame.time.Clock()
car = Car(pygame.image.load(Constants.RED_CAR_IMG.value), Vector(0.0, 0.0), 0.0)
car.accelerate(Vector(1, 1))
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(car.image, (car.position.get_x(), car.position.get_y()))
    car.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draws the surface object to the screen.
    pygame.display.update()
    clock.tick(40)
