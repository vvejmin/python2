# 1
import time


class ServerWebsite:

        def __init__(self, images):
                self.server_db_proxy = ServerProxy(images)

        def enter_db(self):
                self.server_db_proxy.loading()


class Image:

        def __init__(self, img_shape, size):
                self.img_shape = img_shape
                self.size = size
                self.server_website = ServerWebsite(self)

        def enter_db(self):
                self.server_website.enter_db()


class Server:

        def loading(self):
                print("The image is loading.")


class ServerProxy:

        def __init__(self, img):
                self.img = img

        def loading(self):
                print("Proxy in action.")
                print(f'{self.img_shape} + {self.size}')


img_1 = Image('square', 3 * 4, )
img_1.enter_db()
print('\n')


# 2
class TreeFactory:
        def __init__(self):
                self.tree_type = TreeType()

        def getTreeType(self):
                return {self.name, self.color, self.texture}



class TreeType:

        def __init__(self, name, color, texture):
            self.__name = name
            self.__color = color
            self.__texture = texture

        def draw(self, canvas,x,y):
            self.canvas = x
            self.canvas = y

class Tree:
        def __init__(self, x, y):
                self.x = x
                self.y = y
                self.type = TreeType()

        def draw(self, canvas):
                self.canvas = canvas

class Forest(Tree):
        def __init__(self):
                pass

        def plantTree(self, x, y, name, color, texture):
                pass

        def draw(self, canvas):
                pass