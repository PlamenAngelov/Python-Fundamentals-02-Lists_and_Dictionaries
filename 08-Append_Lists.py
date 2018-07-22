list_of_strings = list(map(str,input().split("|")))

for i in range(len(list_of_strings)-1,-1,-1):
    temp_list = list(map(str,list_of_strings[i].split(" ")))
    for item in temp_list:
        if item != "":
            print(f"{item} ", end ='')



