import math
from utils import scale_image, blit_rotate_center
from abstract_sprite import AbstractSprite


class Car(AbstractSprite):
    def __init__(self, image, position, angle, rotation_val, arrow):
        super(Car, self).__init__(image, position)
        self.speed = 0
        self.angle = angle
        self.rotation_val = rotation_val
        self.arrow = arrow

    def move(self):
        self.position.set_x(self.position.get_x() - self.speed * math.cos(math.radians(self.angle - 90)))
        self.position.set_y(self.position.get_y() + self.speed * math.sin(math.radians(self.angle - 90)))

    def rotate(self, wanted_angle):
        if self.angle != wanted_angle:
            if (abs(wanted_angle - self.angle) < self.rotation_val):
                self.angle = wanted_angle
            elif ((wanted_angle - self.angle) % 360) <= ((self.angle - wanted_angle) % 360):
                self.angle += self.rotation_val
            elif ((wanted_angle - self.angle) % 360) > ((self.angle - wanted_angle) % 360):
                self.angle -= self.rotation_val
            self.angle = self.angle % 360.0

    def draw(self, win, draw_arrow=False):
        blit_rotate_center(win, self.image, (self.position.get_x(), self.position.get_y()), self.angle)

        if draw_arrow:
            blit_rotate_center(win, self.arrow, (self.position.get_x() + 100*math.cos(math.radians(self.angle + 90)), self.position.get_y() + 100*math.sin(math.radians(self.angle - 90))), self.angle)
