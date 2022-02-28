# 1
import abc


class Target(metaclass=abc.ABCMeta):

        def __init__(self):
                self.adaptee = Adaptee()

        @abc.abstractmethod
        def words(self):
                pass


class Adapter(Target):
        def words(self):
                print(self.adaptee.specific_words())


class Adaptee:

        def specific_words(self):
                return ['girasol', 'pájaro']


adapter = Adapter()
adapter.words()
# 2
