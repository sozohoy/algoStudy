def solution(id_list, report, k):
    answer = []
    reportArray = [[0 for i in range(1)] for j in range(len(id_list))]
    countCheckArray = []
    isFull = False
    # split으로 report를 쪼갠 후 reportArray에 추가하는 방식으로 진행하면 될 것 같음.
    # reportArray[0] == id_list의 아이디
    report = list(set(report))

    # testCase 3, 10, 11, 14, 15, 20 시간 초과
    for i in range(len(id_list)):
        reportArray[i][0] = id_list[i]

    for i in range(len(report)):
        ## 이곳이 문제
        tmp = report[i].split(" ")
        for j in range(len(id_list)):
            if tmp[0] == reportArray[j][0]:
                if tmp[1] in reportArray[j]:
                    break
                reportArray[j].append(tmp[1])

    # id_list들을 pop한 이후(순서는 id_list 순으로 들어 왔을 테니), 각 요소를 카운트 하는 방법을 사용해야하나

    # countCheckArray에서 count --> k 이상일 경우 어떻게 하는가..

    for i in range(len(reportArray)):
        for j in range(1, len(reportArray[i])):
            countCheckArray.append(reportArray[i][j])

    for i in range(len(id_list)):
        if id_list[i] in countCheckArray and countCheckArray.count(id_list[i]) < k:
            while id_list[i] in countCheckArray:
                countCheckArray.remove(id_list[i])

    countCheckArray = list(set(countCheckArray))

    for i in range(len(id_list)):
        count = 0
        for j in range(1, len(reportArray[i])):
            if len(reportArray[i]) == 1:
                break
            if reportArray[i][j] in countCheckArray:
                count += 1
        answer.append(count)

    return answer