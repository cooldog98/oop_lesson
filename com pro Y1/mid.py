planets = ['mercury', 'venus', 'earth']
items = ['mass', 'density', 'diameter', 'gravity']
data = [
    [0.33, 4.87, 5.97],
    [5429, 5243, 5514],
    [4879, 12104, 12756],
    [3.7, 8.9, 9.8]
]


def find_index(x, ind):
    for i in range(len(x)):
        if x[i] == ind:
            return i
    return -99


choice = input("Extract item or planet(i/p/Q): ")
k = ''
d ={}
while(choice != 'Q'):
    if choice == 'i':
        item = input("Enter item: ")
        j = 1
        while not(item in items):
            j = 0
            print("Invalid item.")
            k = data[find_index(items, item)]
            print(k)
        for i in range(len(k)):
            d[planets[i]] = k[i]
        if j:
            print(d)
    if choice == 'p':
        planet = input("Enter planet: ")