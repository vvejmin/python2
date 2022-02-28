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
                return {'sunflower':'girasol', 'bird':'pájaro'}

adapter = Adapter()
adapter.words()
adapter.translator()

# 2
class Singleton:
        __shared_state = dict()

        def __init__(self):
                self.__dict__ = self.__shared_state

        def busy_to_free(self):
                if Singleton.__shared_state == 'busy':
                        Singleton()
                return Singleton.__shared_state

        def free_to_busy(self):
                if Singleton.__shared_state ==  'free':
                        Singleton()
                return Singleton.__shared_state

free  = Singleton()
free.busy_to_free()