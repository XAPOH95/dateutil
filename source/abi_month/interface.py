class IName:
    def full_ru_name(self) -> str:
        raise NotImplementedError

    def full_eng_name(self) -> str:
        raise NotImplementedError

    def short_ru_name(self) -> str:
        raise NotImplementedError

    def short_eng_name(self) -> str:
        raise NotImplementedError

class Iindex:
    def index(self) -> int:
        """return index of month, where 1 - january, 2 - february. 0 and 12 is december"""
        raise NotImplementedError

    def mIndex(self) -> str:
        """return index of month eg, M00, M01, M12"""
        raise NotImplementedError

class IConstructor:
    def construct_month(self):
        raise NotImplementedError