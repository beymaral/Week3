# functions

# def test_func():
#     print('Hello world')
#
# test_func()

# def test_func():
#     pass

# summ = int(input('Put the amount: '))
# years = int(input('Put the years '))
# # peryear = float(input('%: '))
# #
# # per_one_year = summ * peryear
# # cash = peryear * years + summ
#
# # print(cash)
#
# def get_cash(summ, years, peryear):
#     per_one_year = summ * peryear
#     cash = per_one_year * years + summ
#     # print(cash)
#     return cash


# the_cash = get_cash(10000, 5, 0.2)
# the_cash = get_cash(10000, 6, 0.2)
# the_cash = get_cash(10000, 4, 0.2)
# print(the_cash)
summ = int(input('Put the amount: '))
years = int(input('Put the years '))
# peryear = float(input('%: '))
#
# per_one_year = summ * peryear
# cash = peryear * years + summ

# print(cash)

def get_cash(summ, years, peryear=1.1):
    per_one_year = summ * peryear
    cash = per_one_year * years + summ
    # print(cash)
    return cash

# print(get_cash(100, 3, 1.4))

# for i in range(1, years + 1):
#     dividends = get_cash(summ, i, 0.1 * i)
#     print(dividends)


import random

# game = [[n1, n2, n3], [n4, n5, n6], [n7, n8, n9]]
lists = []
tik_tak = [['O', 0, 'x'], [0, 0, 'x'], ['x', 0, 'o']]
for i in range(len(tik_tak)):
    for j in range(len(tik_tak(i))):
        if tik_tak[i][j] == 0:
            lists.append((i, j))
            print()