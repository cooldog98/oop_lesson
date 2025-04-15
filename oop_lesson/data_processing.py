import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))


class TableDB:
    def __init__(self):
        self.table_db = []

    def insert(self, table):
        index_ = self.search(table)
        if index_ == -1:
            self.table_db.append(table)

    def search(self, table_name):
        for i in self.table_db:
            if i == table_name:
                return i
        return -1


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        _list = []
        for i in self.table:
            if condition(i):
                _list.append(i)
        return _list

    def aggregate(self, aggregation_key, aggregation_function):
        _list = []
        for i in self.table:
            value = float(i[aggregation_key])
            _list.append(value)
        return aggregation_function(_list)

    def __str__(self):
        return f'{self.table_name}: {str(self.table)}'


cities_table = Table('cities', cities)
country_table = Table('countries', countries)
table_db = TableDB()
table_db.insert(cities_table)
table_db.insert(country_table)

filter_italy = cities_table.filter(lambda x: x["country"] == 'Italy')
filter_swe = cities_table.filter(lambda x: x["country"] == 'Sweden')

cities_italy = Table('italy_country', filter_italy)
cities_swe = Table('sweden_country', filter_swe)

table_db.insert(cities_italy)
table_db.insert(cities_swe)

print('The average temperature for all the cities in Italy')
print(cities_italy.aggregate('temperature', lambda x: sum(x)/len(x)))

print('The average temperature for all the cities in Sweden')
print(cities_swe.aggregate('temperature', lambda x: sum(x)/len(x)))

print('The min temperature for all the cities in Italy')
print(cities_italy.aggregate('temperature', lambda x: min(x)))

print('The max temperature for all the cities in Sweden')
print(cities_swe.aggregate('temperature', lambda x: max(x)))

print('The min longitude for all cities')
print(cities_table.aggregate('longitude', lambda x: min(x)))

print('The max longitude for all cities')
print(cities_table.aggregate('longitude', lambda x: max(x)))

print('The min latitude for all cities')
print(cities_table.aggregate('latitude', lambda x: min(x)))

print('The max latitude for all cities')
print(cities_table.aggregate('latitude', lambda x: max(x)))

print('The min population for all counties')
print(country_table.aggregate('population', lambda x: min(x)))

print('The max population for all counties')
print(country_table.aggregate('population', lambda x: max(x)))
