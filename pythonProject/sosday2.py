#backpack = ["Lifegem", "Too many Oranges", "Lunar Tear", "Crimson Tears", "Potion of Healing"]

#print("First item is " + backpack[2])
#print("Second item is " + backpack[4])
#print("Third item is " + backpack[0])
#print("Last item is " + backpack[3])

#backpack = ["Lifegem", "Too many Oranges", "Lunar Tear", "Crimson Tears", "Potion of Healing"]
#backpack[1] = "Orange"
#print(backpack)

#num_num = [1, 2, 2, 4, 7, 4, 4, 8, 7, 1, 3, 9]
#num_num.sort(reverse=True)
#print(num_num)

#name = ["Musa sapiens", "Grimm", "Lucatiel", "Jack", "Anri", "Ichi..wait Why this problem has my name!?"]
#sorted_name = sorted(name, key=len)
#print(sorted_name)
#print(sorted_name[0:5])

#backpack = ['Lifegem', 'Lunar Tear', 'Crimson Tears', 'Potion of Healing']
#backpack.remove("Lunar Tear")
#backpack.sort()
#backpack.insert(2, "Lifegem")
#print(backpack)

#dead_banana = ['Head', 'Body', 'Arm', 'Leg']
#full_body = '----'.join(dead_banana)
#print(full_body)

#backpack = ['Lunar Tear', 'Crimson Tears', 'Lifegem', 'Potion of Healing']
#print("Used first item: Potion of Healing.")
#backpack.pop()
#backpack.append("Empty Flask")
#print("Current items in backpack: " + str(backpack) + ".\n")
#print("Used second item: Lifegem.")
#backpack.remove("Lifegem")
#print("Current items in backpack: " + str(backpack) + ".\n")
#print("Used third item: Crimson Tears.")
#backpack.remove("Crimson Tears")
#backpack.append("Empty Flask")
#print("Current items in backpack: " + str(backpack) + ".\n")

#time_that_occur = []
#user_tuple = tuple(eval(input("Give me tuple: ")))

#time_that_occur.append(user_tuple.count(user_tuple[0]))
#time_that_occur.append(user_tuple.count(user_tuple[1]))
#time_that_occur.append(user_tuple.count(user_tuple[2]))
#time_that_occur.append(user_tuple.count(user_tuple[3]))

#user_tuple = list(user_tuple)

#position_of_most_occur_value = time_that_occur.index(max(time_that_occur)) #นับซ้ำมากที่สุด

#target_value= user_tuple[position_of_most_occur_value]

#for i in range(len(user_tuple)):
#    if user_tuple[i] == target_value: #เปลี่ยนที่ซ้ำเป็น Banana
#        user_tuple[i] = "Banana"

#print(tuple(user_tuple))

#spells_dict = {
#               "Mana": 100,
#               "Fatigue": 0,
#               "Fire Bolt": "Ignis",
#               "Scorching Ray": "Arde",
#               "Darkness": "Tenebrum",
#               "Speak with the Dead": "In nocte concillium",
#               "Hold Person": "Ad lapide ",
#               "Magic Missile": "Tormentum"
#               }

#print(f"The necromancer speaks out loud: {spells_dict["Speak with the Dead"]}")
 # change the dict values
#spells_dict.update({'Mana': 80, 'Fatigue': 10})
#print("The necromancer's stats after using the spell:")
#print(f"Mana: {spells_dict['Mana']}, Fatigue: {spells_dict['Fatigue']}")

#dict_1 = {
#    "Vitality": ["Increased HP", "Increased bleed resistance"],
#    "Attunement": ["Increased attunement slots", "Minor boost to spell casting speed"],
#    "Endurance": ["Increased stamina", "Increased equipment load", "Increased bleed resistance"],
#    "Strength": ["Increased physical attack for strength-based weapons", "Ability to wield heavier weapons"],
#    "Dexterity": ["Increased physical attack for dexterity-based weapons", "Reduced fall damage", "Increased casting speed for certain spells"],
#    "Intelligence": ["Increased magic attack for sorceries", "Increased magic adjustment for catalysts"],
#    "Faith": ["Increased miracle potency", "Increased magic adjustment for talismans"]
#    }
#dict_2 = dict_1.copy()
#print(dict_2)

#dict_2.clear()
#print(f"Don't ask me. I just want to use f-string to show the values: {dict_2}")

#burger_list = []
#burger = {"top": "bun", "middle 1": "cheese", "middle 2": "meat", "bottom": "bun"}
#burger_list = burger.copy()
#burger.clear()
#burger_list = burger_list.items()
#burger_list = list(burger_list)
#burger_list.sort()
#i, j = 1, 2
#burger_list[i], burger_list[j] = burger_list[j], burger_list[i]
#print(f"The dict should be blank by now: {burger}")
#print(f"WOW BURGER: {burger_list}")
#print()

#burger1 = {"top": "bun", "middle 1": "cheese", "middle 2": "meat", "bottom": "bun"}
#burger_list.clear()
#burger = burger1
#p, m = 0, 3
#l, r = 1, 2
#hit = list(burger.items())
#hit[p], hit[m] = hit[m], hit[p]
#hit[l], hit[r] = hit[r], hit[l]
#burger = dict(hit)
#burger['middle 2'] = "banana"
#print("Heh, Banana hamburger")
#print(f"Current state of burger: {burger}")
#print(f"Are your list: {burger_list} empty?")

print(f"56 rtggrgg")