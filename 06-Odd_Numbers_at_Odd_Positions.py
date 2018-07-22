numbers = list(map(int,input().split(" ")))

odd_count = 0

for i in range(0,len(numbers)):
    if numbers[i]% 2 != 0 and i%2 != 0:
        print(f"Index {i} -> {numbers[i]}")