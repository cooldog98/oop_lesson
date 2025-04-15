# m = int(input('Enter m: '))
# n = int(input('Enter n: '))
#
# if m > n:
#     exit()
# i = m
# while i != n+1:
#     print(i)
#     i = i + 1

# m = int(input('Enter m: '))
# n = int(input('Enter n: '))
# k = int(input('Enter k: '))
#
# i = m
# while i <= n:
#     if i == k:
#         break
#     print(i)
#     i = i + 1


# _sum = 0
# _list = []
# x = int(input('Enter x: '))
# i = -999
# while x != i:
#     _list.append(int(x))
#     x = int(input('Enter x: '))
#     _sum = sum(_list)
# print(_sum)
# print(_list)


# n = int(input('Enter n: '))
# m = int(input('Enter m: '))
#
# i = 0
#
# while i != n:
#     j = 0
#     while j != m:
#         print(f'{i},{j}')
#
#         j = j + 1
#     i = i + 1


# x = int(input('Enter start for outer loop: '))
# y = int(input('Enter start for inner loop: '))
# z = int(input('Enter stop for outer loop: '))
# w = int(input('Enter stop for inner loop: '))
# a = int(input('Enter step for outer loop: '))
# b = int(input('Enter step for inner loop: '))
#
# i = x
# while i < z:
#     j = y
#     while j > w:
#         print(f'{i},{j}')
#         j = j + b
#     i = i + a


# x = int(input('Enter x: '))
# y = -99
# list_x = []
# while x != y:
#     list_x.append(x)
#     x = int(input('Enter x: '))
# sum_x = sum(list_x)
# len_x = len(list_x)
# print(f"Sum of {len_x} x's = {sum_x}")


# x = int(input('Enter x: '))
# y = -99
# list_x = []
# list_cum = []
# list_new = []
# while True:
#     while x != y:
#         list_x.append(x)
#         list_new.append(x)
#         x = int(input('Enter x: '))
#     sum_x = sum(list_x)
#     len_x = len(list_x)
#     list_cum.append(sum_x)
#     len_list_cum = len(list_new)
#     list_cum_sum = sum(list_cum)
#     print(f"Sum of {len_x} x's = {sum_x}")
#     print(f"Cumulative sum of {len_list_cum} x's = {list_cum_sum}")
#     quit_f = input('Continue or quit (q for quit): ')
#     if quit_f == 'q':
#         break
#     print()
#     list_x.clear()
#     list_x.append(x)
#     x = int(input('Enter x: '))
#     list_x.remove(-99)


# def read_count_and_sum_x():
#     x = int(input("Enter x: "))
#     ans = -99
#     list_x = []
#     while x != ans:
#         list_x.append(x)
#         x = int(input("Enter x: "))
#     sum_x = sum(list_x)
#     len_x = len(list_x)
#     return sum_x, len_x
#
#
# print('Round 1:')
# list_sc1 = []
# list_lc1 = []
# sum_x, len_x = read_count_and_sum_x()
# list_sc1.append(sum_x)
# list_lc1.append(len_x)
# #print(list_lc1)
# print(f"Sum of {len_x} x's = {sum_x}")
# print(f"Cumulative sum of {len_x} x's = {sum_x}")
# quit_f = input('Continue or quit (q for quit): ')
# if quit_f == 'q':
#     exit()
# i = 1
# list_s = []
# list_l = []
# print()
# while True:
#     list_s.append(sum_x)
#     list_l.append(len_x)
#     i = i + 1
#     print(f'Round {i}:')
#     sum_x, len_x = read_count_and_sum_x()
#     list_lc1.append(len_x)
#     list_sc1.append(sum_x)
#     list_sum = sum(list_s)
#     list_len = sum(list_l)
#     list_lc1_n = sum(list_lc1)
#     #print(list_lc1)
#     list_sc1_n = sum(list_sc1)
#     print(f"Sum of {len_x} x's = {sum_x}")
#     print(f"Cumulative sum of {list_lc1_n} x's = {list_sc1_n}")
#     quit_f = input('Continue or quit (q for quit): ')
#     if quit_f == 'q':
#         break
#     print()


# def read_cumulative_count_and_sum_x(cum_sum,cum_count):
#     listx = []
#     x = int(input('Enter x: '))
#     while x != -99:
#         listx.append(x)
#         x = int(input('Enter x: '))
#     lenx = len(listx)
#     sumx = sum(listx)
#     sumx_new = sumx + cum_sum
#     lenx_new = lenx + cum_count
#     return sumx_new, lenx_new
#
#
# list_sum = []
# list_len = []
# sumx_new, lenx_new = read_cumulative_count_and_sum_x(0,0)
# list_sum.append(sumx_new)
# list_len.append(lenx_new)
# print(f"Round 1: Cumulative sum of {lenx_new} x's = {sumx_new}")
# quit_f = input('Continue or quit (q for quit): ')
# if quit_f == 'q':
#     exit()
#
# print()
# i = 1
# list_sumc = []
# list_lenc = []
# while True:
#     i = i + 1
#     sumx_new, lenx_new = read_cumulative_count_and_sum_x(sumx_new, lenx_new)
#     list_sumc.append(sumx_new)
#     list_lenc.append(lenx_new)
#     sum_new = sum(list_sumc)
#     len_new = sum(list_lenc)
#     #print(list_sumc, list_lenc)
#     print(f"Round {i}: Cumulative sum of {len_new} x's = {sum_new}")
#     quit_f = input('Continue or quit (q for quit): ')
#     if quit_f == 'q':
#         break
#     print()
#     list_sumc.clear()
#     list_lenc.clear()


# def read_list_x():
#     list_x =[]
#     x = int(input("Enter x: "))
#     list_x.append(x)
#     while x != -99:
#         x = int(input("Enter x: "))
#         list_x.append(x)
#     list_x.remove(-99)
#     return list_x
#
#
# print('Round 1:')
# list_x1 = []
# sum_x3 = []
# sum_len = []
# all_len = []
# sum_f = []
# list_x = read_list_x()
# sum_list = sum(list_x)
# list_x1.append(list_x)
#
# len_x = len(list_x)
# sum_xtest = sum(list_x)
# sum_f.append(sum_xtest)
# sum_final = sum(sum_f)
# # print(f'list_x = {list_x}')
# # print(f'sum_xtest = {sum_xtest}')
# # print(f'sum_f = {sum_f}')
#
# all_len_1 = len(list_x)
# # print(list_x)
# sum_len.append(all_len_1)
# all_len_2 = sum(sum_len)
#
#
# # print(all_len_1)
# # print(sum_len)
# # print(all_len_2)
#
# print(f"Current list of x's = {list_x}")
# print(f"Current nested list of x's = {list_x1}")
# print(f"Cumulative sum of {all_len_2} x's = {sum_final}")
# quit_q = input('Continue or quit (q for quit): ')
# if quit_q == 'q':
#     exit()
# print()
# i = 1
# while quit_q != 'q':
#     i = i + 1
#     print(f'Round {i}:')
#
#     list_x = read_list_x()
#
#     list_x1.append(list_x)
#
#     sum_xtest = sum(list_x)
#     # print(f'sum_xtest = {sum_xtest}')
#     sum_f.append(sum_xtest)
#     # print(f'sum_f = {sum_f}')
#     sum_final = sum(sum_f)
#
#     l = [len(o) for o in list_x1]
#     all_len_2 = sum(l)
#
#     # print(f'list_x = {list_x}')
#     # print(list_x1)
#     # print(l)
#     # print(all_len_1)
#
#     print(f"Current list of x's = {list_x}")
#     print(f"Current nested list of x's = {list_x1}")
#     print(f"Cumulative sum of {all_len_2} x's = {sum_final}")
#     quit_q = input('Continue or quit (q for quit): ')
#     if quit_q == 'q':
#         break
#     print()







