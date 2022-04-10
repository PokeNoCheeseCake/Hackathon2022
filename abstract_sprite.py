from vector import Vector


class AbstractSprite(object):
    def __init__(self, image, position):
        self.image = image
        self.position = Vector(position.get_x(), position.get_y())

    def set_position(self, position):
        self.position.set_x(position.get_x())
        self.position.set_y(position.get_y())

    def get_position(self):
        return self.position

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image
