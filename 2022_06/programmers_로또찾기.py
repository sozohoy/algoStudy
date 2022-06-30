def solution(lottos, win_nums):
    for i in win_nums:
        for j in range(len(lottos) - 1, -1, -1):
            if lottos[j] in win_nums or lottos[j] == 0:
                continue
            else:
                lottos.pop(j)

    if len(lottos) < 1:
        x = 6
    else:
        x = 7 - len(lottos)

    for i in range(len(lottos) - 1, -1, -1):
        if lottos[i] == 0:
            lottos.pop(i)

    if len(lottos) < 1:
        y = 6
    else:
        y = 7 - len(lottos)

    answer = [x, y]
    return answer