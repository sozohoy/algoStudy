N = int(input())
count = 0
for i in range(1, N+1):
    sol = list(map(int, str(i)))  # ex 12345 라는 숫자를 1,2,3,4,5로 나눠주는 코드
    count = sum(sol) + i
    if N == count:
        print(i)
        break
    if N == i:
        print(0)
        break
    count = 0
