from vector import Vector


class AbstractSprite(object):
    def __init__(self, image, x, y):
        self.image = image
        self.position = Vector(x, y)

    def set_position(self, x, y):
        self.position.set_x(x)
        self.position.set_y(y)

    def get_position(self):
        return self.position

    def get_image(self):
        return self.image

    def set_image(self, image):
        self.image = image
