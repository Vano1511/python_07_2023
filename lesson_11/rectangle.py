class Rectangle:
    """The class who introduces rectangles/"""
    def __init__(self,
                length_cm: float,
                width_cm: float = None) -> None:
        """The initiation method."""
        self.length = length_cm
        if width_cm:
            self.width = width_cm
        else:
            self.width = length_cm

    def calc_len(self):
        """Calculates the perimetr of rectangle."""
        return (self.width + self.length) * 2

    def calc_square(self):
        """Calculates the square of rectangle."""
        return self.width * self.length

    def __add__(self, other: "Rectangle"):
        """The add method with class instances."""
        return Rectangle(length_cm=self.length + other.length,
                        width_cm=self.width)

    def __sub__(self, other: "Rectangle"):
        """The subtract method with class instances."""
        return Rectangle(length_cm=abs(self.length - other.length),
                width_cm=self.width)

    def __eq__(self, other: "Rectangle"):
        """The equal method with class instances."""
        return self.calc_square() == other.calc_square()

    def __lt__(self, other: "Rectangle"):
        """The lower than method with class instances."""
        return self.calc_square() < other.calc_square()

    def __gt__(self, other: "Rectangle"):
        """The greater than method with class instances."""
        return self.calc_square() > other.calc_square()

    def __ge__(self, other: "Rectangle"):
        """The greater and equal method with class instances."""
        return self.calc_square() >= other.calc_square()

    def __le__(self, other: "Rectangle"):
        """The lower and equal method with class instances."""
        return self.calc_square() <= other.calc_square()


if __name__ == '__main__':
    r1 = Rectangle(length_cm=2,
    width_cm=2)
    print(f'{r1.calc_len() = }')
    print(f'{r1.calc_square() = }')
    print('---')
    r2 = Rectangle(length_cm=3)
    print(f'{r2.calc_len() = }')
    print(f'{r2.calc_square() = }')
    r3 = r2 + r1
    print('---')
    print(f'{r3.calc_len() = }')
    print(f'{r3.calc_square() = }')
    print('---')
    print(r1 <= r2)
