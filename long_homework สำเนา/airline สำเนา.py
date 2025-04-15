# Global list variables
europe = ["England", "Germany", "Italy", "France", "Belgium"]
europe_distance = [9435, 8672, 8705, 9390, 9097]
asia = ["China", "Japan", "Indonesia", "India", "Singapore"]
asia_distance = [3442, 4312, 2333, 4213, 2108]
america = ["USA", "Canada", "Brazil", "Mexico", "Argentina"]
america_distance = [13920, 13280, 16545, 15392, 15640]


# Define your functions here
def get_travel_info():
    # Implement function to get travel information (nested list for multi-destination travel)
    pass
    total = []
    country = int(input('How many destinations?: '))
    for i in range(country):
        i += 1
        destination = input('What is your destination?: ')
        month = input('Departing Month?: ')
        days = int(input('How many days?: '))
        total_list = [destination, month, days]
        total.append(total_list)
    return (total)


def get_passenger_info():
    # Implement function to get passenger information (nested list for passengers and their details)
    pass
    total_passenger = []
    many_passenger = int(input('How many passengers?: '))
    for i in range(many_passenger):
        i += 1
        print(f'Please enter passenger#{i} info')
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        airplane_class = input('Class (Economy/Business): ')
        meal = input('Meal Preference (Veg/Non-Veg): ')
        print('********')
        final_passenger = [first_name, last_name, airplane_class, meal]
        total_passenger.append(final_passenger)
    return (total_passenger)


def check_high_season(month):
    # Implement function to check if the given month is in the high season
    pass
    if month == 'January' or month == 'November' or month == 'December':
        return 1
    else:
        return 0


def get_travel_fee(country):
    # Implement function to calculate travel fee based on country and region
    pass
    if country in europe:
        for i in range(len(country)):
            position = europe.index(country)
            price_new = [price*10 for price in europe_distance]
            return (price_new[position], 'Europe')
    elif country in asia:
        for i in range(len(country)):
            position = asia.index(country)
            price_new = [price*10 for price in asia_distance]
            return (price_new[position], 'Asia')
    elif country in america:
        for i in range(len(country)):
            position = america.index(country)
            price_new = [price*10 for price in america_distance]
            return (price_new[position], 'America')


def get_hotel_fee(num_passengers, period_stay):
    # Implement function to calculate hotel fee based on number of passengers and period of stay
    pass
    price_per_person = num_passengers * 3000
    total_price = price_per_person * period_stay
    return total_price


def calculate_trip_cost():
    # Implement function to calculate the total cost of the trip
    for _destination, _month, _days in a:
        for _first, _last, _class_b, _meal in b:
            _result = check_high_season(month)
            _travel_free = get_travel_fee(destination)
            _final_travel = _travel_free[0]
            if _result == 1:
                if class_b == 'Economy':
                    new_result_t = _final_travel + (_final_travel * 0.2)
                    _total = new_result_t
                    return _total
                elif class_b == 'Business':
                    new_result_t_1 = _final_travel + (_final_travel * 0.2)
                    new_result_t = new_result_t_1 + (new_result_t_1 * 0.5)
                    _total = new_result_t
                    return _total
            else:
                if class_b == 'Economy':
                    _total = _final_travel
                    return _total

                elif class_b == 'Business':
                    _total = (_final_travel + (_final_travel * 0.5))
                    return _total
            continue


# Call your functions and implement the main program flow below


a = get_travel_info()
b = get_passenger_info()

all_free1 = []
for destination, month, days in a:
    all_free_tav = []
    for first, last, class_b, meal in b:
        total = calculate_trip_cost()
        all_free_tav.append(total)
        sum_tav = sum(all_free_tav)
        travel_free = get_travel_fee(destination)
        group = travel_free[1]
        print(f'Passenger Name: {first} {last}')
        print(f'From Bangkok to {destination} ({group})')
        print(f'Traveling fee: {total:.2f} Baht ({class_b})')
        print(f'Meal: {meal}')
        print('********')
    # print(all_free_tav)
    room = len(b)
    hotel_free = get_hotel_fee(room, days)
    all_free = sum_tav + hotel_free
    # print(all_free)
    all_free1.append(all_free)
    # print(all_free1)
    sum_total = sum(all_free1)
    print(f'Hotel fee for {room} rooms x {days} nights is {hotel_free:.2f} Baht')
    print('########################################')
print(f'The total cost is {sum_total:.2f} Baht')
print('Enjoy your trip :)')
