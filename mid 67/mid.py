# list_total = []
# _dic = {}
# list_1 = []
# while True:
#     item_name = str(input('Enter item name: '))
#     if item_name == 'done':
#         break
#     price = float(input(f'Enter price for {item_name}: '))
#     quantity = int(input(f'Enter quantity of {item_name}: '))
#     price_each = price * quantity
#     list_total.append(price_each)
#     _dic.update({item_name: price})
#
# for name, price in _dic.items():
#     price_each = price * quantity
#     print(f'{name}: {quantity} × {price:.1f} = {price_each:.1f} Baht ')
# sum_total = sum(list_total)
# print(f'Total bill: {sum_total:.1f} Baht')


# can_sizes = [1, 2.5, 5]
# can_prices = [700, 1500, 2600]
#
#
# def read_inputs():
#     width = int(input('Width (m) of paint area? '))
#     length = float(input('Length (m)of paint area?'))
#     return width,length
#
#
# def compute_required_paint(width, length):
#     result = (width*length) / 36
#     return result
#
#
# list_1 = []
# def compute_paint_cans(can_need_, can_size_):
#     for i in can_size_:
#         size_1 =

# i = 0
# list_award = []
# list_all = []
# _dic1 = {}
# _dic2 = {}
# _dic3 = {}
# while True:
#     i = i + 1
#     movie = str(input(f'Movie number #{i}: '))
#     if movie == 'end':
#         break
#     award = int(input('Number of awards for Inception: '))
#     year = int(input('Year of participation: '))
#     list_award.append(award)
#     _dic1.update({year: award})
#     _dic2.update({movie: award})
#     _dic3.update({award: movie})
#
# print()
# print('Choose an option:')
# print('1. Search by year\n2. Search by movie title\n3. Find the movie with the highest total awards\n'
#       '4. Exit')
# while True:
#     choice = int(input('Enter your choice: '))
#     if choice == 1:
#         year_ = int(input('Input the year: '))
#         for year, award in _dic1.items():
#             if year_ == year_:
#                 get_year = _dic1.get(year_)
#         print(f'Top award-winning movie(s) of {year_}:')
#         print(f'Parasite with {_dic1.get(year_)} awards.')
#         print()
#
#     elif choice == 2:
#         name_mo = input('Input the movie title: ')
#         for name, award in _dic2.items():
#             if name_mo == name:
#                 get_name = _dic2.get(name_mo)
#         print(f'{name_mo} has won {_dic2.get(name_mo)} awards in total.')
#         print()
#
#     elif choice == 3:
#         hightes = max(list_award)
#         for name, award in _dic3.items():
#             if hightes == award:
#                 get_hight = _dic3.get(hightes)
#             # print(_dic3.get(hightes))
#         print(f'{_dic3.get(hightes)} has the highest total with {hightes} awards.')
#
#     elif choice == 4:
#         exit()


color_codes = {'r': 'red', 'b': 'blue', 'w': 'white', 'y': 'yellow', 'g': 'green'}

RED_MIX = {'red': 'red', 'blue': 'purple', 'white': 'pink', 'yellow': 'orange', 'green': 'brown'}

BLUE_MIX = {'red': 'purple', 'blue': 'blue', 'yellow': 'green', 'green': 'cyan'}

WHITE_MIX = {'red': 'pink', 'white': 'white', 'yellow': 'bizmuth yellow'}

def get_color_mix(color):
    if color == 'red':
        print(RED_MIX)

    elif color == 'white':
        print(WHITE_MIX)

    elif color == 'blue':
        print(BLUE_MIX)


r = 'red'
b = 'blue'
w = 'white'
# main_color = str(input('ain color (r/b/w)? '))
# if main_color == 'r':
#     print(f'Main color is {r}')
#     for key, valur in RED_MIX.items():
#         print(f'red + {key} = {valur}', end='\n')
# elif main_color == 'b':
#     print(f'Main color is {b}')
#     for key, valur in BLUE_MIX.items():
#         print(f'blue + {key} = {valur}', end='\n')
# elif main_color == 'w':
#     print(f'Main color is {w}')
#     for key, valur in WHITE_MIX.items():
#         print(f'blue + {key} = {valur}', end='\n')


# i = 0
# while True:
#     main_color = str(input('Main color (r/b/w)? '))
#     if main_color == '':
#         print(f'You have asked for main color {i} times.')
#         exit()
#     if main_color == 'r':
#         print(f'Main color is {r}')
#         for key, valur in RED_MIX.items():
#             print(f'red + {key} = {valur}', end='\n')
#         print()
#     elif main_color == 'b':
#         print(f'Main color is {b}')
#         for key, valur in BLUE_MIX.items():
#             print(f'blue + {key} = {valur}', end='\n')
#         print()
#     elif main_color == 'w':
#         print(f'Main color is {w}')
#         for key, valur in WHITE_MIX.items():
#             print(f'blue + {key} = {valur}', end='\n')
#         print()
#     i = i + 1


i = 0
while True:
    main_color = str(input('Main color (r/b/w)? '))
    sc_1 = color_codes.get(main_color)
    print(f'Main color is {sc_1}')
    resulr = get_color_mix(sc_1)
    # print(resulr)
    if main_color == '':
        print(f'You have asked for main color {i} times.')
        exit()
    i = i + 1
    while True:
        color_ = str(input('Second color (r/b/w/y/g/x=exit)? '))
        if color_ == 'x':
            exit()
        elif color_ == 'r':
            sc = color_codes.get(resulr)
            print(sc)
            if sc != sc_1:
                print(f'Second color {sc} is not found.')
            else:
                print(f'{sc_1} + {color_} = {sc}')



