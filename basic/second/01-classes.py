#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  Основы ООП - конструктор, наследование, перегрузка, полиморфизм, инкапсуляция
#
class User:
    first_name: str
    last_name: str

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"Fullname: {self.first_name} {self.last_name}"

    def show_age(self):
        print("I have no age")

class AgedUser(User):
    _age: int


    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name)
        self._age = age

    def show_age(self):
        print(self._age)

aged_john = AgedUser("John", "Doe", 30)

print(aged_john.full_name(), aged_john._age)
aged_john.show_age()

