import math

from utils import scale_image, blit_rotate_center


class Car(object):
    def __init__(self, img, position, angle, rotation_val):
        self.img = img
        self.speed = 0
        self.position = Vector(position.get_x(), position.get_y())
        self.angle = angle
        self.rotation_val = rotation_val

    def move(self):
        self.position.set_x(self.position.get_x() - self.speed * math.cos(math.radians(self.angle)))
        self.position.set_y(self.position.get_y() + self.speed * math.sin(math.radians(self.angle)))

    def rotate(self, wanted_angle):
        if self.angle != wanted_angle:
            if (abs(wanted_angle - self.angle) < self.rotation_val):
                self.angle = wanted_angle
            elif ((wanted_angle - self.angle) % 360) <= ((self.angle - wanted_angle) % 360):
                self.angle += self.rotation_val
            elif ((wanted_angle - self.angle) % 360) > ((self.angle - wanted_angle) % 360):
                self.angle -= self.rotation_val
            self.angle = self.angle % 360.0

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.position.get_x(), self.position.get_y()), self.angle)


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # def get_angle(self):
    #     wanted_angle = 0
    #     if self.x == 0:
    #         if self.y >= 0:
    #             wanted_angle = 90
    #         else:
    #             wanted_angle = 270
    #     else:
    #         wanted_angle = int(math.degrees(math.atan(self.y / self.x)))
    #     return 180 - wanted_angle
