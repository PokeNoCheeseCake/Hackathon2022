# # import pygame module in this program
import sys
from time import sleep

import pygame
from car import Car
from vector import Vector
from constants import Constants
from number import Number
from utils import blit_rotate_center


def play_level():
    clock = pygame.time.Clock()

    # assigning values to X and Y variable
    X = Constants.GAME_WIDTH.value
    Y = Constants.GAME_HEIGHT.value

    screen = pygame.display.set_mode((Constants.GAME_WIDTH.value, Constants.GAME_HEIGHT.value))

    # create the display surface object
    # of specific dimension..e(X, Y).
    display_surface = pygame.display.set_mode((X, Y))

    success = True

    number1 = Number(1)
    number2 = Number(2)
    number3 = Number(3)
    number_group = pygame.sprite.Group()

    number_group.add(number1, number2, number3)

    car_array = []

    curve_arrow = pygame.image.load(Constants.CURVE_ARROW_IMG.value)
    curve_arrow = pygame.transform.scale(curve_arrow, (50, 50))

    straight_arrow = pygame.image.load(Constants.STRAIGHT_ARROW_IMG.value)
    straight_arrow = pygame.transform.scale(straight_arrow, (50, 70))

    car = Car(pygame.image.load(Constants.RED_CAR_IMG.value), Vector(635, 632), 0.0, 1.5, curve_arrow)
    car.speed = 10
    wanted_angle = (car.angle + 90) % 360

    car2 = Car(pygame.image.load(Constants.BLUE_CAR_IMG.value), Vector(860, 250), 90.0, 1.5, straight_arrow)
    car2.speed = 10
    wanted_angle2 = car2.angle

    car3 = Car(pygame.image.load(Constants.GREEN_CAR_IMG.value), Vector(360, 70), 180.0, 1.5, curve_arrow)
    car3.speed = 10
    wanted_angle3 = (car.angle - 90) % 360

    car_array.append({
        'car': car3,
        'wanted_angle': wanted_angle3,
        'num': 0,
        'bad': False
    })

    car_array.append({
        'car': car2,
        'wanted_angle': wanted_angle2,
        'num': 0,
        'bad': False
    })

    car_array.append({
        'car': car,
        'wanted_angle': wanted_angle,
        'num': 0,
        'bad': False
    })

    stop_sign = pygame.image.load(Constants.STOP_SIGN_IMG.value)

    current_car = 0
    count_placed_numbers = 0

    # create a surface object, image is drawn on it.
    image = pygame.image.load('images/4-side-road.jpg')
    image = pygame.transform.scale(image, (X, Y))
    screen.blit(image, image.get_rect())

    number_group.draw(display_surface)

    dragged = pygame.sprite.Group()

    dragged_num = None
    back_img = pygame.image.load(Constants.BUTTON_BACK.value)
    back_img = pygame.transform.scale(back_img, (50, 50))
    info_img = pygame.image.load(Constants.BUTTON_INFO.value)

    while count_placed_numbers < 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # deactivate the pygame library and exit
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for x in number_group:
                    if x.rect.collidepoint(event.pos):
                        is_placed = False
                        for obj in car_array:
                            if obj['num'] == x.num:
                                is_placed = True
                        if not is_placed:
                            dragged.add(x)
                            dragged_num = x

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
            elif event.type == pygame.MOUSEBUTTONUP:
                dragged.empty()
                if dragged_num is not None:
                    for obj in car_array:
                        if near_car(obj['car'], dragged_num.rect.x, dragged_num.rect.y):
                            if obj['num'] == 0:
                                obj['num'] = dragged_num.num
                                count_placed_numbers += 1

            elif event.type == pygame.MOUSEMOTION:
                dragged.update(event.rel)

        # remove this for solitaire
        screen.blit(image, image.get_rect())

        car_index = 0
        while car_index < len(car_array):
            screen.blit(back_img, (Constants.GAME_WIDTH.value - 60, 0))
            screen.blit(info_img, (0, Constants.GAME_HEIGHT.value - 50))
            obj = car_array[car_index]
            update_car(screen, obj['car'], obj['wanted_angle'], False)
            car_index = car_index + 1

        blit_rotate_center(screen, stop_sign, (700, 600), 0)
        number_group.draw(screen)
        pygame.display.update()
        pygame.display.flip()

        clock.tick(40)

    # infinite loop - RUNS CARS
    while current_car < 3:
        car_index = current_car

        # create a surface object, image is drawn on it.
        image = pygame.image.load('images/4-side-road.jpg')
        image = pygame.transform.scale(image, (X, Y))
        screen.blit(image, image.get_rect())

        screen.blit(back_img, (Constants.GAME_WIDTH.value - 60, 0))
        screen.blit(info_img, (0, Constants.GAME_HEIGHT.value - 50))
        blit_rotate_center(screen, stop_sign, (700, 600), 0)

        while car_index < len(car_array):
            obj = car_array[car_index]
            bad_car = None

            if car_index == current_car:
                update_car(screen, obj['car'], obj['wanted_angle'], True)

                weird_num = obj['num'] - 1
                if weird_num != current_car:
                    success = False

                    for obj2 in car_array:
                        if current_car + 1 == obj2['num']:
                            bad_car = obj2
                            bad_car['bad'] = True

                    update_car(screen, bad_car['car'], bad_car['wanted_angle'], True)

                    if near_car(obj['car'], bad_car['car'].position.get_x(), bad_car['car'].position.get_y()):
                        crash(obj['car'])
                        crash(bad_car['car'])
                        current_car = 3

                if obj['car'].position.get_x() > X or obj['car'].position.get_x() < 0 or obj[
                    'car'].position.get_y() > Y or obj['car'].position.get_y() < 0:
                    current_car = current_car + 1
            else:
                if obj['bad'] == False:
                    update_car(screen, obj['car'], obj['wanted_angle'], False)

            car_index = car_index + 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        # Draws the surface object to the screen.
        pygame.display.update()
        pygame.display.flip()
        clock.tick(40)

    if not success:
        while True:
            failure_image = pygame.image.load(Constants.LEVEL_1_FAIL.value)
            screen.blit(failure_image, (Constants.GAME_WIDTH.value / 4,
                                        Constants.GAME_HEIGHT.value / 4))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # menu button: top = 410, bot = 462, left = 524, right = 734
                    if 410 <= mouse_y <= 462 and 524 <= mouse_x <= 734:
                        # return to main menu
                        return
                    elif 410 <= mouse_y <= 462 and 306 <= mouse_x <= 507:
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

            pygame.display.update()
            pygame.display.flip()
            clock.tick(40)

    else:
        return success


def update_car(screen, car, wanted_angle, move=False):
    if move:
        if car.angle != wanted_angle:
            car.rotate(wanted_angle)

        car.move()
    car.draw(screen, not move)


def near_car(car, x, y):
    return car.position.x - 50 < x < car.position.x + 50 and car.position.y - 50 < y < car.position.y + 50


def crash(car):
    car.speed = 0
    car.rotation_val = 0
