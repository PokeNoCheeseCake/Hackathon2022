class Car(object):
    def __init__(self, img, position, angle):
        self.img = img
        self.speed = Vector(0.0, 0.0)
        self.position = Vector(position.get_x(), position.get_y())
        self.angle = angle

    def accelerate(self, vector):
        self.speed.set_x(self.speed.get_x() + vector.get_x())
        self.speed.set_y(self.speed.get_y() + vector.get_y())

    def move(self):
        self.position.set_x(self.position.get_x() + self.speed.get_x())
        self.position.set_y(self.position.get_y() + self.speed.get_y())


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
