LAST_RESERVED_DATE = 25
MIN_DURATION = 2
MAX_DURATION = 4


def read_int_input(input_name, scope):
    """ Read the user's input, where it is an integer referred as input_name,
        and evaluate the input.
        The valid input is considered to be an integer that falls inclusively within the given scope.
        If the user enters an input out of scope,
            the function will continue asking the user to enter a valid input.
        When the user enters an input within the scope,
            the function will stop prompting and return this valid input.

        HINT: list operation in may be useful to help with input validation

        :param input_name: name of the input
        :param scope: list of valid integers within the scope
        :return: valid input
    """
    while True:
        input_m = int(input('Enter month: '))
        if input_m in scope:
            break
        else:
            print('month is out of range.')
            continue
    # return input_m

    while True:
        input_d = int(input('Enter date: '))
        if 0 < input_d <= 25:
            break
        else:
            print('date is out of range.')
            continue
    # return input_d

    while True:
        input_dt = int(input('Enter duration: '))
        if 2 <= input_dt <= 4:
            break
        else:
            print('duration is out of range.')
            continue

    return input_d, input_m, input_dt


def find_available_parks(_openings, _month):
    """ Find the available parks that are open during the given month.
        Return a list of available park names.

        :param _openings: list of park-opening months
        :param _month: int
        :return: list of available park names open during the given month
        >>> find_available_parks({'Phi Phi': [1,2,11,12], 'Similan': [10,11,12]}, 12)
        ['Phi Phi', 'Similan']
        >>> find_available_parks({'Phi Phi': [1,2,11,12], 'Similan': [10,11,12]}, 10)
        ['Similan']
        >>> find_available_parks({'Phi Phi': [1,2,11,12], 'Similan': [10,11,12]}, 2)
        ['Phi Phi']
    """
    _list_park = []
    for place, _list in _openings.items():
        # print(_list)
        if _month in _list:
            _list_park.append(place)
        else:
            continue
    return _list_park


def get_reserve_info(_reserves, status="Guest"):
    """ From park reservations (_reserves), return a string containing all reservation information.
        For any park with reservation(s),
            Add a string containing the reservation information.
            If the status of user is "Admin", include guest name and payment status in the string.
        For any park with no reservation, skip adding string.
        Continue adding strings for all park reservations.
        Return the string containing all reservation information.

        :param _reserves: park reservations
        :param status: string value of the user status
        :return: string containing all reservation information
        >>> reserve_info = get_reserve_info({'Erawan': [{'name': 'Ron', 'month': 10, 'date': 25, \
                                                        'duration': 2, 'status': 'paid'}], \
                                            'Phi Phi': [], \
                                            'Similan': [{'name': 'Sam', 'month': 12, 'date': 15, \
                                                        'duration': 3, 'status': 'paid'}, \
                                                        {'name': 'Tony', 'month': 11, 'date': 8, \
                                                        'duration': 4, 'status': 'reserved'}]})
        >>> print(reserve_info)
        @Erawan Reservations
        25/10-26/10, 2 days
        @Similan Reservations
        15/12-17/12, 3 days
        8/11-11/11, 4 days
        <BLANKLINE>
    """
    result_info = ''
    for park, information in _reserves.items():
        if information:
            result_info += f'@{park} Reservations\n'
            if status == 'Guest':
                for i in information:
                    _month = i.get('month')
                    _first_day = i.get('date')
                    _dt = i.get('duration')
                    _last_day = (_first_day + _dt) - 1
                    result_info += f'{_first_day}/{_month}-{_last_day}/{_month}, {_dt} days\n'
            if status == 'Admin':
                for i in information:
                    _name = i.get('name')
                    _month = i.get('month')
                    _first_day = i.get('date')
                    _dt = i.get('duration')
                    _pay = i.get('status')
                    _last_day = (_first_day + _dt) - 1
                    result_info += f'{_first_day}/{_month}-{_last_day}/{_month}, {_dt} days: {_name}, {_pay}\n'
    result_info += ''
    return result_info


def check_availability(_reserves, _park_name, _month, _date, _duration):
    """ Check for the availability of park residents from park reservation (_reserves).
            at the given _park_name on a given _date and _month for the given _duration.
        If there is availability, return True.  Otherwise, return False.

        NOTE: The ending date of one reservation and the starting date of the other reservation can be the same date.

        HINT: If the new reservation has the starting date X and the ending date Y,
                the new reservation is considered available if the range from X to Y
                    does not fully overlap or does not partially overlap with the existing reservations.

        :param _reserves: park reservations
        :param _park_name: string
        :param _month: int
        :param _date: int
        :param _duration: int
        :return: True if park resident is available, else False.
        >>> check_availability({'Phi Phi': [], \
                                'Similan': [{'name': 'A', 'month': 1, 'date': 5, 'duration': 3, 'status': 'reserved'}, \
                                           {'name': 'B', 'month': 2, 'date': 10, 'duration': 2, 'status': 'paid'}]}, \
                                'Phi Phi', 1, 5, 3)
        True
        >>> check_availability({'Phi Phi': [], \
                                'Similan': [{'name': 'A', 'month': 1, 'date': 5, 'duration': 3, 'status': 'reserved'}, \
                                           {'name': 'B', 'month': 1, 'date': 10, 'duration': 2, 'status': 'paid'}]}, \
                                'Similan', 2, 5, 3)
        True
        >>> check_availability({'Phi Phi': [], \
                                'Similan': [{'name': 'A', 'month': 1, 'date': 5, 'duration': 3, 'status': 'paid'}]}, \
                                'Similan', 1, 8, 3)
        True
        >>> check_availability({'Phi Phi': [], \
                                'Similan': [{'name': 'A', 'month': 1, 'date': 5, 'duration': 3, 'status': 'paid'}]}, \
                                'Similan', 1, 7, 3)
        True
        >>> check_availability({'Phi Phi': [], \
                                'Similan': [{'name': 'A', 'month': 1, 'date': 5, 'duration': 3, 'status': 'paid'}]}, \
                                'Similan', 1, 6, 3)
        False
        >>> check_availability({'Phi Phi': [], \
                                'Similan': [{'name': 'A', 'month': 1, 'date': 5, 'duration': 3, 'status': 'paid'}]}, \
                                'Similan', 1, 4, 3)
        False
        >>> check_availability({'Phi Phi': [], \
                                'Similan': [{'name': 'A', 'month': 1, 'date': 5, 'duration': 3, 'status': 'paid'}]}, \
                                'Similan', 1, 3, 3)
        True
        >>> check_availability({'Phi Phi': [], \
                                'Similan': [{'name': '', 'month': 1, 'date': 5, 'duration': 3, 'status': 'paid'}]}, \
                                'Similan', 1, 4, 2)
        True
        >>> check_availability({'Phi Phi': [], \
                                'Similan': [{'name': 'A', 'month': 1, 'date': 5, 'duration': 3, 'status': 'paid'}, \
                                           {'name': 'B', 'month': 1, 'date': 8, 'duration': 3, 'status': 'paid'}]}, \
                                'Similan', 1, 7, 3)
        False
        >>> check_availability({'Phi Phi': [], \
                                'Similan': [{'name': 'A', 'month': 1, 'date': 5, 'duration': 3, 'status': 'paid'}, \
                                           {'name': 'B', 'month': 1, 'date': 8, 'duration': 3, 'status': 'paid'}]}, \
                                'Similan', 1, 7, 2)
        True
        >>> check_availability({'Phi Phi': [], \
                                'Similan': [{'name': 'A', 'month': 1, 'date': 5, 'duration': 3, 'status': 'paid'}, \
                                           {'name': 'B', 'month': 1, 'date': 7, 'duration': 3, 'status': 'paid'}]}, \
                                'Similan', 1, 7, 2)
        False
    """
    result = True
    _list_re = []
    _list_want = []
    for park, info in _reserves.items():
        if _park_name == park:
            for i in info:
                _month1 = i.get('month')
                _date1 = i.get('date')
                _duration1 = i.get('duration')
                _last_date1 = _date1 + _duration1 - 1
                if _month == _month1:
                    for day_re in range(_date1 + 1, _last_date1):
                        _list_re.append(day_re)
                    for day_want in range(_date, _date + _duration):
                        _list_want.append(day_want)
                    for ch_day in _list_want:
                        if ch_day in _list_re:
                            result = False

    return result


def make_reservation(_reserves, _openings):
    """ Read the park name, month, date, and duration of the new reservation from the user.
        Make sure that the park name, month, date, and duration are valid.
        Then, check the availability of the new reservation,
            based on the given park reservations (_reserves) and park openings (_openings).
        If the reservation is available, add the new reservation to park reservations (_reserves).
            Note that the added reservation has its payment status set to "reserved".
        If the reservation is not available, notify the user.

        :param _reserves: park reservations
        :param _openings: park openings
        :return: Nothing
    """
    _reserves1 = _reserves
    while True:
        park = str(input('Enter park: '))
        if park in park_openings.keys():
            _list_m = park_openings.get(park)
            print(f'Available months: {_list_m}')
            break
        else:
            print(f'{park} does not exist.')
            continue
    # print(_list_m)
    input_d, input_m, input_dt = read_int_input(_reserves1, _list_m)
    # print(input_m)
    # list_ = []
    dic_ = {}
    guest_name = input('Enter guest name: ')
    last_day = (input_d + input_dt) - 1
    night = input_dt - 1
    dic_['name'] = guest_name
    dic_['month'] = input_m
    dic_['date'] = input_d
    dic_['duration'] = input_dt
    dic_['status'] = 'reserves'
    # list_.append(dic_)
    check = check_availability(_reserves=park_reserves, _park_name=_reserves1, _month=input_m, _date=input_d,
                               _duration=input_dt)
    if check == 'True':
        new_info = _reserves[park]
        new_info.append(dic_)
        result = (f'Your reservation @{park}: {input_d}/{input_m}-{last_day}/{input_m} '
                  f'for {input_dt} days, {night} nights.')
        print(result)
    elif check == 'False':
        print('The reservation is not available.')
    else:
        new_info = _reserves1[park]
        new_info.append(dic_)
        result = (f'Your reservation @{park}: {input_d}/{input_m}-{last_day}/{input_m} '
                  f'for {input_dt} days, {night} nights.')
        print(result)


def search_reservation(_reserves, _park_name, _guest_name):
    """ In park reservations (_reserves),
            search for the reservation dictionary of the given _park_name and _guest_name.
        If such reservation is not found, return None.
        Otherwise, return the reservation dictionary of the given _park_name and _guest_name

        :param _reserves: park reservations
        :param _park_name: string
        :param _guest_name: string
        :return: dictionary of the reservation, owned by _guest_name
        >>> search_reservation({'Phi Phi': [], \
                                'Similan': [{'name': 'A', 'month': 1, 'date': 5, 'duration': 3, 'status': 'reserved'}, \
                                            {'name': 'B', 'month': 1, 'date': 10, 'duration': 2, 'status': 'paid'}]}, \
                                'Phi Phi', 'A')

        >>> search_reservation({'Phi Phi': [], \
                                'Similan': [{'name': 'A', 'month': 1, 'date': 5, 'duration': 3, 'status': 'reserved'}, \
                                            {'name': 'B', 'month': 1, 'date': 10, 'duration': 2, 'status': 'paid'}]}, \
                                'Similan', 'C')

        >>> search_reservation({'Phi Phi': [], \
                                'Similan': [{'name': 'A', 'month': 1, 'date': 5, 'duration': 3, 'status': 'reserved'}, \
                                            {'name': 'B', 'month': 1, 'date': 10, 'duration': 2, 'status': 'paid'}]}, \
                                'Similan', 'A')
        {'name': 'A', 'month': 1, 'date': 5, 'duration': 3, 'status': 'reserved'}
        >>> search_reservation({'Phi Phi': [], \
                                'Similan': [{'name': 'A', 'month': 1, 'date': 5, 'duration': 3, 'status': 'reserved'}, \
                                            {'name': 'B', 'month': 1, 'date': 10, 'duration': 2, 'status': 'paid'}]}, \
                                'Similan', 'B')
        {'name': 'B', 'month': 1, 'date': 10, 'duration': 2, 'status': 'paid'}
    """
    for park, info in _reserves.items():
        if _park_name == park:
            info = _reserves.get(_park_name)
            for i in info:
                name = i.get('name')
                if _guest_name == name:
                    result = _reserves.get(_park_name)
                    for j in result:
                        name_j = j.get('name')
                        if _guest_name == name_j:
                            return j


def compute_payment(_fees, _park_name, _num_nights, _num_adults, _num_children):
    """ Based on the given park fees (_fees), compute four types of payments that the user must pay.
        1. Resident fee: The park-resident rental fee that the user must pay.
            This is the product of the rental fee per night and the number of nights from the reservation.
        2. Adult ticket fee: The park admission fee for all adult guests.
            Each adult guest needs to pay the admission fee once per reservation, NOT per day.
            Assume that each guest enters the park once per reservation.
            Adult ticket fee is the admission fee for all adult guests.
        3. Children ticket fee: The park admission fee for all children guests.
            Each child guest needs to pay the admission fee once per reservation, NOT per day.
            Children ticket fee is the admission fee for all children guests.
        4. Total fee: The sum of the resident fee, the adult ticket fee, and the children ticket fee.

        :param _fees: park fees
        :param _park_name: string
        :param _num_nights: int
        :param _num_adults: int
        :param _num_children: int
        :return: 4 values: resident fee, adult ticket fee, children ticket fee, total fee
        >>> compute_payment({'Phi Phi': [20, 40, 1500, 2], 'Similan': [50, 100, 2000, 2]}, 'Phi Phi', 1, 1, 1)
        (1500, 40, 20, 1560)
        >>> compute_payment({'Phi Phi': [20, 40, 1500, 2], 'Similan': [50, 100, 2000, 2]}, 'Phi Phi', 2, 2, 0)
        (3000, 80, 0, 3080)
        >>> compute_payment({'Phi Phi': [20, 40, 1500, 2], 'Similan': [50, 100, 2000, 2]}, 'Similan', 2, 1, 1)
        (4000, 100, 50, 4150)
        >>> compute_payment({'Phi Phi': [20, 40, 1500, 2], 'Similan': [50, 100, 2000, 2]}, 'Similan', 1, 2, 0)
        (2000, 200, 0, 2200)
    """
    for park, free in park_fees.items():
        if _park_name == park:
            free_park = park_fees.get(_park_name)
            for i in free_park:
                re_free = free_park[2]
                ch_free = free_park[0]
                ch_free_final = ch_free * _num_children
                ad_free = free_park[1]
                ad_free_final = ad_free * _num_adults
                re_free_fi = re_free * _num_nights
                total = (re_free_fi + ch_free_final + ad_free_final)
                return re_free_fi, ad_free_final, ch_free_final, total


def make_payment(_reserves, _fees):
    """ Read the user's input for the park name and guest name.
        Use the park name and guest name to search for the corresponding park reservations (_reserves)
        If the reservation is not found, notify the user.
        If the reservation is found, display reservation information and
            If its payment status is 'paid', notify the user.
            If its payment status is 'reserved', then
                Ask the user for the number of adult and children guests, where
                    The total number of adult and children guests cannot exceed
                        the maximum number of guests can stay at the park resident.
                    If it exceeds the maximum, ask the user to re-enter the valid number of adult and children guests.
                Next, compute and report the 4 types of payments that the user must pay.
                Last, update the payment status of this reservation to 'paid'.

        :param _reserves: park reservations
        :param _fees: park fees
        :return: Nothing
    """
    result = False
    while True:
        _park = str(input('Enter park: '))
        if _park in park_openings.keys():
            _name = input('Enter guest name: ')
            break
        else:
            print(f'{_park} does not exist.')
            continue

    for park, info in _reserves.items():
        if _reserves.get(park) == []:
            print('Your reservation is not found.')
            break
        if _park == park:
            for i in info:
                _name_i = i.get('name')
                _day = i.get('date')
                _month = i.get('month')
                _duration = i.get('duration')
                _night = _duration - 1
                if _name_i != _name:
                    continue
                if _name_i == _name:
                    result = True
                    if i.get('status') == 'paid':
                        print(f'Your reservation: {_day}/{_month} for {_duration} days, {_night} nights.')
                        print('Your reservation is already paid.')
                    elif i.get('status') == 'reserved':
                        for park, free in _fees.items():
                            if _park == park:
                                k = _fees.get(_park)
                                _c = k[0]
                                _a = k[1]
                                _r = k[2]
                                max_people = k[3]
                                print(f'Maximum of {max_people} guests can stay at the park resident.')
                                while True:
                                    _adult = int(input('Enter #adult guests: '))
                                    _child = int(input('Enter #children guests: '))
                                    total_people = _adult + _child
                                    if total_people > max_people:
                                        print('Total number of guests exceeds the limit.')
                                        continue
                                    elif 0 < total_people <= max_people:
                                        print(f'Your reservation: {_day}/{_month} for {_duration} days,'
                                              f' {_night} nights.')
                                        re_free_fi, ad_free_final, ch_free_final, total = (
                                            compute_payment(_fees=park_fees, _park_name=_park, _num_nights=_night,
                                                            _num_adults=_adult, _num_children=_child))
                                        print(f'Resident rental fee is {re_free_fi} Baht. '
                                              f'({_r} Baht per night)')
                                        print(f'Adult ticket fee is {ad_free_final} Baht. '
                                              f'({_a} Baht per adult)')
                                        print(f'Children ticket fee is {ch_free_final} Baht.'
                                              f' ({_c} Baht per child)')
                                        print(f'Total payment is {total} Baht.')
                                        i['status'] = 'paid'
                                    break

                if _name_i != _name:
                    result = False
                # return result

            if result is False:
                print('Your reservation is not found.')
            break


def change_reservation(_reserves, _openings):
    """ Read the user's input for the park name and guest name.
        Use the park name and guest name to search for the corresponding park reservations (_reserves)
        If the reservation is not found, notify the user.
        If the reservation is found, display the reservation information and
            If its payment status is 'reserved', notify the user.
            If its payment status is 'paid', then
                Ask the user for the new valid month and the new valid date.
                Check for the availability of the new month and date.
                    If it is available, display the new reservation information.
                    If it is not available, notify the user.

        NOTE: The user does not allow to change the duration of the reservation.

        :param _reserves: park reservations
        :param _openings: park openings
        :return: Nothing
    """
    result = False
    while True:
        _park = str(input('Enter park: '))
        if _park in park_openings.keys():
            _name = input('Enter guest name: ')
            break
        else:
            print(f'{_park} does not exist.')
            continue
    for park, info in _reserves.items():
        if _reserves.get(park) == []:
            print('Your reservation is not found.')
            break
        if _park == park:
            for i in info:
                _day = i.get('date')
                _month = i.get('month')
                _duration = i.get('duration')
                _night = _duration - 1
                if _name != i.get('name'):
                    continue
                if _name == i.get('name'):
                    result = True
                    if i.get('status') == 'reserved':
                        print(f'Your reservation: {_day}/{_month} for {_duration} days, {_night} nights.')
                        print('You must a make payment before changing this reservation, '
                              'or you can cancel this reservation.')
                    elif i.get('status') == 'paid':
                        print(f'Your reservation: {_day}/{_month} for {_duration} days, {_night} nights.')
                        list_m = _openings.get(_park)
                        print(f'Available months: {list_m}')
                        while True:
                            input_m = int(input('Enter month: '))
                            if input_m in list_m:
                                i['month'] = input_m
                                break
                            else:
                                print('month is out of range.')
                                continue
                        while True:
                            input_d = int(input('Enter date: '))
                            if 0 < input_d <= 25:
                                i['date'] = input_d
                                break
                            else:
                                print('date is out of range.')
                                continue
                        print(f'Your new reservation: {input_d}/{input_m} for {_duration} days, {_night} nights.')
                        break
                if _name != i.get('name'):
                    result = False

            if result is False:
                print('Your reservation is not found.')
            break


def cancel_reservation(_reserves):
    """ Read the user's input for the park name and guest name.
        Use the park name and guest name to search for the corresponding park reservations (_reserves)
        If the reservation is not found, notify the user.
        If the reservation is found, display the reservation information and
            If the payment status is 'reserved', remove the reservation from the park reservations and notify the user.
            If the payment status is 'paid', notify the user that refund is not available.
                If the user still insists on the cancellation, then
                    remove the reservation from the park reservations and notify the user.

        :param _reserves: park reservations
        :return: Nothing
    """
    result = False
    while True:
        _park = str(input('Enter park: '))
        if _park in park_openings.keys():
            break
        else:
            print(f'{_park} does not exist.')
            continue
    for park, info in _reserves.items():
        if _park == park:
            name = str(input('Enter guest name: '))
            if info == []:
                print('Your reservation is not found.')
                break
            for i in info:
                # print(j)
                if name != i.get('name'):
                    continue
                if name == i.get('name'):
                    result = True
                    print(f'Your reservation: {i.get('date')}/{i.get('month')} for {i.get('duration')} days,'
                          f' {i.get('duration') - 1} nights.')
                    if i.get('status') == 'paid':
                        print('You already made the payment. You will not receive a refund.')
                        choose = input('Do you still want to cancel the reservation? (y/n) ')
                        if choose == 'n':
                            print('Your reservation is not canceled.')

                        elif choose == 'y':
                            info.remove(i)
                            print('Your reservation is canceled.')

                    elif i.get('status') == 'reserved':
                        info.remove(i)
                        print('Your reservation is canceled.')
                if name != i.get('name'):
                    result = False
                    print('Your reservation is not found.')

            if result is False:
                print('Your reservation is not found.')
            break


def run_choice(_reserves, _openings, _fees, _choice):
    """ Receive menu choice (_choice) as function parameter.
        Call function corresponding to each choice.
    """
    if _choice == 1:
        _month = int(input('Enter month: '))
        _list = find_available_parks(_openings, _month)
        print(_list)
    elif _choice == 2:
        ch_2 = get_reserve_info(_reserves, status="Guest")
        print(ch_2)
    elif _choice == 3:
        make_reservation(_reserves, _openings)
    elif _choice == 4:
        make_payment(_reserves, _fees)
    elif _choice == 5:
        change_reservation(_reserves, _openings)
    elif _choice == 6:
        cancel_reservation(_reserves)
    elif _choice == 7:
        ch_7 = get_reserve_info(_reserves, 'Admin')
        print(ch_7)


def read_choice():
    """ Display and read menu choice (_choice) as user input.
        If user enters invalid menu choice, keep asking user to enter
        another menu choice.
        Once the menu choice is valid, return such menu choice.
    """
    while True:
        print('\nChoices')
        print('1. Find available parks')
        print('2. Display reservations')
        print('3. Make a reservation')
        print('4. Make a payment')
        print('5. Change a reservation')
        print('6. Cancel a reservation')
        print('7. Display reservations by Admin')
        print('0. Exit')

        _choice = int(input('Enter your choice: '))
        if 0 <= _choice <= 7:
            break
        else:
            print('Your choice is invalid.  Choose again.')
    return _choice


# Main
# Read explanations of park_openings, park_reserves, park_fees in the pdf handout.
park_openings = {'Doi Inthanon': [1, 2, 3, 4, 5, 11, 12],
                 'Khao Yai': [1, 2, 3, 4, 5, 10, 11, 12],
                 'Erawan': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                 'Thap Lan': [1, 2, 6, 7, 8, 9, 10, 11, 12],
                 'Phi Phi': [1, 2, 3, 4, 5, 6, 10, 11, 12],
                 'Similan': [1, 2, 3, 4, 11, 12]}

temp_reserve1 = {'name': 'Ann', 'month': 1, 'date': 15, 'duration': 2, 'status': 'paid'}
temp_reserve2 = {'name': 'Bob', 'month': 12, 'date': 25, 'duration': 5, 'status': 'paid'}
temp_reserve3 = {'name': 'Charlie', 'month': 11, 'date': 2, 'duration': 3, 'status': 'reserved'}
temp_reserve4 = {'name': 'Mary', 'month': 3, 'date': 10, 'duration': 2, 'status': 'reserved'}
temp_reserve5 = {'name': 'Nancy', 'month': 2, 'date': 7, 'duration': 4, 'status': 'reserved'}
temp_reserve6 = {'name': 'Owen', 'month': 12, 'date': 2, 'duration': 3, 'status': 'paid'}

park_reserves = {'Doi Inthanon': [temp_reserve1],
                 'Khao Yai': [temp_reserve2, temp_reserve3],
                 'Erawan': [temp_reserve4],
                 'Thap Lan': [temp_reserve5],
                 'Phi Phi': [],
                 'Similan': [temp_reserve6]}

park_fees = {'Doi Inthanon': [30, 60, 1000, 3],
             'Khao Yai': [20, 40, 2400, 8],
             'Erawan': [30, 60, 1800, 3],
             'Thap Lan': [10, 20, 600, 4],
             'Phi Phi': [20, 40, 1500, 2],
             'Similan': [50, 100, 2000, 2]}

choice = read_choice()
while 0 < choice <= 7:
    run_choice(park_reserves, park_openings, park_fees, choice)
    choice = read_choice()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import doctest

    doctest.testmod()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
