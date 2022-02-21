from abc import ABCMeta, abstractmethod, abstractproperty, ABC


class AbstractBuilder(ABC):

        @abstractmethod
        def create_id(self, id):
                pass

        @abstractmethod
        def create_balance(self, balance):
                pass

        @abstractmethod
        def create_rate(self, rate):
                pass

class BankAccount():

        def __init__(self):
                self.attributes = {}

        def add(self, key, value):
                self.attributes[key] = value

        def describe(self):
                print(self.attributes)

class BankAccountBuilder(BankAccount):

        def __init__(self):
                self.bank_account.add('id', id)

        def create_balance(self, balance):
                self.bank_account.add('balance', balance)

        def create_rate(self, rate):
                self.bank_account = rate

from abc import ABCMeta, abstractmethod
import copy

class Shape(ABC):

        def __init__(self):
                self.id = None
                self.type = None

        @abstractmethod
        def draw(self):
                pass

        def get_type(self):
                return self.type

        def set_type(self, _type):
                self.type = _type

        def set_type(self, _type):
                self.type = _type

        def get_id(self):
                return self.id

        def set_id(self, _id):
                self.id = _id

        def clone(self):
                return copy.copy(self)

class Circle(Shape):
        def __init__(self):
                super().__init__()

class ShapeCache:

        cache = {}

        @staticmethod
        def get(_id):
                shape = ShapeCache.cache.get(_id, None)

                return shape.clone()

ShapeCache.load()

circle = ShapeCache.get(1)
print(circle.get_type())

square = ShapeCache.get(2)
print(square.get_type())


# 1
class BankAccount:
        def __init__(self, id, balance, rate):
                self.id = id
                self.balance = balance
                self.rate = rate


account = BankAccount(2, 6000, 5)

# 2
class Shape(ABCMeta):
        pass

class Circle(Shape):
        pass

class Square(Shape):
        pass

class Rectangle(Shape):
        pass

class ShapeCache:
        cache ={'Circle':Circle, 'Square':Square,'Rectangle':Rectangle}


