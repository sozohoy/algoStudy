N = int(input())
m = 0
result = 0

for i in range(1, N+1):
    result += i
    m += 1
    if (result > N):
        m -= 1
        break;
        
print(m)

