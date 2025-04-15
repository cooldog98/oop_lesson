import random

a = [4, 'asd', True, 5.6]
print(type(a)) #<class 'tuple'>
print(dir(a)) #['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
#
c = iter(a)
print(type(c))
print(dir(c))

# print(vars(a)) #error


class Mylist():
    def __init__(self, data):
        self.__data = data
        self.__index = 0
        self.__index2 = len(self.__data) - 1

    def __iter__(self):
        return self

    # @staticmethod
    def __process(a=None, b=None):
        print('hello')

    def __next__(self):
        if self.__index < len(self.__data):
            value = self.__data[self.__index]
            value2 = self.__data[self.__index2]
            self.__index += 1
            self.__index2 -= 1
            self.__process()
            return (value, value2)
        raise StopIteration
        # return 'hello ====' + str(self.__index)
        # return super().__next__(self)


r = []
for i in range(11):
    r.append(random.randint(100, 200))
# b = Mylist([4, 'asd', True, 5.6])
# print(b)

b = Mylist(r)

# print(r)
#
# print(next(b))
# print(next(b))
# print(next(b))
# for i in b:
#     print(i)
