numbers = list(map(int,input().split(" ")))
numbers.sort()
result = ""
for item in numbers:
    result += f"{item} <= "

print(result.strip(" <= "))