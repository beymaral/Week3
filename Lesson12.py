

# set1 = {'Hi', 'Hello', }
# set2 = {'hi', 'Greetings', 'Hey', }
# set3 = {'Hi', 'Yo'}
#
# print(set1.intersection(set3, set2))
#
# set1 = {1, 2}
# set2 = {3}
# set3 = {4, 5}
# set4 = {3, 2, 6}
# set5 = {6}
# set6 = {7, 8}
# set7 = {9, 8}
# set2.update(set4)
# set1.update(set4)
# set4.update(set5)
# set6.update(set7)
#
# set1.update(set2)
# set1.update(set4)
# print(set2)
# print(set1)
# print(set4)
# print(set6)
#
# set1 = {2, 3, 5}
# set2 = {2, 3, 5}
# if set2.issuperset(set1):
#     print(f'Object {set2}is superset')
# # elif set1.issuperset(set2):
# #     print(f'Object {set1}is superset')
# else:
#     print('there are no subsets')
# if set1 == set2:
#     print('They are equal')

# comprehensions - lists, dict
# lists = []
# for i in range(1, 10001):
#     lists.append(i)
# print(lists)
# str1 = 'jajdaijdiwajdiawjdiwajdiawjdiwajdoiawjdawjdiowajdoawi'
# lists = [i for i in str1]
#
#
#
# # lists = [i for i in range(1, 10001)]
# print(lists)

# import datetime
#
# time_now = datetime.datetime.now()
# print(time_now)


# lists = []
# time_now = datetime.datetime.now()
# for i in range(1, 10001):
#     lists.append(i)
# delta = datetime.datetime.now() - time_now
# print(delta)
#
# time_now = datetime.datetime.now()
# lists = [i for i in range(1, 10001)]
# delta = datetime.datetime.now() - time_now
# print(delta)


# lists = [i for i in range(1, 10001) if i % 2 == 0 and i % 5 == 0]
# print(lists)

# s = int(input())
# fact = 1
# for i in range(1, s + 1):
#     fact *= i
# print(fact)

# dicts = {i: i**2 for i in range(1, 5)}
# print(dicts)
# lists = {'apple', 'pineapple', 'pen', 'banana', 'pear'}
# dicts = {i: i+i for i in lists}
# print(dicts)
# import random
#
# l = ['rock', 'paper', 'scissors']
# opponent = input('Your turn: ').lower()
# comp = random.choice(l)
# compindex = 0
# opponentindex = 0
# while opponent == comp:
#         compindex = compindex
#         opponentindex = opponentindex
#         print('Play again')
# if opponent == 'rock' and comp == 'scissors':
#     opponentindex += opponentindex
# if opponent == 'paper' and comp == 'rock':
#     opponentindex += opponentindex
# if opponent == 'scissors' and comp == 'paper':
#     opponentindex += opponentindex
# if opponent == 'scissors' and comp == 'rock':
#     compindex += compindex
# if opponent == 'rock' and comp == 'paper':
#     compindex += compindex
# if opponent == 'paper' and comp == 'scissors':
#     compindex += compindex
#
# if comp == 'rock' and opponent == 'scissors':
#     compindex += compindex
# if comp == 'paper' and opponent == 'rock':
#     compindex += compindex
# if comp == 'scissors' and opponent == 'paper':
#     compindex += compindex
# if comp == 'scissors' and opponent == 'rock':
#     opponentindex += opponentindex
# if comp == 'rock' and opponent == 'paper':
#     opponentindex += opponentindex
# if comp == 'paper' and opponent == 'scissors':
#     opponentindex += opponentindex
# if compindex >= 2:
#     print('You have lost')
# if opponentindex == 2:
#     print('You won')

import random

l = ['rock', 'paper', 'scissors']
compindex = 0
opponentindex = 0

while opponentindex < 2:
    cmpindex = 0
    userindex = 0
    comp = random.choice(l)
    opponent = input('Your turn: ').lower()
    print(comp)
    if opponent == comp:
        print("Play again")
    if opponent == 'rock' and comp == 'scissors':
        userindex = opponentindex + 1
        print(f'Comp has:{cmpindex} and you got: {userindex}')
    if opponent == 'paper' and comp == 'rock':
        userindex += opponentindex + 1
        print(f'Comp has:{cmpindex} and you got: {userindex}')
    if opponent == 'scissors' and comp == 'paper':
        userindex += opponentindex + 1
        print(f'Comp has:{cmpindex} and you got: {userindex}')
    else:
        cmpindex += compindex + 1
        print(f'Comp has:{cmpindex} and you got: {userindex}')

    if cmpindex == 2:
        print('You have lost')
        print(f'Comp has:{cmpindex} and you got: {userindex}')
        break
    elif userindex == 2:
        print('You won')
        print(f'Comp has:{compindex} and you got: {userindex}')
        break


from Lesson13 import test_func
import Lesson13