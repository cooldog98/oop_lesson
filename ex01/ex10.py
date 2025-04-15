import json


class MyTmp:
    _instance = None

    def __new__(cls, para):
        return super().__new__(cls)

    def __init__(self, dbname=None):
        self.__db_name = dbname
        self.__db = None

    def loadDB(self):
        # file = open(self.__db_name, 'r')
        # self.__db = json.load(file)

        with open(self.__db_name, 'r') as file:
            self.__db = json.load(file)

    def modifyDB(self, tablename, date):
        self.__db[tablename].append(date)

    def getDB(self):
        return self.__db

    def saveDB(self):
        with open(self.__db_name, 'w') as file:
            json.dump(self.__db, file)



a = MyTmp('hello.json')
b = MyTmp('hello.json')
b.loadDB()
a.loadDB()
a.modifyDB("table1", {'col1': 11, 'col2': 22})
a.modifyDB("table1", {'col1': 'Mr.white', 'col2': 'Apple'})
a.modifyDB("table1", {'col1': 'Mr.Black', 'col2': 'Banana'})
print(a.getDB())
a.saveDB()
b.modifyDB("table1", {'col1': 11, 'col2': 22})
b.modifyDB("table1", {'col1': 'Mr.white', 'col2': 'Apple'})
b.modifyDB("table1", {'col1': 'Mr.Black', 'col2': 'Banana'})
b.saveDB()
