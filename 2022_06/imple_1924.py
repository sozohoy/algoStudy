import sys

A, B = map(int, sys.stdin.readline().strip().split(" "))

day = ['MON', 'TUE', "WED", "THU", "FRI", "SAT", "SUN"]
monthToDay = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

dayCount = 0

for i in range(A):
    dayCount += monthToDay[i]
dayCount += B
dayIdx = (dayCount % 7) - 1
print(day[dayIdx])
