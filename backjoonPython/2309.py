listNan = []

for _ in range(9):
    listNan.append(int(input()))
total = sum(listNan)
check = 0
for i in range(8):
    for j in range(i+1, 9):
        if total - (listNan[i] + listNan[j]) == 100:
            del1 = listNan[i]
            del2 = listNan[j]
            break
# for 문 안에서 리스트 원소 삭제 시 에러 발생 함
listNan.remove(del1)
listNan.remove(del2)
listNan.sort()

for i in range(len(listNan)):
    print(listNan[i])
