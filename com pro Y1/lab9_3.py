# seq = [1,3,2,6]
# seq2 = [seq2*3 for seq2 in seq]

# c_list = [-40,0,20,37,40,100]
# f_list = [(1.8 * i ) + 32 for i in c_list]
# print(f_list)

# N = 20
# s = [x for x in range(1, N+1) if x % 2 != 0 and x % 5 != 0]

# def f(n):
#     return sum([((2*i) + 5) ** 2 for i in range(1,n+1)])

#nums = [i for i in range(1,100) if i % 5 == 0 or i % 7 == 0]

# def print_map(map):
#     """
#     Display 2D array by replacing 0 with ., 1 with #, and 2 with X
#     :params 2D array contains integer 0,1,2
#     :return nothing
#
#     >>> print_map([[1,0],[0,2]])
#     #.
#     .X
#     >>> print_map([[2,2,1],[0,0,0],[1,2,0]])
#     XX#
#     ...
#     #X.
#     >>> print_map([[0],[1],[2]])
#     .
#     #
#     X
#     """
#     for row in:
#         for col in:
#
#
# map1 = [[1, 1, 1, 1],
#         [1, 0, 0, 0],
#         [1, 0, 1, 1],
#         [0, 2, 0, 1],
#         [1, 1, 0, 1]]
#
# map2 = [[1, 1, 1, 1, 0, 0, 0, 1],
#         [0, 2, 0, 0, 0, 1, 0, 1],
#         [1, 1, 0, 1, 1, 0, 2, 1]]
#
# # Show Map 1
# print("Map 1")
# print_map()
# print()
#
# # Show Map 2
# print("Map 2")
# print_map()
# print()


def read_matrix():
    """
    Read number of rows and columns of a matrix.
    Then, read each element and store it in a matrix.
    Return the read-in matrix
    :params Nothing
    :return 2D-list contains the matrix
    """
    row = int(input("Input #rows? "))
    column = int(input("Input #columns? "))
    i = 0
    j = 0
    list_matrix = []
    for i in range(row):
        i = i + 1
        list_e = []
        for j in range(column):
            j = j + 1
            element = int(input(f"Input element[{i}][{j}]: "))
            list_e.append(element)
        list_matrix.append(list_e)
    return list_matrix


def print_matrix(matrix):
    """
    Display a matrix, where each number is displayed in 5 spaces and right-aligned.
    :params a 2D-list contains a matrix
    :return Nothing
    """
    for row in matrix:
        list_ma = [f'{matrix:>5}' for matrix in row] #list comprehensions
        print(''.join(list_ma)) # join(1) = 9 8 7, join(2) = 6 5 4 คำสั่งjoinคือเอามา 9 8 7 \n 6 5 4



matrix = read_matrix()
# print(matrix)
print("Matrix A is")
print_matrix(matrix)



