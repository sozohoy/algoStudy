T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    room_cnt = N % H * 100
    room_num = N // H + 1

    if N % H == 0:
        room_cnt = H * 100
        room_num = N // H
    room = room_cnt + room_num
    print(room)