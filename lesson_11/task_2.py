class Archive:
    """Class Archive in which, when creating a new instance, the old one is deleted,
    and the data on it is saved in the archive parameters"""
    instance = None

    def __new__(cls, *args, **kwargs):
        """A method in which, when a new instance of a class is created, the old instance
        is overwritten and its data is stored in the history (old_text and old_int)."""
        if cls.instance:
            cls.instance.old_text.append(cls.instance.text)
            cls.instance.old_int.append(cls.instance.number)
        else:
            cls.instance = super().__new__(cls)
            cls.instance.old_text = []
            cls.instance.old_int = []
        return cls.instance

    def __init__(self, text: str, number: int) -> None:
        """Initiation method."""
        self.text = text
        self.number = number


if __name__ == "__main__":
    a1 = Archive(text='T', number=1)
    a2 = Archive(text='E', number=2)
    a3 = Archive(text='Z', number=3)

    print(a2.old_text)
    print(a2.old_int)

    print('---')

    print(a3.text)
    print(a3.number)
