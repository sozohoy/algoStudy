import sys

N = int(sys.stdin.readline())

# 3kg, 5kg --> 최소 갯수 세기
count = N
bag = 0
while True:
    if count % 5 == 0:
        bag += int(count // 5)
        print(bag)
        break

    count -= 3
    bag += 1

else:
    print(-1)