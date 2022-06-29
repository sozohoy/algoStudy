def solution(s):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in range(10):
        print(s.find(numbers[i]))
        if s.find(numbers[i]) != -1:
            s = s.replace(numbers[i], str(i))

    print(s)
    answer = int(s)
    return answer