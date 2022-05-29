# from abc import ABC, abstractmethod
#
#
# class Builder(ABC):
#         @abstractmethod
#         def produce_part_a(self):
#                 pass
#
#         @abstractmethod
#         def produce_part_b(self):
#                 pass
#
#         @abstractmethod
#         def produce_part_c(self):
#                 pass
#
#
# class ConcreteBuilder(Builder):
#         def __init__(self):
#                 self.product = Product1()
#
#         def produce_part_a(self):
#                 self.product.add('PartA1')
#
#         def produce_part_b(self):
#                 self.product.add('PartB1')
#
#         def produce_part_c(self):
#                 self.product.add('PartC1')
#
# class Product1():
#
#         def __init__(self):
#                 self.parts = []
#
#         def add(self, part):
#                 self.parts.append(part)
#
#         def list_parts(self):
#              print(f"Product parts:{','.join(self.parts)}", end="")
#
# builder = ConcreteBuilder()
#
# print("Custom product: ")
# builder.produce_part_a()
# builder.produce_part_b()
# builder.produce_part_c()
# builder.product.list_parts()


# from abc import ABC, abstractmethod
#
# class Builder(ABC):
#         @abstractmethod
#         def produce_part_a(self):
#                 pass
#         @abstractmethod
#         def produce_part_b(self):
#                 pass
#         @abstractmethod
#         def produce_part_c(self):
#                 pass
#
# class ConcreteBuilder(Builder):
#
#         def __init__(self):
#                 self.product = Product1()
#
#         def produce_part_a(self):
#                 self.product.add('PartA1')
#
#         def produce_part_b(self):
#                 self.product.add('PartB1')
#
#         def produce_part_c(self):
#                 self.product.add('PartC1')
#
#
#
# class Product1():
#         def __init__(self):
#                 self.parts = []
#
#         def add(self,part):
#                 self.parts.append(part)
#
#
#         def list_parts(self):
#                 print(f"Product parts:{','.join(self.parts)}", end="")
#
#
# builder = ConcreteBuilder()
# print("Custom Products:")
# builder.produce_part_a()
# builder.produce_part_b()
# builder.produce_part_c()
# builder.product.list_parts()

#
# from abc import ABC, abstractmethod
#
# class Builder(ABC):
#         @abstractmethod
#         def produce_part_a(self):
#                 pass
#
#         @abstractmethod
#         def produce_part_b(self):
#                 pass
#
#         @abstractmethod
#         def produce_part_c(self):
#                 pass
#
# class ConcreteBuilder(Builder):
#
#         def __init__(self):
#                 self.product = Product1()
#
#         def produce_part_a(self):
#                 self.product.add("PartA1")
#
#         def produce_part_b(self):
#                 self.product.add("PartB1")
#
#         def produce_part_c(self):
#                 self.productk.add("PartC1")
#
# class Product1():
#
#         def __init__(self):
#                 self.parts = []
#
#         def add(self, part):
#                 self.parts.append(part)
#
#         def list_parts(self):
#                 print(f"Product parts:{','.join(self.parts)}")
#
# builder = ConcreteBuilder()
# builder.produce_part_a()
# builder.produce_part_a()
# builder.produce_part_c()
# print("Custom parts:")
# builder.product.list_parts()

# from abc import ABC, abstractmethod
#
# class Builder(ABC):
#         @abstractmethod
#         def produce_part_a(self):
#                 pass
#         @abstractmethod
#         def produce_part_b(self):
#                 pass
#         @abstractmethod
#         def produce_part_c(self):
#                 pass
#
# class ConcreteBuilder(Builder):
#         def __init__(self):
#                 self.product = Product1()
#
#         def produce_part_a(self):
#                self.product.add("PartA ")
#
#         def produce_part_b(self):
#                 self.product.add("PartB")
#
#         def produce_part_c(self):
#                 self.product.add("PartC")
#
#
# class Product1():
#         def __init__(self):
#                 self.parts = []
#
#         def add(self, part):
#                 self.parts.append(part)
#
#         def list_parts(self):
#                 print(f"Custom Parts:{','.join(self.parts)}")
#
# builder = ConcreteBuilder()
# builder.produce_part_a()
# builder.produce_part_b()
# builder.produce_part_c()
# print("Custom parts:")
# builder.product.list_parts()
# from abc import ABC, abstractmethod
#
# class Builder(ABC):
#
#         @abstractmethod
#         def produce_part_a(self):
#                 pass
#
#         @abstractmethod
#         def produce_part_b(self):
#                 pass
#
#         @abstractmethod
#         def produce_part_c(self):
#                 pass
#
# class ConcreteBuilder(Builder):
#         def __init__(self):
#                 self.product = Product1()
#
#         def produce_part_a(self):
#                 self.product.add("Part A")
#
#         def produce_part_b(self):
#                 self.product.add("Part B")
#
#         def produce_part_c(self):
#                 self.product.add("Part C")
#
# class Product1():
#         def __init__(self):
#                 self.parts = []
#
#         def add(self, part):
#                 self.parts.append(part)
#
#         def list_parts(self):
#                 print(f"Custom Parts:{','.join(self.parts)}")
#
# builder = ConcreteBuilder()
# builder.produce_part_a()
# builder.produce_part_b()
# builder.produce_part_c()
# print("Custom Products:")
# builder.product.list_parts()
# from abc import ABC, abstractmethod
#
# class Builder(ABC):
#
#         @abstractmethod
#         def produce_part_a(self):
#                 pass
#
#         @abstractmethod
#         def produce_part_b(self):
#                 pass
#
#         @abstractmethod
#         def produce_part_c(self):
#                 pass
#
# class ConcreteBuilder(Builder):
#
#         def __init__(self):
#                 self.product = Product1()
#
#         def produce_part_a(self):
#                 self.product.add("PartA")
#
#         def produce_part_b(self):
#                 self.product.add("PartB")
#
#         def produce_part_c(self):
#                 self.product.add("PartC")
#
#
# class Product1():
#         def __init__(self):
#                 self.parts = []
#
#         def add(self,part):
#                 self.parts.append(part)
#
#         def list_parts(self):
#                 print(f"Custom Parts:{','.join(self.parts)}")
#
# builder = ConcreteBuilder()
# builder.produce_part_a()
# builder.produce_part_b()
# builder.produce_part_c()
# print("Custom Products:")
# builder.product.list_parts()
import copy
from abc import ABC, abstractmethod

class Courses_At_AUA(ABC):

        def __init__(self, age):
                self.age = age
                self.id = None
                self.type = None

        @abstractmethod
        def course(self):
                pass

        def get_type(self):
                return self.type

        def get_id(self):
                return self.get_id

        def set_id(self, sid):
                self.set_id = sid

        def clone(self):
                return copy.copy(self)


class Technical_course(Courses_At_AUA):
        def __init__(self, name):
                super(Courses_At_AUA, self).__init__(age)