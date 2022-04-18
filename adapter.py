from abc import ABC, abstractmethod

class Target(ABC):
        """Define the domain-specific interface that Client uses."""

        def __init__(self):
                self.adaptee = Adaptee()

        @abstractmethod
        def request(self):
                pass

class Adapter(Target):
        """Adapt the interface of Adaptee to the Target interface."""
        def request(self):
                print(self.adaptee.specific_request()[::-1])

class Adaptee():
        """Define an existing interface that needs adapting."""
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

# Adapter
class Adapter:

        def get_available_adapter(self):
                return EUtoUSAdapter()

class EUtoUSAdapter:

        def __init__(self):
                self.voltage_range = np.arange(0,110)

#Client
class ElectricKettle:

        def __init__(self, voltage, adapter, socket):

                self.voltage = voltage
                self.adapter = adapter
                self.socket = socket

        def boil(self):
            if self.socket.voltage not in self.adapter.voltage_range:
                print("Kettle on fire!")
            else:
                print("Coffee time!")

socket = USSocket()
adapter = Adapter().get_available_adapter()
kettle = ElectricKettle(200, adapter, socket)
kettle.boil()
