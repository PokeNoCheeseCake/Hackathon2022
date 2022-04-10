# # import pygame module in this program
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
    });

    car_array.append({
        'car': car3,
        'wanted_angle': wanted_angle3
    });

    car_array.append({
        'car': car,
        'wanted_angle': wanted_angle
    });

    current_car = 0

    # infinite loop
    while True:
        car_index = current_car

        # create a surface object, image is drawn on it.
        image = pygame.image.load('images/4-side-road.jpg')

        image = pygame.transform.scale(image, (X, Y))

        screen.blit(image, image.get_rect())

        number_group.draw(display_surface)

        while car_index < len(car_array):
            obj = car_array[car_index];

            if (car_index == current_car):
                update_car(screen, obj['car'], obj['wanted_angle'], True)
                if obj['car'].position.get_x() > X or obj['car'].position.get_x() < 0 or obj['car'].position.get_y() > Y or obj['car'].position.get_y() < 0:
                    current_car = current_car + 1
            else:
                update_car(screen, obj['car'], obj['wanted_angle'], False)

            car_index = car_index + 1

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
        clock.tick(40)

def update_car(screen, car, wanted_angle, move=False):
    if move:
        if car.angle != wanted_angle:
            car.rotate(wanted_angle)

        car.move()

    car.draw(screen)

    # pygame.display.update()






















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

    