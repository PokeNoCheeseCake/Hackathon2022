import pygame
import math

from car import Car
from car import Vector

pygame.init()

pygame.display.set_caption('Rush Hour')

clock = pygame.time.Clock()

img_path = 'images/red_car.png'
car = Car(pygame.image.load(img_path), Vector(400, 300), 0.0, 1)

wanted_angle = (car.angle - 90) % 360

screen = pygame.display.set_mode((800, 600))

car.speed = 5

running = True
while running:

    screen.fill((0, 0, 0))

    if car.angle != wanted_angle:
        car.move()
        car.rotate(wanted_angle)

    car.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draws the surface object to the screen.
    pygame.display.update()

    clock.tick(40)
