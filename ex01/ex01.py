"""
Singlenton Pattern
"""

class MySinglenton:
    _instance = None

    def __init__(self, v):
        if MySinglenton._instance == None:
            self.a = v
            MySinglenton._instance = self
        # else:
        #     return ValueError{"Not allow"}

    @classmethod
    def getInstance(cls):
        return cls._instance


tmp = MySinglenton(5)
print(tmp)
print(id(tmp))# get address
print(tmp.a)

print('--------------')

tmp2 = MySinglenton.getInstance()
print(tmp2)
print(id(tmp2)) # get address
print(tmp2.a)

tmp3 = MySinglenton(10)
print(tmp3)
print(id(tmp3))
print(tmp3.a)

print('--------------')

tmp4 = MySinglenton.getInstance()
print(tmp4)
print(id(tmp4)) # get address
print(tmp.a)
print('--------------')
