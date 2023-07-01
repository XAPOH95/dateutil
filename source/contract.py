class CShortRepresentation:
    """Contract for short representation"""
    def Ru(self):
        raise NotImplementedError

    def Eng(self):
        raise NotImplementedError

class CIndexRepresentation:
    """Contract for index-like representation"""
    def M(self):
        raise NotImplementedError

    def index(self):
        raise NotImplementedError

class CLongRepresentation:
    """Contract for long representation"""
    def RuFull(self):
        raise NotImplementedError
    
    def EngFull(self):
        raise NotImplementedError

class CComparision:
    """Contract for ability to compare itself with other"""
    def __eq__(self, __o) -> bool:
        raise NotImplementedError

    def __lt__(self, __o) -> bool:
        raise NotImplementedError

    def __gt__(self, __o) -> bool:
        raise NotImplementedError

    def __le__(self, __o) -> bool:
        raise NotImplementedError

    def __ge__(self, __o) -> bool:
        raise NotImplementedError

class COffset:
    """Contract for ability to offset itself by given number"""
    def __sub__(self, offset:int):
        raise NotImplementedError

    def __add__(self, offset:int):
        raise NotImplementedError

    def __int__(self):
        raise NotImplementedError