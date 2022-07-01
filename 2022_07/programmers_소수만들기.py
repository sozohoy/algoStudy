from itertools import combinations

def solution(nums):
    answer = 0
    combinationList = list(combinations(nums, 3))
    sumList = []

    for i in range(len(combinationList)):
        sumList.append(sum(combinationList[i]))

    for i in range(len(sumList)):
        isPrime = True
        for j in range(2, sumList[i] - 1):
            if sumList[i] % j == 0:
                isPrime = False
                break
        if isPrime == True:
            answer += 1

    return answer