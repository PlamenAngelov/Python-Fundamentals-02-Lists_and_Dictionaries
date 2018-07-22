list_of_strings = list(map(str,input().split(" ")))
last = list_of_strings.pop()
list_of_strings.insert(0,last)

for item in list_of_strings:
    print(f"{item} ", end = '')