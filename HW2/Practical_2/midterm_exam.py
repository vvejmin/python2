# 1
from abc import ABC, abstractmethod
class AbstractHandler(ABC):
      def __init__(self):
              pass

      def handle(request):
              pass

      @abstractmethod
      def processRequest(request):
              pass


class DataScience(AbstractHandler):
        @staticmethod
        def process_request():
                print("data science team tasks")

class QA(AbstractHandler):
        @staticmethod
        def process_request():
                print("qa team tasks")

class Design(AbstractHandler):
        @staticmethod
        def process_request():
            print("design team tasks")

class DefaultHandler(AbstractHandler):
        @staticmethod
        def processRequest():
                print("other team tasks")


class Client:


        @staticmethod
        def call(requests):
                ds = ['analyze','research','model']
                design = ['words','color','decorator']
                qa = ['test']

                if requests in ds:
                        return DataScience.process_request()
                if requests in design:
                        return Design.process_request()
                if requests in qa:
                        return QA.process_request()


if __name__ == '__main__':
   tasks = Client()
   tasks.call('analyze')
   tasks.call('test')

# 2
class ChristmasTree:
    def __init__(self, id):
            self.id = id


    def show(self):
             print(f"This is a christmasTree { self.id } I am decorated with: {self.christmasStar} {self.garland}  {self.lights}")





class TreeDeocrator:
        pass



class ChristmasStar:
        def __init__(self, christmasStar):
                self.christmasStar = christmasStar



class Garland:
      def __init__(self, garland):
            self.garland = garland

class Lights:
        def __init__(self, lights):
                self.lights = lights


if __name__ == '__main__':
        christmasStar = ChristmasStar("star")
        garland = Garland("garland")
        lights = Lights("lights")
        christmasTree = ChristmasTree(4)
        christmasTree.show()








