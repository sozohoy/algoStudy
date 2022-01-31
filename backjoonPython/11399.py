N = int(input())
p = list(map(int, input().split()))
sortedList = sorted(p)
cnt = 0
realcnt = 0
for i in sortedList:
    cnt = cnt + i
    realcnt = realcnt + cnt

print(sortedList)