numbers = list(map(int,input().split(" ")))

new_list = []
for i in range(0,len(numbers)):
    if numbers[i] >= 0:
        new_list.append(numbers[i])

new_list.reverse()

if len(new_list) > 0:
    for item in new_list:
        print(f"{item} ", end = '')
else:
    print("empty")