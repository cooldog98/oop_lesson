# intn = int(input("Enter start date: "))
# if n <= 0:
#     print("Program exits")
#     exit()
# c = input(f"Enter degrees Celsius of date {n}: ")
# l = []
# a = n
# while c != 'exit':
#     k = []
#     if a % 2 == 0:
#         word = 'Fahrenheit'
#         th = float(c) / 5 * 9 + 32
#     else:
#         word = 'Kelvin'
#         th = float(c) + 273.15
#     a += 1
#     c = input(f"Enter degrees Celsius of date {a}: ")
#     k.append(word)
#     k.append(th)
#     l.append(k)
#
# for i in range(len(l)):
#     print(f"Date {n+i} has degrees {l[i][0]} of {l[i][1]:.1f}")
#


# n = int(input("Number of items: "))
# l = []
#
# for i in range(n):
#
#     s = input(f"Name[{i}]: ")
#     l.append(s)
# ind = int(input("Print name from index: "))
# print(l[ind])


# def f():
#     m = x + 1
#     n = y + 5
#     return m, n
#
# x, y = 2, 3
# x,y = f(x)
# print(x,y)

# even_num = []
# for i in range(5):
#     x = int(input('Enter even number: '))
#     # even_num = []
#     if x % 2 == 0:
#         even_num.append(x)
# print(f'The output is:\n{even_num}')


# x = int(input('x: '))
# y = int(input('y: '))
# z = int(input('z: '))
# i = 0
# j = 0
# k = 0
# z_new = z
# list_ = []
# for i in range(x):
#     for j in range(y):
#         for k in range(z_new, -1, -1):
#             list_.clear()
#             list_.append(i)
#             list_.append(j)
#             list_.append(k)
#             sum_list = sum(list_)
#             # print(list_)
#             print(f'{i},{j},{k} sum={sum_list}')
#     print()


# num_user = int(input('Number of users: '))
# list_i = []
# list_i_new = []
# list_all = []
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# result = ''
# result1 = ''
# for i in range(num_user):
#     first_name = input('First name: ')
#     for j in first_name:
#         if j not in vowels:
#             result = result + j
#
#     print(result)
    # list_i.clear()
#     list_i.append(result)
#     print(list_i)
# #     # list_i.remove(result)
#     list_i_new = list_i.copy()
#
#     last_name = input('Last name: ')
#     for k in last_name:
#         if k not in vowels:
#             result1 = result1 + k
#     print(result1)
#     list_i.append(result1)
#     list_i_new = list_i.copy()
#
#     age = int(input('Age: '))
#     list_i.append(age)
#     print(list_i)
#     list_i_new = list_i.copy()
#     list_i.clear()
#     list_all.append(list_i_new)
# print(f'All users: {list_all}')


# num_users = int(input('Number of users: '))
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# list_one = []
# list_all = []
# list_total = []
# result = ''
# result_1 = ''
#
# for i in range(num_users):
#     first = input('First name: ')
#     for j in first:
#         # print(first)
#         # print(j)
#         if j not in vowels:
#             result = result + j
#             # print(result)
#     list_one.append(result)
#     result = ''
#
#     last = input('Last name: ')
#     for k in last:
#         if k not in vowels:
#             result_1 = result_1 + k
#     list_one.append(result_1)
#     age = int(input('Age: '))
#     list_one.append(age)
#     list_all = list_one.copy()
#     list_total.append(list_all)
#     print(list_one)
#     # print(list_all)
#     # print(list_total)
#     result_1 = ''
#     list_one.clear()
#
# print(f'All users: {list_total}')




