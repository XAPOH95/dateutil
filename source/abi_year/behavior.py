from .abstraction import Abstraction
from .interface import IName

class Behavior(Abstraction, IName):
    def _year(self):
        year = str(self.Year())
        if len(year) > 3:
            return self.Sep() + year[2:]
        return self.Sep() + year

    def Short(self) -> str:
        return self._year()

    def Long(self) -> str:
        return self.Year()

    def __str__(self) -> str:
        return str(self.Year())

    def __repr__(self) -> str:
        return str(self.Year())