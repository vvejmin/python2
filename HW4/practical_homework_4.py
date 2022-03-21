from __future__ import annotations
from abc import ABC, abstractmethod

class MessageSender(ABC):

        @abstractmethod
        def send(self, texts, imgs):
               pass

class EmailSender(MessageSender):
    def send(self, texts, imgs):
       print(f'the email is {texts} {imgs}')


class SMSSender(MessageSender):
    def send(self, texts):
            print(f'the email is {texts}')

class Client:
        def __init__(self, sender):
                self.sender = sender

        def send_message(self, text):
            self.sender.send.text

client1 = Client(EmailSender())
client1.send_message('Hello')


client2 = Client(EmailSender())
client2.send_message('Hello')

# problem 2
class Instrument:

        def __init__(self, functionality):
                self.functionality = functionality

        def make(self):
                self.
class InstrumentCollection:
        def __init__(self, functionality):
                self.functionality = self.instrument_collections = []

box = Box('Box')





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




