import math 

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setX(self, newX):
        self.x = newX

    def setY(self, newY):
        self.y = newY

    def add(self, v):
        # Adds a Vector2D to this vector.
        self.x = self.x + v.x
        self.y = self.y + v.y

    def sub(self, v):
        # Subtracts a Vector2D from this vector.
        self.x = self.x - v.x
        self.y = self.y - v.y

    def mult(self, factor):
        # Multiplies this vector by a given factor.
        self.x = self.x * factor
        self.y = self.y * factor

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def setLength(self, newLength):
        factor = newLength / self.length()
        self.mult(factor)

    def copy(self):
        return Vector2D.Copy(self)
    
    def rotate(self, angle):
        cos = math.cos(math.radians(angle))
        sin = math.sin(math.radians(angle))
        newX = self.x * cos - self.y * sin
        newY = self.x * sin + self.y * cos
        self.x = newX
        self.y = newY

    def normalize(self):
        length = self.length()
        self.x = self.x / length
        self.y = self.y / length

    @staticmethod
    def Add(vector1, vector2):
        return Vector2D(vector1.x + vector2.x, vector1.y + vector2.y)

    @staticmethod
    def Sub(vector1, vector2):
        return Vector2D(vector1.x - vector2.x, vector1.y - vector2.y)

    @staticmethod
    def Mult(vector, factor):
        return vector.copy().mult(factor)

    @staticmethod
    def Dist(point1, point2):
        return Vector2D.Sub(point2, point1).length()

    @staticmethod
    def Copy(vector):
        return Vector2D(vector.x, vector.y)

    @staticmethod
    def Rotate(vector, angle):
        return vector.copy().rotate(angle)

    @staticmethod
    def Normalized(vector):
        return vector.copy().normalize()