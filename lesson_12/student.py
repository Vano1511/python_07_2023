import csv
from statistics import mean

subjects_file = "subjects.csv"


def import_subjects():
    """Imports all student's subjects and returns they in tuple."""
    with open(subjects_file, encoding="utf-8") as file:
        data = []
        reader = csv.reader(file)
        for el in reader:
            data.append(el[0])
    return tuple(data)


class Snp:
    """Descriptor class who checks surname, name and patronymic to content only letters and capitalize.
    If not capitalize - fix it, if word have digits - raise exception."""
    def __set_name__(self, owner, name):
        self._param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value: str):
        new_value = self.validate(value)
        setattr(instance, self._param_name, new_value)

    @staticmethod
    def validate(value: str):
        if value:
            new_value = value.title()
            if new_value.isalpha():
                return new_value
            raise ValueError("surname, name and patronymic must contains only letters")
        return value


class Student:
    """create objects which have params:
     - name(necessarily)
     - surname(necessarily)
     - patronymic(can be None)
     - subjects(import from csv file)
     - marks (dict where keys are subjects, values are list of marks from 2 to 5)
     - test_marks (dict where keys are subjects, values are list of marks from 0 to 100)
     and methods:
     - validate_subject(validate that student have subject takes string raise exception if wrong)
     - recieve_mark(recieve subject and mark and validate it, variable test is bool, default=False)
     - average_from_subject(recieve subject and give average of marks)-> float
     - average_mark(give average mark of all subjects, variable test is bool)-> float
     """
    surname = Snp()
    name = Snp()
    patronymic = Snp()

    def __init__(self, surname: str, name: str, patronymic: str = None):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.__subjects = import_subjects()
        self.marks = {key: [] for key in self.__subjects}
        self.test_marks = {key: [] for key in self.__subjects}

    def __repr__(self):
        return f"Student(surname={self.surname}, name={self.name}, patronymic={self.patronymic})"

    def __str__(self):
        return (f"Student: {self.surname} {self.name}\n"
                f"marks: {self.marks}\n"
                f"tests: {self.test_marks}\n"
                f"avg mark = {self.average_mark()}\n"
                f"average tests = {self.average_mark(test=True)}")

    def recieve_mark(self, subject: str = None, mark: int = 0, test: bool = False):
        self.validate_subject(subject)
        if test:
            if 0 <= mark <= 100:
                self.test_marks[subject].append(mark)
            else:
                raise ValueError("test mark must be in range from 0 to 100")
        else:
            if 2 <= mark <= 5:
                self.marks[subject].append(mark)
            else:
                raise ValueError("mark must be in range from 2 to 5")

    @property
    def all_subjects(self):
        return self.__subjects

    def validate_subject(self, subject: str):
        if subject not in self.__subjects:
            raise ValueError(f"student doesn't have subject {subject}, only {self.__subjects}")

    def average_from_subject(self, subject: str, test: bool = False) -> float:
        self.validate_subject(subject)
        if test:
            return mean(self.test_marks[subject])
        return mean(self.marks[subject])

    def average_mark(self, test: bool = False) -> float:
        all_marks = []
        if test:
            for val in self.test_marks.values():
                if isinstance(val, int):
                    all_marks.append(val)
                else:
                    all_marks.extend(val)
        else:
            for val in self.marks.values():
                if isinstance(val, int):
                    all_marks.append(val)
                else:
                    all_marks.extend(val)
        if all_marks:
            return round(mean(all_marks), 3)
        else:
            return 0.0


if __name__ == "__main__":
    # stud2 = Student("Petrov1", "Petr", "petrovicz") #exception
    stud1 = Student("ivanov", "iVan")
    stud1.recieve_mark("mathematics", test=True, mark=75)
    stud1.recieve_mark("economy", test=True, mark=86)
    stud1.recieve_mark("economy", mark=5)
    stud1.recieve_mark("economy", mark=4)
    stud1.recieve_mark("physic", mark=3)
    stud1.recieve_mark("physic", mark=5)
    stud1.recieve_mark("physic", mark=99, test=True)
    stud1.recieve_mark("sociology", mark=64, test=True)
    stud1.recieve_mark("history", mark=70, test=True)
    stud1.recieve_mark("programming", mark=82, test=True)
    stud1.recieve_mark("geometry", mark=79, test=True)
    # stud1.recieve_mark("ewfwefw", mark=5) # exception
    # stud1.recieve_mark("geometry", mark=39) #exception
    stud1.recieve_mark("geometry", mark=4, test=True)
    stud1.recieve_mark("programming", mark=5)
    stud1.recieve_mark("history", mark=4)
    stud1.recieve_mark("geometry", mark=5)
    stud1.recieve_mark("mathematics", mark=5)
    stud1.recieve_mark("mathematics", mark=5)
    stud1.recieve_mark("sociology", mark=2)
    print(stud1)
    print(stud1.all_subjects)
    print(f"{stud1.average_from_subject('geometry', test=True) = }")
