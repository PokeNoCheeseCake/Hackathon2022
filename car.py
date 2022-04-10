from abstract_sprite import AbstractSprite
from vector import Vector


class Car(AbstractSprite):
    def __init__(self, image, position, angle):
        super(Car, self).__init__(image, position.get_x(), position.get_y())
        self.speed = Vector(0.0, 0.0)
        self.angle = angle

    def accelerate(self, vector):
        self.speed.set_x(self.speed.get_x() + vector.get_x())
        self.speed.set_y(self.speed.get_y() + vector.get_y())

    def move(self):
        self.position.set_x(self.position.get_x() + self.speed.get_x())
        self.position.set_y(self.position.get_y() + self.speed.get_y())
