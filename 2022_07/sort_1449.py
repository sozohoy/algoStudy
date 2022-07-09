import sys

N, L = map(int, sys.stdin.readline().split())
locate = list(map(int, sys.stdin.readline().split()))
locate.sort()

tape = 1
start = locate[0]
end = start + L - 0.5

for i in locate:
    if end >= i:
        continue
    else:
        tape += 1
        end = i + L - 0.5

print(tape)


# N, L = map(int, sys.stdin.readline().split())
# locate = list(map(int, sys.stdin.readline().strip().split(" ")))
# locate.sort()
#
# tapeLength = L
# count = 0
#
# for i in range(0, N):
#     if i != N-1:
#         distance = (locate[i+1] - locate[i] + 1)
#
#         if (locate[i+1] - locate[i]) > L:
#             continue
#         elif distance < tapeLength:
#             tapeLength -= distance
#         else:
#             count += 1
#             tapeLength = L
#
#     else:
#         if locate[i] - locate[i-1] + 1 > tapeLength:
#             count += 1
#
# print(count)