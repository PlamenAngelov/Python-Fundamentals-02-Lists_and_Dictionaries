from math import sqrt

numbers = list(map(int,input().split(" ")))

new_list = []

for item in numbers:
    if item > 0 and sqrt(item) == int(sqrt(item)):
        new_list.append(item)

new_list.sort(reverse=True)

for item in new_list:
    print(item, end = ' ')

# print(*new_list)