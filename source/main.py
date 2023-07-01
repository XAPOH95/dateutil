from .abi_month.behavior import Constructor
from .abi_year.behavior import Behavior as Year
from .contract import CShortRepresentation, CLongRepresentation, CIndexRepresentation, CComparision, COffset

class Month(CShortRepresentation, CLongRepresentation, CIndexRepresentation, CComparision, COffset):
    def __init__(self, month) -> None:
        self.__month = Constructor(month).construct_month()

    def RuFull(self):
        return self.__month.full_ru_name()
    
    def EngFull(self):
        return self.__month.full_eng_name()

    def Ru(self):
        return self.__month.short_ru_name()

    def Eng(self):
        return self.__month.short_eng_name()

    def M(self):
        return self.__month.mIndex()

    def index(self):
        return self.__month.index()

    def __repr__(self) -> str:
        return self.EngFull()

    def __str__(self) -> str:
        return self.Eng()

    def __eq__(self, __o) -> bool:
        if self.index() == __o.index():
            return True
        return False

    def __lt__(self, __o) -> bool:
        if self.index() < __o.index():
            return True
        return False

    def __gt__(self, __o) -> bool:
        if self.index() > __o.index():
            return True
        return False

    def __le__(self, __o) -> bool:
        if self.index() <= __o.index():
            return True
        return False

    def __ge__(self, __o) -> bool:
        if self.index() >= __o.index():
            return True
        return False

    def __sub__(self, offset:int) -> "Month":
        return Month(int(self) - offset)

    def __add__(self, offset:int) -> "Month":
        return Month(int(self) + offset)

    def __int__(self):
        return self.index()

class MonthYear(CShortRepresentation):
    """Role of class is to show trimmed month and year with separator between.
    
    Month trimmed to 3 chars and year is trimmed to 2 chars."""
    def __init__(self, month, year, separator) -> None:
        self.__month = Constructor(month).construct_month()
        self.__year = Year(year, separator)

    def Ru(self) -> str:
        return self.__month.short_ru_name() + self.__year.Short()

    def Eng(self) -> str:
        return self.__month.short_eng_name() + self.__year.Short()

    def __str__(self) -> str:
        return self.Eng()

    def __repr__(self) -> str:
        return self.Eng()

