class Borg:

        # state shared by each instance
        __shared_state = dict()

        # constructor method
        def __init__(self):

                self.__dict__ = self.__shared_state
                self.state = 'some state'


obj1 = Borg()
obj2 = Borg()
obj3 = Borg()

print(obj1.state)
print(obj2.state)

obj1.state = 'object1 state' # obj1 changed the state
obj2.state = 'object2 state' # obj2 changed the state

print(obj1.state)
print(obj2.state)

# Government elections

class Government:

        __shared_state = dict()

        def __init__(self):
                self.__dict__ = self.__shared_state

        def choose_president(self, candidate):
                self.president = candidate

russian_gov = Government()
russian_gov.president = 'Putin'
print(russian_gov.president)
moldovian_gov = Government()
moldovian_gov.president

# class Singleton:
#
#         __shared_instance = 'initial_state'
#
#         @staticmethod
#         def getInstance():
#
#                 """Static Access Method"""
#                 if Singleton.__shared_instance == 'initial_state':
#                         Singleton()
#                 return Singleton.__shared_instance
#
#         def __init__(self):
#
#                 if Singleton.__shared_instance != 'initial_state':
#                         raise Exception("This class is a singleton class !")
#                 else:
#                         Singleton.__shared_instance = self
#
#
# obj = Singleton()
# print(obj)
# obj = Singleton.getInstance()
# print(obj)
# obj1 = Singleton()

class DBConnection:

        __shared_instance = 'not connected'

        @staticmethod
        def getInstance():

                """Static Access Method"""
                if DBConnection.__shared_instance == 'not connected':
                        DBConnection()
                return DBConnection.__shared_instance

        def __init__(self):

                if DBConnection.__shared_instance != 'not connected':
                        raise Exception("This class is a singleton class !")
                else:
                        DBConnection.__shared_instance = self

        def connect(self):
                print('Connection established!')


conn1 = DBConnection()
conn1.connect()

# Adapter design pattern

import abc





class Target(metaclass=abc.ABCMeta):
        """ Define the domain-specific interface that Client uses."""

        def __init__(self):
                self.adaptee = Adaptee()

        @abc.abstractmethod
        def request(self):
                pass


class Adapter(Target):
        """
        Adapt the interface of Adaptee to the Target interface.
        """

        def request(self):
                print(self.adaptee.specific_request()[::-1])

class Adaptee:
        """
        Define an existing interface that needs adating.
        """

        def specific_request(self):
                return "!olleH"

adapter = Adapter()
adapter.request()

import numpy as np
# Adaptee1
class EuropeanSocket:

        def __init__(self):
                self.voltage = 219

# Adaptee2
class USSocket:

        def __init__(self):
                self.voltage = 109





class Adapter:

        def get_available_adapter(self):
                return EUtoUSAAdapter()

class EUtoUSAAdapter:

        def __init__(self):
                self.voltage_range = np.arange(0,110)


# Client
class ElectricKettle:

        def __init__(self, voltage, adapter, socket):
                self.voltage = voltage
                self.adapter = adapter
                self.socket = socket

        def boil(self):
                if self.socket.voltage not in self.adapter.voltage_range:
                        print("Kettle on fire!")
                else:
                        print('Coffee time!')

socket = USSocket()
adapter = Adapter().get_available_adapter()
kettle = ElectricKettle(200, adapter, socket)
kettle.boil()
