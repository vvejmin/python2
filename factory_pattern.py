# from abc import ABCMeta, abstractmethod
#
# class ShapeFactory(metaclass=ABCMeta):
#         def __init__(self):
#                 pass
#
#         @abstractmethod
#         def draw(self):
#                 pass
#
# class Circle(ShapeFactory):
#
#         def __init__(self):
#                 pass
#
#         def draw(self):
#                 print('the type of shape is circle')
#
# class Square(ShapeFactory):
#
#         def draw(self):
#                 print('the shape type is square')
#
# class Triangle(ShapeFactory):
#
#         def draw(self):
#                 print('the shape type is triangle')
#
# class Client:
#         @staticmethod
#         def create_shape(shape_type):
#                 if shape_type == 'Circle':
#                         return Circle()
#                 if shape_type == 'Square':
#                         return 'Square'
#                 if shape_type == 'Triangle':
#                         return 'Triangle'
#                 print('invalid type')
#                 return -1
#
# choice = input('What type do you want:')
# shape = Client.create_shape(choice)
# shape.draw()
#
# from abc import ABCMeta, abstractmethod
#
# class ShapeFactory(metaclass=ABCMeta):
#         @abstractmethod
#         def draw(self):
#                 pass
#
# class Circle(ShapeFactory):
#         def __init__(self):
#                 pass
#
#         def draw(self):
#             print('circle shape')
#
# class Square(ShapeFactory):
#
#         def __init__(self):
#             pass
#
#         def draw(self):
#                 print('square shape')
#
#
# class Triangle(ShapeFactory):
#         def __ini__(self):
#                 pass
#         def draw(self):
#                 print('triangle shape')
#
# class Client:
#         @staticmethod
#         def create_shape(shape_type):
#                 if shape_type == 'circle':
#                         return Circle()
#                 if shape_type == 'square':
#                         return Square()
#                 if shape_type == 'triangle':
#                         return Triangle()
#                 print('Invalid type')
#                 return -1
#
# choice = input('What type of shape do want to draw: ')
# shape = Client.create_shape(choice)
# shape.draw()

# from abc import ABCMeta, abstractmethod
#
# class ShapeFactory(metaclass=ABCMeta):
#         @abstractmethod
#         def draw(self):
#                 pass
#
# class Circle(ShapeFactory):
#         def draw(self):
#                 print('circle shape')
#
# class Square(ShapeFactory):
#         def draw(self):
#                 print('square shape')
#
# class Triangle(ShapeFactory):
#         def draw(self):
#                 print('triangle shape')
#
# class Client:
#         @staticmethod
#         def create_shape(shape_type):
#             if shape_type == 'Circle':
#                     return Circle()
#             if shape_type == 'Square':
#                     return Square()
#             if shape_type == 'Triangle':
#                     return Triangle()
#             print('invlaid input')
#             return -1
#
# choice = input('What type of shape do you want to draw?')
# shape = Client.create_shape(choice)
# shape.draw()
#
#
# from abc import ABCMeta, abstractmethod
# class FactoryShape(metaclass=ABCMeta):
#         @abstractmethod
#         def draw(self):
#                 pass
#
# class Circle(FactoryShape):
#         def draw(self):
#                 print('circle shape')
#
# class Square(FactoryShape):
#         def draw(self):
#                 print('square shape')
#
# class Triangle(FactoryShape):
#         def draw(self):
#                 print('trinagle shape')
#
# class Client:
#         @staticmethod
#         def create_shape(shape_type):
#                 if shape_type == 'Circle':
#                         return Circle()
#                 if shape_type == 'Square':
#                         return Square()
#                 if shape_type == 'Triangle':
#                         return Triangle()
#                 print('Invalid shape')
#                 return -1
#
#
# if __name__ == '__main__':
#     choice = input('What type of shape do you want to draw:')
#     shape = Client.create_shape(choice)
#     shape.draw()
