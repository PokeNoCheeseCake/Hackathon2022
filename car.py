import math

from utils import scale_image, blit_rotate_center


class Car(object):
    def __init__(self, img, position, angle, rotation_val):
        self.img = img
        self.speed = Vector(0.0, 0.0)
        self.position = Vector(position.get_x(), position.get_y())
        self.angle = angle
        self.rotation_val = rotation_val

    def accelerate(self, vector):
        self.speed.set_x(self.speed.get_x() + vector.get_x())
        self.speed.set_y(self.speed.get_y() + vector.get_y())

    def move(self):
        self.position.set_x(self.position.get_x() + self.speed.get_x())
        self.position.set_y(self.position.get_y() + self.speed.get_y())

    def rotate(self, left=False, right=False):
        if self.angle != self.speed.get_angle():
            if (abs(self.speed.get_angle() - self.angle) < self.rotation_val):
                self.angle = self.speed.get_angle()
            elif self.angle < self.speed.get_angle():
                self.angle += self.rotation_val
            elif self.angle > self.speed.get_angle():
                self.angle -= self.rotation_val
            self.angle = self.angle % 360.0
            print(self.angle)

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

    def get_angle(self):
        return 180 - int(math.degrees(math.atan(self.y/self.x)))
