from .abstration import Abstraction, Collection
from .interface import IConstructor, Iindex, IName

class Behavior(Abstraction, Collection, Iindex, IName):
    def __init__(self, month: int) -> None:
        super().__init__(month)

    def full_ru_name(self) -> str:
        return self.LongRu()[self.Month()]

    def full_eng_name(self) -> str:
        return self.LongEng()[self.Month()]

    def short_ru_name(self) -> str:
        return self.ShortRu()[self.Month()]

    def short_eng_name(self) -> str:
        return self.ShortEng()[self.Month()]

    def index(self) -> int:
        index = self.Month()
        if index < 0:
            return 0
        return index + 1

    def mIndex(self):
        index = self.index()
        if index >= 10:
            return f"M{index}"
        return f"M0{index}"

class Constructor(Collection, IConstructor):
    __value = None

    def __init__(self, value) -> None:
        self.__value = value

    def construct_month(self):
        if isinstance(self.__value, int):
            return self._fromInt()
        elif isinstance(self.__value, str):
            return self._fromString()
        else:
            raise TypeError(self.__value)

    def _fromInt(self):
        if self.__value > 12:
            self.__value = self.__value // 12
        elif self.__value < 0:
            self.__value = abs(self.__value)
        return Behavior(self.__value - 1)

    def _fromString(self):
        self.__value = self.__value.lower()
        index = self._find_month_index(self.__value)
        return Behavior(index)

    def _find_month_index(self, month:str) -> int:
        inRu = [i for i in self.ShortRu() if month.startswith(i)]
        inEng = [i for i in self.ShortEng() if month.startswith(i)]
        if any(inRu):
            return self.ShortRu().index(inRu[0])
        elif any(inEng):
            return self.ShortEng().index(inEng[0])
        else:
            ValueError("Can't define month for", month)
