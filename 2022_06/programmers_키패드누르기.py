left = [1, 4, 7]
right = [3, 6, 9]
mid = [2, 5, 8, 0]
pad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0, "#"]  # left 첫 위치는 [3][0], right [3][2]
]

def solution(numbers, hand):
    leftIdx, rightIdx = [3, 0], [3, 2]
    answer = ""

    for i in range(len(numbers)):
        tmp = [(k, l) for k in range(4) for l in range(3) if pad[k][l] == numbers[i]]

        if numbers[i] in left:
            answer += "L"
            idx = left.index(numbers[i])
            leftIdx = [idx, 0]

        elif numbers[i] in right:
            answer += "R"
            idx = right.index(numbers[i])
            rightIdx = [idx, 2]

        else:  # numbers[i] in mid 일 때
            if (abs(rightIdx[0] - tmp[0][0]) + abs(rightIdx[1] - tmp[0][1])) < (
                    abs(leftIdx[0] - tmp[0][0]) + abs(leftIdx[1] - tmp[0][1])):

                answer += "R"
                rightIdx = [tmp[0][0], tmp[0][1]]

            elif (abs(rightIdx[0] - tmp[0][0]) + abs(rightIdx[1] - tmp[0][1])) > (
                    abs(leftIdx[0] - tmp[0][0]) + abs(leftIdx[1] - tmp[0][1])):

                answer += "L"
                leftIdx = [tmp[0][0], tmp[0][1]]

            else:  # 둘의 값이 같을 경우

                if hand == "right":
                    answer += "R"
                    rightIdx = [tmp[0][0], tmp[0][1]]
                else:
                    answer += "L"
                    leftIdx = [tmp[0][0], tmp[0][1]]

    return answer