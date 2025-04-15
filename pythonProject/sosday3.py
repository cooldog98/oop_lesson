#def round_or_not(num):
#    if float(num) - int(float(num)) >= 0.5:
#        print(int(float(num)) + 1)
#    else:
#        print(int(float(num)))
#    return int()
#user_num = input("What is your number? ")
#round_or_not(user_num)

#SMALL = 90
#MEDIUM = 105
#LARGE = 121
#USED = None

#x = input("How many bananas do you eat today?")
#if int(float(x)) > 0:
#    y = input("What is the size of the banana?")
#    m = y.upper()
#    if str(m) == str("SMALL"):
#        print(f"You eat {x} bananas today.")
#        print(f'1 banana = {SMALL} calories.')
#        print(f'10 banana = {SMALL * int(float(x))} calories.')
#    elif str(m) == str("MEDIUM"):
#        print(f"You eat {x} bananas today.")
#        print(f'1 banana = {MEDIUM} calories')
#        print(f'10 banana = {MEDIUM * int(float(x))} calories.')
#    elif str(m) == str("LARGE"):
#        print(f"You eat {x} bananas today.")
#        print(f'1 banana = {LARGE} calories')
#        print(f'10 banana = {LARGE * int(float(x))} calories.')
#    else:
#        print(f'Invalid size Please input only Small, Medium, Large')
#elif int(x) == 0:
#    print(f"You eat {x} bananas today.")
#    print(f'1 banana = {USED} calories')
#    print(f'0 banana = {0} calories')

#word = ""
#alphabet = "abcdefghijklmnopqrstuvwxyz"
#for the_word in alphabet:
#    b = "Host"
#    print(b)
#    break
#print(word)

#start = int(input("What is the start number of the loop? "))
#stop = int(input("What is the stop number of the loop? "))
#for i in range(start,stop):
#    if i % 2 == 0:
#        print(f'{i} is an even number.')
#    else:
#        print(f'{i} is an odd number.')

#which_department = ["Computer", "Software", "Mechanical", "and", "Knowledge", "Engineering", "Banana", "Science",
#                    "Dancing", "Red herring"]

#for my_depart in which_department:
#    if my_depart == "Software":
#        print("Software")
#    elif my_depart == "and":
#        print("and")
#    elif my_depart == "Knowledge":
#        print("Knowledge\nEngineering")
#    else:
#        continue

'''death_report = {
    'Stable Boy Tomas': {'Age': 17, 'Cause of Death': "Horse kicking", 'Date': "1315 DR-03-03"},
    'Princess Elara': {'Age': 29, 'Cause of Death': "Falling", 'Date': "1315 DR-03-10"},
    'Bard Taliesin': {'Age': 29, 'Cause of Death': "Duel", 'Date': "1315 DR-03-15"},
    'Rogue Thief Kael': {'Age': 31, 'Cause of Death': "Executed", 'Date': "1315 DR-03-20"},
    'Hunter Finnian': {'Age': 20, 'Cause of Death': "Wolf Attack", 'Date': "1315 DR-03-25"},
    'Sailor Roderic': {'Age': 41, 'Cause of Death': "Falling", 'Date': "1315 DR-04-10"},
    'Knight Commander Duncan': {'Age': 42, 'Cause of Death': "Battlefield Injury", 'Date': "1315 DR-04-15"},
    'Innkeeper Bess': {'Age': 24, 'Cause of Death': "Mysterious Illness", 'Date': "1315 DR-04-20"},
    'Lord Garrick': {'Age': 45, 'Cause of Death': "Garlic Allergy", 'Date': "1315 DR-04-25"},
    'Blacksmith Hrothgar': {'Age': 48, 'Cause of Death': "Forge Accident", 'Date': "1315 DR-04-30"},
    'Sir Reginald': {'Age': 51, 'Cause of Death': "Old Age", 'Date': "1315 DR-05-05"},
    'Merchant Galen': {'Age': 53, 'Cause of Death': "Murdered by Banana", 'Date': "1315 DR-05-10"},
    'Miss Seraphina': {'Age': 55, 'Cause of Death': "Old Age", 'Date': "1315 DR-05-15"},
    'Sorcerer Sellen': {'Age': 62, 'Cause of Death': "Magical Explosion", 'Date': "1315 DR-05-20"},
    'Dwarven Miner Thrain': {'Age': 75, 'Cause of Death': "Cave-in", 'Date': "1315 DR-05-25"},
    'Mage Apprentice Serin': {'Age': 23, 'Cause of Death': "Spell Backfire", 'Date': "1315 DR-05-30"},
    'Lady Aeliana': {'Age': 34, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-06-27"},
    'Blacksmith Luira': {'Age': 70, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-06-28"},
    'Madam Luika': {'Age': 70, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-06-28"},
    'Sir Luigi': {'Age': 70, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-06-28"},
    'Elven Archer Xenos': {'Age': 70, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-06-29"},
    'Elven Archer Lythiel': {'Age': 128, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-06-29"},
    'Knight Seenato': {'Age': 44, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-06-30"}
}
death_report["Lovely Girl Anri"] = {'Age': 16, 'Cause of Death': "Ritual Murdered", 'Date': "1315 DR-07-01"} #???
filtered_report = {}

for key, value in death_report.items():
    murder_causes = {"Murdered", "Ritual Murdered", "Murdered by Banana"}
    causes_of_death = value["Cause of Death"]
    if causes_of_death in murder_causes:
        filtered_report[key] = value.copy()
    #elif filtered_report.get("Caues of Death") == "Murdered" + str():
     #   print(key, value)
print(filtered_report)'''

"""SKE = 0

while SKE != 22:
    SKE += 1
    if SKE == 23:
        continue
    print("SKE" + str(SKE))
print("Let us journey onward, my junior. "
      "Together we shall forge a path and pass the torch "
      "of knowledge to the next generation!") """

'''name = input("What is your name? ")
name2 = name.isdecimal()
i = 0
while i <= 3:
    if name2 == False :
        print("Nah")
        name = input("What is your name? ")
        name2 = name.isdecimal()
        if name2 == False:
            print("Nah")
            name = input("What is your name? ")
            name2 = name.isdecimal()
            if name2 == False:
                print("Already 3 times? Access denied HAHAHA.")
            else:
                print(f'Your name is {name}? That weird!')
        else:
            print(f'Your name is {name}? That weird!')
    else:
       print(f'Your name is {name}? That weird!')
    i += 1
    break'''

# list comprehension
'''numbers = [x for x in range(10) if x % 2 == 0] # Please use List comprehension
print(numbers)'''

'''spells_dict = {
               "Mana": 100,
               "Fatigue": 0,
               "Fire Bolt": "Ignis",
               "Scorching Ray": "Arde",
               "Darkness": "Tenebrum",
               "Speak with the Dead": "In nocte concillium",
               "Hold Person": "Ad lapide ",
               "Magic Missile": "Tormentum"
               }

spells_list = [x for x in spells_dict.items()]
print(spells_list)'''

'''monsters_list = [
    "Dragon",
    "Beholder",
    "Mind Flayer",
    "Lich",
    "Goblin",
    "Orc",
    "Troll",
    "Kobold",
    "Owlbear",
    "Gelatinous Cube",
    "Demogorgon",
    "Vampire",
    "Ghost",
    "Skeleton",
    "Zombie",
    "Basilisk",
    "Chimera",
    "Griffon",
    "Harpy",
    "Mimic",
    "Sphinx",
    "Wyvern",
    "Yeti",
    "Kraken",
    "Banshee",
    "Medusa",
    "Gnoll",
    "Bugbear",
    "Ankheg",
    "Carrion Crawler"
]
monsters_dict = {key: monsters for monsters in monsters_list for key in range(30)}
print(monsters_dict)
print(dict.fromkeys(monsters_list).keys())''' #ค้างยังไม่ได้


'''#not_leap_years = 1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600
#leap_years = 1600, 2000, 2400
def is_leap_year(leap_year):
        is_leap_years = 1600, 2000, 2400
        if leap_year in is_leap_years:
            return True

user_year = input("What years do you want to check? ")
if is_leap_year(int(user_year)):
    print(f"{user_year} is a leap year.")
else:
    print(f"{user_year} is not a leap year.")'''


'''def please_be_polite():
    """This function hates you if you don't put anything in it"""
    return True

# Call function here
say = input()
if say == "":
    print("I love you~ \nI hate you! \nOi! Oi! You should input some text isn't it!?")

please_be_polite()'''

def str_split(string, Separate_By):

print(str_split("Praise The Sun!", " "))
print(str_split("1,2,3,4,5,6", ","))
print(str_split("Bananas", "a"))