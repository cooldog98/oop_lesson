# text = input('Enter text: ')
# _dict = {}
# len_text = len(text)
# for i in range(len_text):
#     if text[i] == ' ':
#         continue
#     _dict[text[i]] = 1
#     for j in range(i):
#         if text[i] == '':
#             continue
#         if text[j] == text[i]:
#             _dict[text[i]] = _dict[text[i]] + 1
# print(_dict)
# for key, value in _dict.items():
#     print(f"There are {value} {key}'s")




msg = input('Input a message: ')
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
len_msg = len(msg)
_dict = {}
time = 0

for i in range(len_msg):
    if msg[i] in vowels:
        # _dict[msg[i]] = _dict[msg[i]] + 1
        time = time + 1
        print(f'{msg[i]} {time}')
    if msg[i] == '':
        continue

