# _dict = {'id': '1001', 'name': 'Ann', 'age': 18, 'birthday': '01/09/2018'}
# for key in _dict:
#     print(key)
import math


# scores = {'Beth': 66, 'Nancy': 79, 'Pat': 82, 'Zoe': 57, 'Ken': 94}
# for key in scores:
#     print(key)


# _dict = {'id': '1001', 'name': 'Ann', 'age': 18, 'birthday': '01/09/2018'}
# for val in _dict.values():
#     print(val)


# scores = {'Beth': 66, 'Nancy': 79, 'Pat': 82, 'Zoe': 57, 'Ken': 94}
# _sum = 0
# for val in scores.values():
#     print(val)
#     _sum += val
# print(f'Sum of scores = {_sum}')


# scores = {'Beth': 66, 'Nancy': 79, 'Pat': 82, 'Zoe': 57, 'Ken': 94}
# for key, value in scores.items():
#     print(f'{key} got score = {value}')



# _dict = {100: 200, 250: 500, 300: 600, 700: 1400, 730: 1460, 850: 1700}
# _dic = {}
#
# for key in _dict.keys():
#     if key % 100 == 0:
#         r = _dict.get(key)
#         _dic.update({key: r})
# print(_dic)


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


# _dict = {}
# list_score = []
# while True:
#     name = input("Enter name: ")
#     if name == 'Q':
#         break
#     score = float(input("Enter scores: "))
#     _dict.update({name: score})
# print(_dict)
#
# for key, value in _dict.items():
#     print(f"{key} got {value:.2f}")
#     if value < 60:
#         list_score.append(value)
#
# sum_list = sum(list_score)
# num = len(list_score)
# if num > 0:
#     average = sum_list / len(list_score)
#     print(f'Average scores of students who got below 60 = {average:.2f}')
# else:
#     print(f'No one got below 60.')


# def update1(x): id เซ็กว่า เบส เหมือนกันมั้ย ถ้าเหมือนจะได้เลขออกม่เหมือนกัน
#     print(id(x))
#     x[0] = -100
#     print(x)
#     x.append(5)
#     print(x)
#     print(id(x))
#
# x1 = [1,2,3]
# print(id(x1))
# update1(x1)
# print(x1)
# print(id(x1))


# def update(x, y, z, v, w):
#     v = 200
#     x[2] = 20
#     y.append(1000)
#     z = [101, 201]
#     w = 'bye'
#
# _list1 = [1, 2, 3, 4, 5]
# _list2 = [11, 12, 13, 14, 15]
# _list3 = [21, 22, 23, 24, 25]
# value = 100
# text = 'hi'
# update(_list1, _list2, _list3, value, text)
# print(_list1)
# print(_list2)
# print(_list3)
# print(value)
# print(text)


def update(x,y,z,w):
    x = 5
    y[1] = 3
    z = 'hi'
    w = [i**2 for i in range(1,5)]  # List comprehension
    print(x)
    print(y)
    print(z)
    print(w)
    return x,w

a = 2
b = [1, 2, 4, 8]
c = 'hello'
d = [100, 200, 300]
e, f = update(a, b, c, d)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)



