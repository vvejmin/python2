from __future__ import annotations
from abc import ABC, abstractmethod

class MessageSender(ABC):

        @abstractmethod
        def send(self, texts):
               pass

class EmailSender(MessageSender):

    def send(self, text):
       print(f'Sending Email: {text}')


class SMSSender(MessageSender):
    def send(self, text):
            print(f'Sending SMS: {text}')

class Client:

    def __init__(self, sender):
        self.sender = sender

    def send_message(self, text):
        self.sender.send(text)

client1 = Client(EmailSender())
client1.send_message('Hello')


client2 = Client(SMSSender())
client2.send_message('Hello')

# problem 2
class Instrument:

    def __init__(self, functionality):
        self.functionality = functionality

    def make(self):
        print('\t', end= '')
        print(self.functionality)


class InstrumentCollection:

    def __init__(self, collection_id):
        self.collection_id = collection_id
        self.instruments = []

    def add(self, instrument):
            self.instruments.append(instrument)

    def remove(self):
        self.instruments.remove()

    def make(self):
        print(self.collection_id)

        for instrument in self.instruments:
                print('\t', end = '')
                instrument.make()

class Box:

      def __init__(self, functionality):
              self.functionality = functionality
              self.instrument_collections = []

      def make(self):
          print(self.functionality)

          for instrument_c in self.instrument_collections:
              print('\t', end = '')
              instrument_c.make()

      def add(self, instrument_c):
              self.instrument_collections.append(instrument_c)

      def remove(self, instrument_c):
              self.instrument_collections.remove(instrument_c)

box = Box('Box')
col1 = InstrumentCollection('Collection 1')
col2 = InstrumentCollection('Collection 2')
pen = Instrument('Pen')
pencil = Instrument('Pencil')
rubber = Instrument('Rubber')

col1.add(pen)
col1.add(pencil)

box.add(col1)
box.add(col2)

box.make()
