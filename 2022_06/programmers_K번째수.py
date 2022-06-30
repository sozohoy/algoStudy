def solution(array, commands):
    answer = []
    # command의 내부 스플릿 할 필요 x
    # [x][0], [x][1]이 슬라이스 해야하는 범위
    tmp = []

    for i in range(len(commands)):
        tmp = (array[(commands[i][0] - 1):commands[i][1]])
        tmp.sort()
        answer.append(tmp[commands[i][2] - 1])

    return answer