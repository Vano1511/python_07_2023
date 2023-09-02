import random
class Person:

    def __init__(self, surname, name, patronymic, age):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.__age = age

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} {self.__age} '

class Employee(Person):
    def __init__(self, surname, name, patronymic, age):
        super().__init__(surname, name, patronymic, age)
        self.id = random.randint(100000, 999999)
        self.level = sum(map(int, str(self.id))) % 7


if __name__ == '__main__':
    p1 = Employee("Ivanov", 'Ivan', 'Ivanovich', 25)
    print(p1.get_age())
    print(p1.id)
    print(p1.level)
    p1.birthday()
    print(p1.get_age())
