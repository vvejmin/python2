# 1
import abc


class Target(metaclass=abc.ABCMeta):

        def __init__(self):
                self.adaptee = Adaptee()

        @abc.abstractmethod
        def words(self):
                pass

        @abc.abstractmethod
        def translator(self):
                pass


class Adapter(Target):
        def words(self):
                print(self.adaptee.specific_words())

        def translator(self):
                print(self.adaptee.specific_translated_words())


class Adaptee:

        def specific_words(self):
                return ['girasol', 'pájaro']

        def specific_translated_words(self):
                return {'sunflower': 'girasol', 'bird': 'pájaro'}


adapter = Adapter()
adapter.words()
adapter.translator()


# 2
import numpy as np
from abc import ABCMeta,abstractmethod

class Video:

        def play(self):
                pass

class Media:
        pass

class MediatoVideo:
        pass

#Client
class Musician:

        def __init__(self, media, adapter, player):
                self.media = media
                self.adapter = adapter
                self.player = player

        def play(self):
                self.media = self.adapter.convert_file()
                if (self.media.hasAudio == self.player.supportsAudio):
                        pass


# 3
class Singleton:
        __shared_state = dict()

        def __init__(self):
                self.__dict__ = self.__shared_state

        def choose(self, choice):
                self.choice = choice


        def busy_to_free(self):
                if Singleton.__shared_state == 'busy':
                        Singleton()
                return Singleton.__shared_state

        def free_to_busy(self):
                if Singleton.__shared_state == 'free':
                        Singleton()
                return Singleton.__shared_state


free = Singleton()
free.choice = 'busy'
busy = Singleton()
print(free.busy_to_free())
