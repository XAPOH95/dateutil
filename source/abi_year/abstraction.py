class Abstraction:
    __year = None
    __month = None
    __sep = None

    def __init__(self, month,  year:int, sep:str) -> None:
        self.__year = year
        self.__month = month
        self.__sep = sep

    def Year(self):
        return self.__year

    def Month(self):
        return self.__month

    def Sep(self):
        return self.__sep