def solution(n, lost, reserve):
    result = n - len(lost)

    lost.sort()
    reserve.sort()

    results = []

    for j in lost:
        print(j)
        if j in reserve:
            result += 1
            reserve.remove(int(j))
        else:
            results.append(int(j))

    for i in results:

        if i - 1 in reserve:
            result += 1
            reserve.remove(int(i - 1))
        elif i + 1 in reserve:
            result += 1
            reserve.remove(int(i + 1))

    answer = result
    return answer