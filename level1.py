# # import pygame module in this program
import sys

import pygame
from car import Car
from vector import Vector
from constants import Constants
from number import Number


def play_level():
    clock = pygame.time.Clock()

    # assigning values to X and Y variable
    X = Constants.GAME_WIDTH.value
    Y = Constants.GAME_HEIGHT.value

    screen = pygame.display.set_mode((Constants.GAME_WIDTH.value, Constants.GAME_HEIGHT.value))

    # create the display surface object
    # of specific dimension..e(X, Y).
    display_surface = pygame.display.set_mode((X, Y))

    # set the pygame window name
    pygame.display.set_caption('Image')

    number1 = Number(1)
    number2 = Number(2)
    number3 = Number(3)
    number_group = pygame.sprite.Group()

    number_group.add(number1, number2, number3)

    car_array = []

    car = Car(pygame.image.load(Constants.RED_CAR_IMG.value), Vector(635, 632), 0.0, 1.5)
    car.speed = 10
    wanted_angle = (car.angle + 90) % 360

    car2 = Car(pygame.image.load(Constants.BLUE_CAR_IMG.value), Vector(860, 250), 90.0, 1.5)
    car2.speed = 10
    wanted_angle2 = car2.angle

    car3 = Car(pygame.image.load(Constants.GREEN_CAR_IMG.value), Vector(360, 70), 180.0, 1.5)
    car3.speed = 10
    wanted_angle3 = (car.angle - 90) % 360

    car_array.append({
        'car': car2,
        'wanted_angle': wanted_angle2
    })

    car_array.append({
        'car': car3,
        'wanted_angle': wanted_angle3
    })

    car_array.append({
        'car': car,
        'wanted_angle': wanted_angle
    })

    current_car = 0

    # infinite loop
    while True:
        car_index = current_car

        # create a surface object, image is drawn on it.
        image = pygame.image.load('images/4-side-road.jpg')

        image = pygame.transform.scale(image, (X, Y))

        screen.blit(image, image.get_rect())
        back_img = pygame.image.load(Constants.BUTTON_BACK.value)
        back_img = pygame.transform.scale(back_img, (50, 50))
        screen.blit(back_img, (Constants.GAME_WIDTH.value - 60, 0))
        info_img = pygame.image.load(Constants.BUTTON_INFO.value)
        screen.blit(info_img, (0, Constants.GAME_HEIGHT.value - 50))
        number_group.draw(display_surface)

        while car_index < len(car_array):
            obj = car_array[car_index]

            if car_index == current_car:
                update_car(screen, obj['car'], obj['wanted_angle'], True)
                if obj['car'].position.get_x() > X or obj['car'].position.get_x() < 0 or obj[
                    'car'].position.get_y() > Y or obj['car'].position.get_y() < 0:
                    current_car = current_car + 1
            else:
                update_car(screen, obj['car'], obj['wanted_angle'], False)

            car_index = car_index + 1

        for event in pygame.event.get():

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # back button: top = 0, bot = 45, left = 968, right = 1011
                if 0 <= mouse_y <= 45 and 968 <= mouse_x <= 1011:
                    # return to main menu
                    return

                # info button: right = 48, left = 0, # up = 720, down = 768
                if 0 <= mouse_x <= 48 and 768 >= mouse_y >= 720:
                    # display laws
                    bg2 = pygame.image.load(Constants.LAW.value)
                    bg2 = pygame.transform.scale(bg2, (Constants.GAME_WIDTH.value, Constants.GAME_HEIGHT.value))
                    running = True
                    while running:
                        screen.blit(bg2, (0, 0))

                        for law_event in pygame.event.get():
                            if law_event.type == pygame.QUIT:
                                running = False

                        pygame.display.update()

        # Draws the surface object to the screen.
        pygame.display.update()
        pygame.display.flip()
        clock.tick(40)


def update_car(screen, car, wanted_angle, move=False):
    if move:
        if car.angle != wanted_angle:
            car.rotate(wanted_angle)

        car.move()

    car.draw(screen)
