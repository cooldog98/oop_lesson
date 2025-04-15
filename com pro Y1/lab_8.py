# score = ' '
# score1 = input('Enter student score (or just ENTER to end): ')
# all_score = []
# i = 0
# z = 0
# while score1 != score:
#     all_score.append(int(score1))
#     i = i + 0
#     score1 = input('Enter student score (or just ENTER to end): ')
#     if not score1:
#         break
# for i in all_score:
#     z = z + 1
#     print(f'Score #{z}: {all_score[z-1]}')
# average = sum(all_score)/len(all_score)
# print(f'Average score is {average:.2f}')
# mini = min(all_score)
# maxi = max(all_score)
# print(f'Minimum score is {mini}')
# print(f'Maximum score is {maxi}')


# score = ' '
# score1 = input('Enter student score (or just ENTER to end): ')
# i = 0
# a = 0
# all_score = []
# while score1 != score:
#     all_score.append(score1)
#     i =+ 1
#     score1 = input('Enter student score (or just ENTER to end): ')
#     if not score1:
#         break
# for i in all_score:
#     a = a + 1
#     all_score.sort(reverse=True)
#     print(f'Rank #{a}: {all_score[a - 1]}')


# score = ' '
# score1 = input('Enter student score (or just ENTER to end): ')
# all_score = []
# i = 0
# a = 0
#
#
# def score():
#     import math
#     average = sum(all_score) / len(all_score)
#     n = len(all_score)
#     total = [(y - average)** 2 for y in all_score]
#     up = sum(total)
#     #print(total)
#     down = n - 1
#     _sd = math.sqrt(up / down)
#     #print(f'Standard deviation is {_sd:.2f}')
#     return _sd
#
#
#
# while score1 != score:
#     all_score.append(int(score1))
#     score1 = input('Enter student score (or just ENTER to end): ')
#     i =+ 1
#     if not score1:
#         break
# average = sum(all_score)/len(all_score)
# print(f'Average score is {average:.2f}')
# #print(all_score)
#
# #print(all_score[0])
#
# _sd = score()
# print(f'Standard deviation is {_sd:.2f}')
#
# new1 = [int(u) for u in all_score]
#
# for i in range(len(all_score)):
#     i = i + 1
#     #print(new1[i-1])
#     if new1[i-1] >= average + (1.5* _sd):
#         print(f'Score #{i}: {all_score[i-1]} grade: A')
#     elif average + (1*_sd) <= new1[i-1] < average + (1.5 * _sd):
#         print(f'Score #{i}: {all_score[i-1]} grade: B+')
#     elif average + (0.5*_sd) <= new1[i-1] < average + (1.0 * _sd):
#         print(f'Score #{i}: {all_score[i - 1]} grade: B')
#     elif average <= new1[i-1] < average + (0.5*_sd):
#         print(f'Score #{i}: {all_score[i-1]} grade: C+')
#     elif average - (0.5*_sd) <= new1[i-1] < average:
#         print(f'Score #{i}: {all_score[i-1]} grade: C')
#     elif average - (1.0*_sd) <= new1[i-1] < average - (0.5*_sd):
#         print(f'Score #{i}: {all_score[i-1]} grade: D+')
#     elif average - (1.5*_sd) <= new1[i-1] < average - (1.0*_sd):
#         print(f'Score #{i}: {all_score[i-1]} grade: D')
#     elif new1[i-1] < average - (1.5*_sd):
#         print(f'Score #{i}: {all_score[i-1]} grade: F')



