class Abstraction:
    """Abstract month"""
    __month:int = None
    def __init__(self, month:int) -> None:
        self.__month = month

    def Month(self):
        return self.__month

class Collection:
    """Collection of names"""
    __short_eng = ('jan', 'feb', "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")
    __short_ru = ('янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')
    __long_ru = ('январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')
    __long_eng = ('january', 'february', "march", "april", "may", "june", "july", "august", "september", "october", "november", "december")

    def ShortEng(self):
        return self.__short_eng

    def ShortRu(self):
        return self.__short_ru

    def LongRu(self):
        return self.__long_ru

    def LongEng(self):
        return self.__long_eng