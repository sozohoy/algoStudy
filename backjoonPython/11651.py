N = int(input())
arrayList = []
for _ in range(N):
    x, y = map(int, input().split())
    arrayList.append([y, x]) # y의 오름차순으로 정렬하라고 했기 때문에 반대로 넣어줌.

arrayList.sort() # y를 기준으로 오름차순 정렬이 된 상태
for i in range(N):
    print(arrayList[i][1], arrayList[i][0]) # x, y 형식으로 출력해주기 위함
