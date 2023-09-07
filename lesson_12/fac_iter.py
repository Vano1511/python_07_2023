class Factorial:

    def __init__ (self, *args):
        if len(args) == 3:
            self.start, self.stop, self.step = args
        elif len(args) == 2:
            self.start, self.stop = args
            self.step = 1
        elif len(args) == 1:
            self.stop = args[0]
            self.start = 1
            self.step = 1

    def __iter__ (self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            res: int = 1
            for el in range(1, self.start+1):
                res *= el
            self.start += self.step
            return res
        raise StopIteration


if __name__ == "__main__":
    a = Factorial(1, 10, 2)
    for i in a:
        print(i)
