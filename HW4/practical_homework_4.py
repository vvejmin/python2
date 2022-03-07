from __future__ import annotations
from abc import ABC, abstractmethod


class ProducingAPI(ABC):

        @abstractmethod
        def produceCuboid(self, length, breadth, height):
                pass


class ProducingAPI1(ProducingAPI):
        """Implementation specific"""

        def produceCuboid(self, length, breadth, height):
                print(f'API1 is  a producing Cuboid with length = {length}',
                      f'Breadth = {breadth} and Height = {height}')


class ProducingAPI2(ProducingAPI):
        """ Implementation specific """

        def produceCuboid(self, length, breadth, height):
                print(f'API2 is a producing Cuboid with length = {length}, ',
                      f'Breadth = {breadth} and Height = {height}')


class Cuboid:

        def __init__(self, length, breadth, height, producingAPI):
                """Implementation independent"""
                self._length = length
                self._breadth = breadth
                self._height = height
                self._producingAPI = producingAPI

        def produce(self):
                self._producingAPI.produceCuboid(self._length, self._breadth, self._height)

        def expand(self, times):
                """Implementation independent"""

                self._length = self._length * times
                self._breadth = self._breadth * times
                self._height = self._height * times


cuboid1 = Cuboid(1, 2, 3, ProducingAPI1())
cuboid1.produce()

cuboid2 = Cuboid(19, 19, 19, ProducingAPI2())
cuboid2.produce()

class LeafElement:
        '''Class representing objects at the bottom or Leaf of the hierarchy tree.'''

        def __init__(self, position, salary):

                '''Takes the first positional argument and assigns to member variable "position"'''
                self.position = position
                self.salary = salary

        def showDetails(self):

                '''Prints the position and salary of the child element.'''
                print("\t", end="")
                print(f"position - {self.position}, salary - {self.salary}")

class CompositeElement:
        '''Class representing objects at any level of the hierarchy tree except for the bottom or leaf level. Maintains the child objects by adding and removing them from the tree structure.'''
        def __init__(self, position, salary):
                self.position = position
                self.salary = salary
                self.children = []

        def add(self, child):
                self.children.remove(child)

        def showDetails(self):
                print(self.position)
                ch_salary = self.report_children_salary()
                print(ch_salary)
                for child in self.children:
                        print("\t", end="")
                        child.showDetails()

        def report_children_salary(self):
                res_sal = sum([ch.salary for ch in self.children])
                return res_sal

topLevelMenu = CompositeElement("GeneralManager", 1000)
subMenuItem1 = CompositeElement("Manager1", 500)
subMenuItem2 = CompositeElement("Manager2", 500)
subMenuItem11 = LeafElement("Developer11", 100)
subMenuItem12 = LeafElement("Developer12", 100)
subMenuItem21 = LeafElement("Developer21", 100)
subMenuItem22 = LeafElement("Developer22", 100)

subMenuItem1.add(subMenuItem11)
subMenuItem1.add(subMenuItem12)


class Email:
        def send(self):
                pass


class SMS:
        def send(self):
                pass


# problem 2
class InstrumentCollection:
        def Make(self):
                pass

class Box(InstrumentCollection):
        def __init__(self, instruments: list):
                self._instruments = instruments

        def Make(self):
                pass

        def Remove(instr):
                pass

        def GetChild(self):
                pass

class Pen(InstrumentCollection):
        def Make(self):
             pass

class Pencil(InstrumentCollection):
        def Make(self):
                pass

class Rubber(InstrumentCollection):
        def Make(self):
                pass




