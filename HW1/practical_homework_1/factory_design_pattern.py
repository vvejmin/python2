from abc import ABCMeta


# 1
class ShapeFactory(metaclass=ABCMeta):
        def draw(self):
                pass


class Circle(ShapeFactory):
        def __init__(self):
           pass

        def draw(self):
            print('circle shape')


class Square(ShapeFactory):
        def draw(self):
                print('square shape')


class Triangle(ShapeFactory):
        def draw(self):
                print('triangle shape')


class Client:
        @staticmethod
        def create_shape(shape_type):
                if shape_type == 'Circle':
                        return Circle()
                if shape_type == 'Square':
                        return Square()
                if shape_type == 'Triangle':
                        return Triangle()
                print("Invalid type")
                return -1


if __name__ == '__main__':
        choice = input('What type of shape do you want to draw?')
        shape = Client.create_shape(choice)
        shape.draw()


# 2

class BankAccountFactory(metaclass=ABCMeta):
        def create_account(self):
                pass


class BankAccount(BankAccountFactory):
        def create_account(self):
                pass


class PersonalAccount(BankAccount):
        def create_account(self):
                print('This account is a personal account')


class BusinessAccount(BankAccount):
        def create_account(self):
                print('This account is a business account')


class Client:
        @staticmethod
        def create_account_client(account_type):
                if account_type == 'Personal':
                        return PersonalAccount()
                if account_type == 'Business':
                        return BusinessAccount()
                print("Invalid type")
                return -1


if __name__ == '__main__':
        choice_2 = input('What type of account do you want to create?')
        account = Client.create_account_client(choice_2)
        account.create_account()


# 3
class GUIFactory:
     def createButton(self):
         pass

     def createCheckbox(self):
         pass


class MacFactory(GUIFactory):
        def createButton(self):
                print('mac button')

        def createCheckbox(self):
                print('mac checkbox')


class WinFactory(GUIFactory):
        def createButton(self):
                print('win button')

        def createCheckbox(self):
                print('win checkbox')


class Application(GUIFactory):
    def __init__(self, factory, button):
                self.__factory = factory
                self.__button = button

    def create_UI(button_type):
            if button_type == 'MacButton':
                    return MacFactory()

            if button_type == 'WinButton':
                    return WinFactory()

    def paint(checkbox_type):
        if checkbox_type == 'MacCheckbox':
            return MacFactory()
        if checkbox_type == 'WinCheckbox':
            return WinFactory()


if __name__ == '__main__':
        choice = input('what is your button type?')
        btn = Application.create_UI(choice)
        btn.createButton()

        choice_2 = input('what is your checkbox type?')
        check_box = Application.paint(choice_2)
        check_box.createCheckbox()