# shop_cash = [10000, 44000, 30000, 12300, 45000, 90000, 78999]
# expenses = [3000, 3000, 3500, 4200, 3700, 5200, 2100]
# # all_cash = sum(shop_cash)
# # all_expenses = sum(expenses)
# # profit = all_cash - all_expenses
# # print(profit)
#
# def get_money(shop_cash, expenses):
#     all_cash = sum(shop_cash)
#     all_expenses = sum(expenses)
#     profit = all_cash - all_expenses
#     return profit

# profitprint(get_money(shop_cash, expenses))

# day2 = get_money(expenses=expenses2, shop_cash=shop_cash2)
# print(day2)

# *args, **kwargs

# def get_arguments(*args, **kwargs):
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)
#
# get_arguments(1, 2, 3, 'dawdwa', [1, 0], name = 'Nazgul', age=26)

# d = {
#     'name': 'AALY',
#     'age':
#     }


def get_list_square(*args, **kwargs):
    result = []
    # dicts = {}
    if args:
        for i in args:
            result.append(i**2)
    if kwargs:
        for key, value in kwargs.items():
            if type(value) == str:
                kwargs.update({
                    key: value.upper()
                })
            if type(value) == set:
                kwargs.update({
                    key: [value]
                })

    return result, kwargs
print(get_list_square(1, 2, 3, 4, 625, name = "Nazigul", age = 50, sets ={1, 4, 5, }))


