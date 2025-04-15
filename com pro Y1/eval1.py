# 1 kg of weight need 7,700 calories burned
# run 10 km burn 600 calories.  1 km burn 60 cal
'''import math
def lose_weight():
    weight = float(input("Input weight you want to lose (kg.): "))
    run_per_day = float(input("Input distance you run per day (km): "))
    wantlose = weight * 7700
    run = wantlose / 60
    total_day = math.ceil( run/run_per_day)
    print(f'You should run {run:.2f} kilometers to lose {weight:.2f} kilograms.')
    print(f'You will spend {total_day} days for running.')
lose_weight()'''


# LITERTOOUNCES = 33.814
#
#
# def calculate_total_volume(number_of_guests, glass_volume):
#     volume = number_of_guests * glass_volume
#     return volume
#
#
# def find_exact_num_bottles(total_volume):
#     soda = total_volume / LITERTOOUNCES
#     return soda
#
# import math
# number_of_guests = int(input("Enter number of guests: "))
# glass_volume = float(input("Enter glass volume: "))
# volume = calculate_total_volume(number_of_guests, glass_volume)
# num_soda = find_exact_num_bottles(volume)
# soda_final = math.ceil(num_soda)
# print(f"It's exactly required {num_soda:.2f} 2-liter bottles of soda.")
# print(f"Hence, you must purchase at least {soda_final} 2-liter bottles.")

# def get_circle_area(radius):
#     import math
#     area = math.pi * radius**2
#     return area
#
#
# def get_ring_area(outer_radius, inner_radius):
#     import math
#     area_circle = get_circle_area(outer_radius)
#     area_ring = math.pi * inner_radius**2
#     total_area = area_circle - area_ring
#     return total_area
#
# out_r = float(input("Input outer radius: "))
# inner_r = float(input("Input inner radius: "))
# ring = get_ring_area(out_r, inner_r)
# print(f'The area of the ring is {ring:.3f} sq.m.')

# def compute_sphere_volume(radius):
#     import math
#     volume = (4/3) * math.pi * radius**3
#     return volume
#
#
# def compute_sphere_surface_area(radius):
#     import math
#     surface = 4 * math.pi * radius**2
#     return surface
#
# radius = float(input("Enter sphere radius: "))
# volume = compute_sphere_volume(radius)
# surface = compute_sphere_surface_area(radius)
# print(f'The volume of sphere is {volume:.2f}.')
# print(f'The surface area of this sphere is {surface:.2f}.')

# REGULAR_PRICE = 150
# SENIOR_PRICE = 25
# KID_PRICE = 100
#
#
# def read_guests():
#     total_guests = int(input('Enter #guests in total: '))
#     seniors = int(input('Enter #seniors: '))
#     kids = int(input('Enter #children: '))
#     return total_guests, seniors, kids
#
#
# def calculate_price(num_items=0, price_per_item=0):
#     price = num_items * price_per_item
#     return price
#
#
# def calculate_total_ticket_price(num_total_guest=1, seniors=0, kids=0):
#     regular = num_total_guest - (seniors + kids)
#     price_regular = regular * REGULAR_PRICE
#     price_senior = seniors * SENIOR_PRICE
#     price_kid = kids * KID_PRICE
#     total = price_regular + price_senior + price_kid
#     return total
#
#
# def show_ticket_summary(num_total_guest, seniors, kids):
#     regular = num_total_guest - (seniors + kids)
#     price_regular = regular * REGULAR_PRICE
#     price_senior = seniors * SENIOR_PRICE
#     price_kid = kids * KID_PRICE
#     print('Ticket Summary:')
#     print(f'{seniors} senior tickets cost {price_senior:.2f} Baht.')
#     print(f'{kids} children tickets cost {price_kid:.2f} Baht.')
#     print(f'{regular} general tickets cost {price_regular:.2f} Baht.')
#
# num_total_guest, seniors, kids = read_guests()
# show_ticket_summary(num_total_guest, seniors, kids)
# total = calculate_total_ticket_price(num_total_guest, seniors, kids)
# print(f'Total tickets cost {total:.2f} Baht.')


REGULAR_PRICE = 150
SENIOR_PRICE = 25
KID_PRICE = 100
IMAX_PRICE = 100
DRINK_PRICE = 25


def read_guests():
    total_guests = int(input('Enter #guests in total: '))
    seniors = int(input('Enter #seniors: '))
    kids = int(input('Enter #children: '))
    return total_guests, seniors, kids


def read_services():
    imax = int(input('Enter #IMAX tickets: '))
    drink = int(input('Enter #drink vouchers: '))
    return imax, drink


def calculate_price(num_items=0, price_per_item=0):
    price = num_items * price_per_item
    return price


def calculate_total_ticket_price(num_total_guest=1, seniors=0, kids=0):
    regular = num_total_guest - (seniors + kids)
    price_regular = regular * REGULAR_PRICE
    price_senior = seniors * SENIOR_PRICE
    price_kid = kids * KID_PRICE
    total = price_regular + price_senior + price_kid
    return total


def show_ticket_summary(num_total_guest, seniors, kids):
    regular = num_total_guest - (seniors + kids)
    price_regular = regular * REGULAR_PRICE
    price_senior = seniors * SENIOR_PRICE
    price_kid = kids * KID_PRICE
    print('Ticket Summary:')
    print(f'{seniors} senior tickets cost {price_senior:.2f} Baht.')
    print(f'{kids} children tickets cost {price_kid:.2f} Baht.')
    print(f'{regular} general tickets cost {price_regular:.2f} Baht.')


def get_purchase_summary_str(total_ticket_price, num_imax, num_drink):
    imax1 = num_imax * IMAX_PRICE
    drink1 = num_drink * DRINK_PRICE
    total_ticket_price = calculate_total_ticket_price(num_total_guest, seniors, kids)
    total_payment = (num_imax * 100) + (num_drink * 25) + total_ticket_price
    return (f'Purchase Summary:\nTotal tickets cost {total_ticket_price:.2f} Baht.\nTotal IMAX tickets cost {imax1:.2f} Baht.'
            f'\nTotal drink vouchers cost {drink1:.2f} Baht.\nTotal payment cost {total_payment:.2f} Baht.')

num_total_guest, seniors, kids = read_guests()
imax, drink = read_services()
show_ticket_summary(num_total_guest, seniors, kids)
total_ticket_price = calculate_total_ticket_price(num_total_guest, seniors, kids)
ps = get_purchase_summary_str(total_ticket_price, imax, drink)
print(ps)
