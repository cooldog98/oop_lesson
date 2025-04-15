import math


APPETIZERS = {'som tam': 110,
              'salad': 100,
              'larb': 120,
              'bbq chicken': 95,
              'tom yam': 65}

ENTREES1 = {'basil pork': 580,
            'fried rice': 660,
            'pad thai': 565,
            'fried noodle': 520,
            'noodle with gravy': 405}

ENTREES2 = {'noodle soup': 330,
            'suki': 345,
            'bbq pork rice': 560,
            'chicken rice': 585,
            'green curry': 485}

DESSERTS = {'mango sticky rice': 170,
            'pie': 400,
            'cake': 350,
            'ice cream': 300,
            'fruit': 80}

DRINKS = {'soda': 110,
          'juice': 90,
          'iced tea': 80,
          'iced cocoa': 120,
          'iced coffee': 115}

BURNED_CALORIES_PER_HOUR = {
    'aerobics': 600,
    'badminton': 315,
    'cycling': 560,
    'housework': 215,
    'running': 550,
    'swimming': 420,
    'walking': 230,
}


def read_personal_info():
    print('Welcome to the SKE Calorie Tracker\nPlease provide your personal info.')
    _name = input('What is your name? ')
    _age = int(input('How old are you? '))
    _gender = input('What is your gender (F/M)? ')
    _meals = int(input('How many meals you eat pay day? '))
    _exercise = input('Choices of exercise: aerobics, badminton, cycling, housework, running, swimming, walking \n'
                      'Select one exercise choice: ')
    return _name, _age, _gender, _meals, _exercise


def create_line(width1, width2, width3, width4, width5):
    """ From five widht parameters,
            Return a string of dashes specified by these widths, separated by |.

            :param width1: int
            :param width2: int
            :param width3: int
            :param width4: int
            :param width5: int
            :return: a string of dashes specified by these widths, separated by |.
            >>> create_line(3,5,4,2,6)
            '|---|-----|----|--|------|'
            >>> create_line(1,2,3,4,5)
            '|-|--|---|----|-----|'
            >>> create_line(2,2,2,2,2)
            '|--|--|--|--|--|'
        """
    pass
    first = '-'*width1
    second = '-'*width2
    third = '-'*width3
    fourth = '-'*width4
    fifth = '-'*width5
    result_line = ('|{}|{}|{}|{}|{}|'.format(first, second, third, fourth, fifth))
    return result_line


def display_menu():
    print('\nHere is the food menu:')
    max_app_len = max([len(key) for key, val in APPETIZERS.items()]) + 2
    max_entree1_len = max([len(key) for key, val in ENTREES1.items()]) + 2
    max_entree2_len = max([len(key) for key, val in ENTREES2.items()]) + 2
    max_dessert_len = max([len(key) for key, val in DESSERTS.items()]) + 2
    max_drink_len = max([len(key) for key, val in DRINKS.items()]) + 2

    app_menu = [key for key in APPETIZERS.keys()]
    entree1_menu = [key for key in ENTREES1.keys()]
    entree2_menu = [key for key in ENTREES2.keys()]
    dessert_menu = [key for key in DESSERTS.keys()]
    drink_menu = [key for key in DRINKS.keys()]

    line = create_line(max_app_len, max_entree1_len, max_entree2_len, max_dessert_len, max_drink_len)
    print(line)
    print('|{:^{}}|'.format('Appetizers', max_app_len), end='')
    print('{:^{}}|'.format('Entree 1', max_entree1_len), end='')
    print('{:^{}}|'.format('Entree 2', max_entree2_len), end='')
    print('{:^{}}|'.format('Desserts', max_dessert_len), end='')
    print('{:^{}}|'.format('Drinks', max_drink_len))

    line = create_line(max_app_len, max_entree1_len, max_entree2_len, max_dessert_len, max_drink_len)
    print(line)
    for i in range(len(app_menu)):
        print(f'|{app_menu[i]:^{max_app_len}}|', end='')
        print(f'{entree1_menu[i]:^{max_entree1_len}}|', end='')
        print(f'{entree2_menu[i]:^{max_entree2_len}}|', end='')
        print(f'{dessert_menu[i]:^{max_dessert_len}}|', end='')
        print(f'{drink_menu[i]:^{max_drink_len}}|')
    line = create_line(max_app_len, max_entree1_len, max_entree2_len, max_dessert_len, max_drink_len)
    print(line)


def take_order():
    print('Please provide your choices of food.')
    _entree = input('Select entree choices or none: ')
    _drink = input('Select drink choices or none: ')
    _appetizer = input('Select appetizer choices or none: ')
    _dessert = input('Select dessert choices or none: ')
    return _appetizer, _entree, _dessert, _drink


def get_app_calories(_app_choice):
    if APPETIZERS.get(_app_choice) is None:
        return 0
    else:
        return APPETIZERS[_app_choice]


def get_entree_calories(_entree_choice):
    all_entrees = ENTREES1.copy()
    all_entrees.update(ENTREES2)
    if all_entrees.get(_entree_choice) is None:
        return 0
    else:
        return all_entrees[_entree_choice]


def get_dessert_calories(_dessert_choice):
    if DESSERTS.get(_dessert_choice) is None:
        return 0
    else:
        return DESSERTS[_dessert_choice]


def get_drink_calories(_drink_choice):
    if DRINKS.get(_drink_choice) is None:
        return 0
    else:
        return DRINKS[_drink_choice]


def compute_consumed_calories(_app_choice, _entree_choice, _dessert_choice, _drink_choice):
    """ From the user's choices of appetizer, entree, dessert and drink,
            Return the total calories based on the user's choices.

            :param _app_choice: string
            :param _entree_choice: string
            :param _dessert_choice: string
            :param _drink_choice: string
            :return: total calories based on the user's choices.
            >>> compute_consumed_calories('bbq chicken', 'fried rice', 'mango sticky rice', 'iced coffee')
            1040
            >>> compute_consumed_calories('none', 'chicken rice', 'fruit', 'juice')
            755
            >>> compute_consumed_calories('larb', 'none', 'cake', 'iced cocoa')
            590
            >>> compute_consumed_calories('som tam', 'noodle with gravy', 'none', 'soda')
            625
            >>> compute_consumed_calories('tom yam', 'fried noodle', 'ice cream', 'none')
            885
        """
    pass
    _appetizer = get_app_calories(_app_choice)
    _entree = get_entree_calories(_entree_choice)
    _dessert = get_dessert_calories(_dessert_choice)
    _drink = get_drink_calories(_drink_choice)
    total_calories = _appetizer + _entree + _dessert + _drink
    return total_calories


def get_needed_calories_per_day(_age, _gender):
    if _gender == 'F':
        if _age < 15:
            needed_calories = 1600
        elif 15 <= _age <= 50:
            needed_calories = 2000
        else:
            needed_calories = 1800
    else:
        if _age < 15:
            needed_calories = 2000
        elif 15 <= _age <= 50:
            needed_calories = 2600
        else:
            needed_calories = 2300
    return needed_calories


def compute_needed_calories_per_meal(_needed_calories_per_day, _num_meals):
    """ From the needed calories per day and number of meals,
            Return the average needed calories per meal

            :param _needed_calories_per_day: string
            :param _num_meals: int
            :return: average needed calories per meal.
            >>> compute_needed_calories_per_meal(2000, 2)
            1000.0
            >>> compute_needed_calories_per_meal(2000, 3)
            666.6666666666666
            >>> compute_needed_calories_per_meal(1800, 3)
            600.0
        """
    pass
    average_calories_per_meal = _needed_calories_per_day / _num_meals
    return average_calories_per_meal


def get_burned_calories(_exercise):
    # https://www.nutristrategy.com/caloriesburned.htm
    if BURNED_CALORIES_PER_HOUR.get(_exercise) is None:
        return 0
    else:
        return BURNED_CALORIES_PER_HOUR[_exercise]


def compute_exercise_duration(_exercise, _calories):
    """ From the user's choices of exercise and the given calories,
            Return exercise duration in FULL minutes.
            The duration must be sufficient for the user to burn the given calories.

            :param _exercise: string
            :param _calories: float
            :return: exercise duration in FULL minutes..
            >>> compute_exercise_duration('cycling', 250)
            27
            >>> compute_exercise_duration('walking', 500)
            131
            >>> compute_exercise_duration('housework', 300)
            84
        """
    pass
    exercise1 = get_burned_calories(_exercise)
    minute = (_calories*60)/exercise1
    final = math.ceil(minute)
    return final


def summarize_exercise(_name, _needed_calories_per_meal, _consumed_calories, _exercise):
    r""" From the neeeded and the consumed calories, and the given exercise
        Return a string reporting the exercise duration with the user's name and exercise.

        :param _name: string
        :param _needed_calories_per_meal: float
        :param _consumed_calories: int
        :param _exercise: string
        :return: String reporting the exercise duration with the user's name and exercise.
        >>> __exercise = summarize_exercise('Ann', 760, 975, 'cycling')
        >>> print(__exercise)
        Ann needs to do cycling as exercise for 24 minutes.
    """
    pass
    final_cal = _consumed_calories - _needed_calories_per_meal
    burned_cal = compute_exercise_duration(_exercise, final_cal)
    result_se = f'{_name} needs to do {_exercise} as exercise for {burned_cal} minutes.'
    return result_se


def get_exercise_summary(_name, _needed_calories_per_meal, _consumed_calories, _exercise):
    if _needed_calories_per_meal >= _consumed_calories:
        return _name + ' does not need to exercise.'
    else:
        exercise_text = summarize_exercise(_name, _needed_calories_per_meal, _consumed_calories, _exercise)
        return exercise_text


def acquire_summary(_name, _age, _gender, _app, _entree, _dessert, _drink, _needed_calories_per_meal,
                    _consumed_calories, _exercise):
    """ From the user's information,
            Return a string providing result summary of this program.

            :param _name: string
            :param _age: int
            :param _gender: string
            :param _app: string
            :param _entree: string
            :param _dessert: string
            :param _drink: string
            :param _needed_calories_per_meal: float
            :param _consumed_calories: int
            :param _exercise: string
            :return: string providing result summary of this program
            >>> __summary = acquire_summary('Ann', 19, 'F', 'none', 'fried rice', 'cake', 'soda', 1000, 1215,'swimming')
            >>> print(__summary)
            Ann's SUMMARY:
            Ann's choices of food:
            fried rice for entree, soda for drink,
            along with none for appetizer and cake for dessert.
            Ann's calorie tracker:
            Needed calories per meal = 1000.000
            Consumed calories = 1215.000
            Ann's exercise suggestion:
            Based on Ann's choices of food and exercise,
            Ann needs to do swimming as exercise for 31 minutes.
        """
    pass
    min_ac = get_exercise_summary(_name, _needed_calories_per_meal, _consumed_calories, _exercise)
    final = (f"{_name}'s SUMMARY:\n{_name}'s choices of food:\n{_entree} for entree, {_drink} for drink,"
             f"\nalong with {_app} for appetizer and {_dessert} for dessert.\n{_name}'s calorie tracker:"
             f"\nNeeded calories per meal = {_needed_calories_per_meal:.3f}\nConsumed "
             f"calories = {_consumed_calories:.3f}"
             f"\n{_name}'s exercise suggestion:\nBased on {_name}'s choices of food and exercise,\n{min_ac}")
    return final


# main part
# Fill in code for main part below
name, age, gender, meals, exercise = read_personal_info()
display_menu()
appetizer, entree, dessert, drink = take_order()
compute_needed_calories_per_meal(get_needed_calories_per_day(age, gender), meals)
print()
print(acquire_summary(name, age, gender, _app=appetizer, _entree=entree, _dessert=dessert, _drink=drink,
                      _needed_calories_per_meal=compute_needed_calories_per_meal
                      (_needed_calories_per_day=get_needed_calories_per_day(age, gender), _num_meals=meals),
                      _consumed_calories=compute_consumed_calories(_app_choice=appetizer, _entree_choice=entree,
                                                                   _dessert_choice=dessert, _drink_choice=drink),
                      _exercise=exercise))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import doctest

    doctest.testmod()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
