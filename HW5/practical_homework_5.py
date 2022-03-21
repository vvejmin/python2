#1
def and_wrapper(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)

        return f'&&& {value} &&&'
    return wrapper

def asteriks_wrapper(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)

        return f'*** {value} ***'
    return wrapper

class Person:

        def __init__(self, first_name, last_name, email, age):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.age = age

        def print_information(self):
            if self.age < 14:
                @asteriks_wrapper
                @and_wrapper
                def printer():
                    return self.__base_printer()

            else:
                @and_wrapper
                def printer():
                    return self.__base_printer()
            return printer()

        def __base_printer(self):
            return f'{self.first_name} - {self.last_name} - {self.email}'


person1 = Person('A', 'B', 'a@gmail.com', 12)
print(person1.print_information())

person2 = Person('A', 'B', 'b@gmail.com', 15)
print(person2.print_information())




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