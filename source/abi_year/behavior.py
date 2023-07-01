from .abstraction import Abstraction
from .interface import IName

class Behavior(Abstraction, IName):
    def _year(self):
        year = str(self.Year())
        if len(year) > 3:
            return self.Sep() + year[2:]
        return self.Sep() + year

    def ShortRu(self) -> str:
        return self.Month().short_ru_name() + self._year()

    def ShortEng(self) -> str:
        return self.Month().short_eng_name() + self._year()

    def __str__(self) -> str:
        return self.Month().short_eng_name() + " " + str(self.Year())

    def __repr__(self) -> str:
        return self.Month().short_eng_name() + " " + str(self.Year())