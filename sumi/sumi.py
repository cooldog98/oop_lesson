_list = []
n = int(input(''))
if 1 <= n <= 10000:
    for i in range(1, n+1):
        _list.append(i)
        _sum = sum(_list)
    print(_sum)
    _list.clear()
