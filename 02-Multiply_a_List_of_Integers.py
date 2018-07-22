numbers_as_string = input().split(" ")
n = int(input())

list_numbers = []
index = 0
for item in numbers_as_string:
    list_numbers.append(int(item)*n)
    print(f"{list_numbers[index]} ", end = '')
    index += 1

#print(list_numbers)