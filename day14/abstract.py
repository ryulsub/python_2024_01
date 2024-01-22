# abstract
# 추상 클래스
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def get_round(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, r):
#         self.radius = r
#
#     def get_area(self):
#         return 3.14 * self.radius ** 2
#     def get_around(self):
#         return 3.14 * self.radius * 2

class Trianle(Shape):
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def get_area(self):
        return self.base * self.height * 0.5
    def get_round(self):
        return self.base * 4

a = Triangle(5,5)
print(b.get_area())
print(h.get_around())


