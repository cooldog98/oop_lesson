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

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print all cities in Italy
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(city['city'])
print("All the cities in", my_country, ":")
print(temps)
print()

# Print the average temperature for all the cities in Italy
# Write code for me
print("The average temperature of all the Italy:")
city_temp = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        city_temp.append(float(city['temperature']))
print(sum(city_temp)/len(city_temp))
print()


# Print the max temperature for all the cities in Italy
# Write code for me
max_temps = []
my_country = 'Italy'
print("The max temperature of all the cities in Italy:")
for city in cities:
    if city['country'] == my_country:
        max_temps.append(float(city['temperature']))
print(max(max_temps))
print()

# Print the max temperature for all the cities in Italy
# Write code for me
min_temp = []
my_country = 'Italy'
print("The min temperature of all the cities in Italy:")
for city in cities:
    if city['country'] == my_country:
        min_temp.append(float(city['temperature']))
print(min(min_temp))
print()


# Let's write a function to filter out only items that meet the condition
def filter(condition, dict_list):
    pass
    _list = []
    for item in dict_list:
        if condition(item):
            _list.append(item)
    return _list
# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    pass
    _list = []
    for i in dict_list:
        if aggregation_function(i):
            _list.append(float(i[aggregation_key]))
    return _list
# Let's write code to
# - print the average temperature for all the cities in Italy


avg_italy = aggregate('temperature', lambda x: x['country'] == 'Italy', cities)
print(f'the average temperature for all the cities in Italy is {sum(avg_italy)/len(avg_italy)}')
print()
# - print the average temperature for all the cities in Sweden


avg_swe = aggregate('temperature', lambda x: x['country'] == 'Sweden', cities)
print(f'the average temperature for all the cities in Sweden is {sum(avg_swe)/len(avg_swe)}')
print()

#min,max

# - print the min temperature for all the cities in Italy


min_italy = aggregate('temperature', lambda x: x['country'] == 'Italy', cities)
print(f'The min temperature for all the cities in Italy is {min(min_italy)}')
print()
# - print the max temperature for all the cities in Sweden

max_swe = aggregate('temperature', lambda x: x['country'] == 'Italy', cities)
print(f'The min temperature for all the cities in Italy is {max(min_italy)}')