class Abstraction:
    __year = None
    __sep = None

    def __init__(self, year:int, sep:str) -> None:
        self.__year = year
        self.__sep = sep

    def Year(self):
        return self.__year

    def Sep(self):
        return self.__sep