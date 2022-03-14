# 1
# class Person:
#           def __init__(self, name, last_name, email, age):
#                   self.name = name
#                   self.last_name = last_name
#                   self.email = email
#                   self.age = age
#
#           def age(self):
#                 pass
#
# class Decorator(Person):
#
#         def __init__(self, person:Person):
#                 super().__init__(self.name, self.last_name, self.email, self.age)
#                 self._person = person
#
#         def age(self):
#                 if self._person.age < 14:
#                        print(f'&&& self._person.name - self._person.last_name - self._person.email &&&')
#                 else:
#                         print(f'&&& self._person.name - self._person.last_name - self._person.email')
#
# def client_code(person: Person):
#         print(f'RESULT: {person.age()}', end='')
#
# new_person = Decorator('Ejmin','Vartoumian','Vartoumian.Ejmin91@gmail.com',31)
# client_code(new_person)





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