while True:
    a, b, c = list(map(int, input().split()))
    c_a = a ** 2
    c_b = b ** 2
    c_c = c ** 2
    arrayList = [c_a, c_b, c_c]
    arrayList.sort()
    if a == 0:
        break
    if arrayList[2] == arrayList[0]+arrayList[1]:
        print('right')
    if arrayList[2] != arrayList[0]+arrayList[1]:
        print('wrong')
