# def pack(total_or, box_size):
#     total = total_or // box_size
#     size = total_or % box_size
#     return total, size
#
#
# def display_outputs(total_or, box_size, num_full_box, unpack):
#     print(f'To pack {total_or} oranges, {num_full_box} boxes of size {box_size} are used.\n'
#           f'There are {unpack} unpacked oranges left.')
#
#
# total_oranges1 = int(input('Enter total oranges? '))
# box_size1 = int(input('Enter box size? '))
# total_oranges, box_size = pack(total_oranges1, box_size1)
# display_outputs(total_oranges1, box_size1, total_oranges, box_size)


# def read_inputs():
#     r = float(input('Enter radius? '))
#     h = float(input('Enter height? '))
#     shap = input('Enter shape choice (cy or co)? ')
#     return r, h, shap
#
#
# def compute_volume(r, h, shap):
#     import math
#     if shap == 'cy':
#         result = math.pi*r**2*h
#     elif shap == 'co':
#         result = (1/3)*math.pi*r**2*h
#     return result
#
#
# r, h, shap = read_inputs()
# volume = compute_volume(r, h, shap)
# print(f'Volume of your choice = {volume:.4f}')


# num = int(input("Type number: "))
# if num == 0:
#     print('Zero')
# elif num < 0:
#     print('Negative number')
# elif num > 0:
#     if num % 2 == 0:
#         print('Positive even number')
#     else:
#         print('Positive odd number')


# string = input('Enter a string: ')
# count = input('Enter a character to count: ')
# u = 0
# for i in string:
#     u = u + 1
#     if string == count:
#
#     print(u)


# _list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print('First display:')
# # for i in _list:
# #     result = i
# #
# #     print(result)
# first = _list
# print(first)
# print('Second display:')
# k = int(input("Input k: "))
# list_aws = []
# for i in range(0, len(_list), k+1):
#     aws = _list[i]
#     list_aws.append(int(aws))
#     list_aws1 = [u for u in list_aws]
# print(list_aws1)

# list_num = []
# num = input("Enter a number (type 'stop' to finish): ")
# list_num.append(num)
# if num == "stop":
#     print('Collected numbers:')
#     exit()
# while True:
#     num = input("Enter a number (type 'stop' to finish): ")
#     if num == 'stop':
#         break
#     list_num.append(num)
# print('Collected numbers:')
# for i in list_num:
#     print(i)


# num_cus = int(input('How many customers?: '))
# list_cu = []
# for i in range(num_cus):
#     print(f'Customer #{i+1}')
#     name = input('Name: ')
#     age = input('Age: ')
#     list_cu.append([name,age])
# print()
# print('Customer List:')
# for i in list_cu:
#     print(f'{i[0]} {i[1]}')


# i = 1
# list_gu = []
# all_list = []
# list_num = []
# y = 0
#
# # num_gu = int(input("How many guests? "))
# while True:
#     y = y + 1
#     print(f'Table No. {y}')
#     num_gu = int(input("How many guests? "))
#     if num_gu <= 0:
#         break
#     list_num.append(num_gu)
#     for i in range(num_gu):
#         guest = float(input(f"Guest#{i+1}: How much rice serving: "))
#         list_gu.append(guest)
#         all_list.append(guest)
#     sum_gu = sum(list_gu)
#     print(f'Table rice servings: {sum_gu:.2f}')
#     print()
#     list_gu.clear()
#
# sum_all = sum(all_list)
# sum_num_gu = sum(list_num)
# print(f'Totally, there are {y-1} tables with {sum_num_gu} guests.')
# print(f'Total rice servings = {sum_all:.2f} servings.')

# listq = []
# list_m = []
# while True:
#     s = int(input('Get up (0) or Sleep more (>0)? '))
#     listq.append(s)
#     list_m.append(s)
#     if s == 0:
#         break
# l = len(listq)
# su = sum(list_m)
# print(f'Your {l-1} snoozes take {su} minutes in total.')
# print('Have a nice day!')



while True:
    sn = input("Enter student name (or type 'done' to finish): ")
    if sn == 'done':
        break
    while True:
        g = (input("Enter a grade for Torres (or type 'done' to finish): "))
        if g == 'done':
            break

