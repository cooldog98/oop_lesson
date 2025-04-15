import random


class Prime():
    def __init__(self):
        self.__index = 0
        self.__history = {}


    def __iter__(self):
        return self

    def __chk_p(self, i):
        # if i in self.__history:
        #     return self.__history[i]  #make code run faster

        j = i - 1
        while j > 1:
            if i % j == 0:
                return False
            j -= 1
            # print(i, j)
        return True

    def __next__(self):
        result = False
        while result == False:
            result = self.__chk_p(self.__index)
            self.__index += 1
        return self.__index, result


b = Prime()

i = 0
# print(i, next(b))
# print(i, next(b))
# print(i, next(b))

for i in range(100):
    print(i, next(b))

