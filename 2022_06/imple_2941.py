import sys

alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = sys.stdin.readline().strip()

for i in alpha:
    word = word.replace(i, "a")

print(len(word))
# count = 0
#
# for i in range(len(alpha)):
#     if word.find(alpha[i]) != -1:
#         if word.find(alpha[i]) == 0:
#             word = word.replace(alpha[i], "!")
#             count += (word.count("!") // alpha[i].count(alpha[i]))
#         else:
#             word = word.replace(alpha[i], "*")
#             count += 1
#
# if word.count("!") > 0:
#     word = word.replace("!", "")
#
# if word.count("*") > 0:
#     word = word.replace("*", "")
#
# if word.count("-") > 0:
#     word = word.replace("-", "")
#
# if word.count("=") > 0:
#     word = word.replace("=", "")
# print(count)
#
# count += len(word)
