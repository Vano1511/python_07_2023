class Animal:
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age

    def __str__(self) -> str:
        return f'{self.name} {self.age}'

    def birthday(self):
        self.age += 1


class Dog(Animal):
    def __init__(self,
                name: str,
                age: int,
                color: str,
                breed: str,
                is_domestic: bool = True) -> None:
        super().__init__(name, age)

        self.color = color
        self.breed = breed
        self.is_domestic = is_domestic

    def __str__(self):
        if self.is_domestic:
            return f'Dog {self.color} {self.breed} домашняя'
        return f'Dog {self.color} {self.breed} дворняга'


class Kotopes(Animal):
    def __init__(self,
                age: int,
                name: str,
                number_heads: int = 2) -> None:
        super().__init__(name, age)
        self.__number_heads = number_heads

    def __str__(self):
        return (f'Kotopes -> number_heads: {self.__number_heads}, '
                f'Возраст: {self.age}, не женат ')


class Fish(Animal):

    def __init__(self, name, age, aqua, size):
        super().__init__(name, age)
        self.aqua = aqua
        self.size = size

    def __str__(self):
        if self.aqua:
            return f'{self.name} морская'
        else:
            return f'{self.name} пресноводная'


class Factory:
    def __init__(self, type_animal: str):
        self.type_animal = type_animal
        self.third = None
        self.fourth = None
        self.fivth = None

    def create(self, name: str, age: int, **kwargs):
        """Creates a class object, depending on the type, calls the desired function.
        Takes only kwargs arguments."""
        if self.type_animal.capitalize() == "Fish":
            for key, value in kwargs.items():
                if key == "aqua":
                    self.third = value
                elif key == "size":
                    self.fourth = value
            res_obj = Fish(name, age, self.third, self.fourth)
            return res_obj
        elif self.type_animal.capitalize() == "Kotopes":
            for key, value in kwargs.items():
                if key == "number_heads":
                    self.third = value
            res_obj = Kotopes(age, name, self.third)
            return res_obj
        elif self.type_animal.capitalize() == "Dog":
            for key, value in kwargs.items():
                if key == "color":
                    self.third = value
                elif key == "breed":
                    self.fourth = value
                elif key == "is_domestic":
                    self.fivth = value
            res_obj = Dog(name, age, self.third, self.fourth, self.fivth)
            return res_obj


if __name__ == "__main__":
    dog = Dog('Бобик', 3, "рыжий", "спаниель", True)
    fishes = Factory("Fish")
    fish1 = fishes.create("Dori", 2, aqua="river", size=7)
    dogs = Factory("dog")
    dog1 = dogs.create(name="Bobik", age=5, is_domestic=True, color="white", breed="Bulldog")
    print(fish1.__dict__)
    print(dog1.__dict__)
