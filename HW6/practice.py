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


img_1 = Image('square',3*4,)
img_1.enter_db()
print('\n')

