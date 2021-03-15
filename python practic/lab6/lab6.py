from abc import ABCMeta, abstractmethod, abstractproperty


class abcClass(metaclass=ABCMeta):
    def __init__(self, x=0):
        self.__x = x

    @abstractmethod
    def getX(self):
        return self.__x


class abcClass2(abcClass):
    def getX(self):
        return super().getX()


a = abcClass2(5)
print(a.getX())
