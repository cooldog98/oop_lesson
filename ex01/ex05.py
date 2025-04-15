class Parent:
    pass




class MySinglenton():
    _instance = None
    def __new__(cls, v=None):
        if cls._instance == None:
            print('new')
            cls._instance = super().__new__(cls) ##### important

        return cls._instance

    def __init__(self, b=None):
        if b is not None:
            self.k = b
        print('init')
        print('k', self.k)


a = MySinglenton('hello')
print(type(a))
print(id(a))

print('---------------------------')

a1 = MySinglenton('world')
print(type(a1))
print(id(a1))
# print(isinstance(a, MySinglenton))
# print(isinstance(a, Parent))
# print(isinstance(a, int))
