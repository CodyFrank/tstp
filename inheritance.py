class Shape:
    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):
    pass

class Square(Shape):
    pass


shape = Shape()
rect = Rectangle()
sq = Square()

shape.what_am_i()
rect.what_am_i()
sq.what_am_i()