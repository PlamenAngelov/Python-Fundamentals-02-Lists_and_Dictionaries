numbers = list(map(int,input().split(" ")))

odd_count = 0

for num in numbers:
    if num% 2 != 0:
        odd_count += 1

print(odd_count)