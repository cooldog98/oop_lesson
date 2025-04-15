# n = int(input('Enter n: '))
# i = 1
# odd_even = str(input('Choose odd or even (o/e): '))
# list_num = []
# while i < n:
#     if i % 2 == 0 and odd_even == 'e':
#         list_num.append(i)
#         print(f'{i},', end=' ')
#     elif i % 2 != 0 and odd_even == 'o':
#         list_num.append(i)
#         print(f'{i},', end=' ')
#     i = i + 1
# print()
# print(f'Sum of {len(list_num)} printed numbers = {sum(list_num)}')



# vowels = ['a', 'e', 'i', 'o', 'u']
# list_character = []
# t = 0
#
# character = str(input('Enter character: '))
# character_new = character.lower()
# if character_new not in vowels:
#     t = t + 1
# list_character.append(character)
# al_x = ['x','X']
# while character not in al_x:
#     character = str(input('Enter character: '))
#     character_new = character.lower()
#     list_character.append(character)
#     if character == 'x':
#         list_character.remove('x')
#     if character == 'X':
#         list_character.remove('X')
#
#     if character_new == 'x':
#         t = t - 1
#     if character_new not in vowels:
#         t = t + 1
#
# print(list_character)
# len_c = len(list_character)
# print(f'You enter {len_c} characters.')
# print(f'You enter {t} non-vowels.')


# vowels = ['a', 'e', 'i', 'o', 'u']
# list_character = []
# t = 0
#
# character = str(input('Enter character: '))
# character_new = character.lower()
# if character_new not in vowels:
#     t = t + 1
# list_character.append(character)
# al_x = ['x','X']
# while True:
#     character = str(input('Enter character: '))
#     character_new = character.lower()
#     if character_new == 'x':
#         break
#     list_character.append(character)
#
#     if character == 'x':
#         list_character.remove('x')
#     if character == 'X':
#         list_character.remove('X')
#
#     if character_new == 'x':
#         t = t - 1
#     if character_new not in vowels:
#         t = t + 1
#
# print(list_character)
# len_c = len(list_character)
# print(f'You enter {len_c} characters.')
# print(f'You enter {t} non-vowels.')


# _dict = {}
# while True:
#     name = str(input('Enter name: '))
#     if name == 'X':
#         break
#     score = float(input('Enter score: '))
#     _dict.update({name: score})
# print(_dict)
# for key, value in _dict.items():
#     print(f'{key} received {value:.2f}')


# scores = {'Ivan': 14.3, 'John': 16.43, 'Karen': 9.82, 'Laura': 13.4, 'Mike': 17.239}
#
# scores1 = scores.values()
# average = sum(scores1)/len(scores1)
# print(f'Average score = {average:.2f}')
# print('Students who receive scores more than average are')
# for key, value in scores.items():
#     if value > average:
#         print(key)



