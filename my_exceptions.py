class MyException(Exception):
    pass


class MarkError(MyException):
    def __init__(self, mark: int, min_val: int, max_val: int):
        self.mark = mark
        self.min_val = min_val
        self.max_val = max_val

    def __str__(self):
        return (f"The mark must be in range from {self.min_val} to {self.max_val}\n"
                f"you got - {self.mark}")


class NotSubjectFoundError(MyException):
    def __init__(self, subject: str, subj_list: tuple):
        self.subject = subject
        self.subj_list = subj_list

    def __str__(self):
        return f"There is no {self.subject} in student's subjects: {self.subj_list}"


class MatrixShapesError(MyException):
    def __init__(self, shape_1: tuple, shape_2: tuple):
        self.shape_1 = shape_1
        self.shape_2 = shape_2

    def __str__(self):
        return (f"We must have matrix with same shapes!\n"
                f"but we have {self.shape_1} and {self.shape_2}")


class AnyNameError(MyException):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.name} must contains with only letters"
