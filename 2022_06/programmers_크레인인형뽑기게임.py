def solution(board, moves):
    result = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            item = board[j][i - 1]

            if item > 0:
                result.append(item)
                board[j][i - 1] = 0
                # for i in list를 사용할 경우 해당 요소로 수정이 이루어지면 반복문이 꼬인다.
                if len(result) > 1:
                    if result[-2] == item:  # 이미 append 된 상황이기에, append 하기 이전의 index와 판별 해야함.
                        result.pop(-1)
                        result.pop(-1)
                        answer += 2
                break

    return answer