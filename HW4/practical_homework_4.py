from __future__ import annotations
from abc import ABC, abstractmethod

class Email(ABC):
        def send(self):
                pass


class SMS(ABC):
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




