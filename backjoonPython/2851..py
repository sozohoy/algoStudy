arr = [list(map(int, input().split())) for _ in range(10)]
result1 = 0
result2 = sum(arr[0])
max = 100
for i in range(1, len(arr)):
    result1 = result1 + sum(arr[i-1])
    result2 = result2 + sum(arr[i])
    if result2 >= 100:
        if (result2 - max) > (max - result1):
            result = result1
            break
    if result2 < 100:
        result = result2
print(result)
