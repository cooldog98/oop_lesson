import random


class NextFibo():
    def __init__(self):
        self.__index = 0
        self.__history = {}

    def __iter__(self):
        return self

    def __fibo(self, i):
        if i in self.__history:
            return self.__history[i]  #make code run faster

        if i == 0:
            return 0
        if i == 1:
            return 1
        return self.__fibo(i-1) + self.__fibo(i-2)

    def __next__(self):

        value = self.__fibo(self.__index)
        self.__history[self.__index] = value

        self.__index = self.__index+1
        return value


b = NextFibo()

for i in range(100):
    print(i, next(b))

