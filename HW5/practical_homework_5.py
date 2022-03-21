#1
def person(func):
        def wrapper(*args, **kwargs):
                value = func(*args, **kwargs)

                return f'&&& {value} &&&'
        return wrapper

@person
def asteriks_wrapper(func):
        pass

class Person:

        def __init__(self, name, last_name, age, email):
                self.name = name
                self.last_name = last_name
                self.age = age
                self.email = email

        def print_info(self):
                pass

person = Person()



# 2
import time

def time_to_sleep(func):
        def wrapper():
                begin = time.time()

                func()

                end = time.time()
                print("total time taken in :", func.__name__, end - begin)
        return wrapper

@time_to_sleep
def text():
    print("Happy pi day!")
    time.sleep(2)
    return None

print(text())


# 3
class Dispatcher:
        def dispatch_order(self):
            print("what do you want?")


class Resturant:

        def cook_food(self):
                print("the food is ready!")


class DeliveryGuy:
        def delivered_food(self):
                print("the food is delivered!")


class Food:

        def __init__(self):
                self.dispatcher = Dispatcher()
                self.resturant = Resturant()
                self.delivery_guy = DeliveryGuy()

        def organize_priority(self):
                self.dispatcher.dispatch_order()
                self.resturant.cook_food()
                self.delivery_guy.delivered_food()


food = Food()
food.organize_priority()