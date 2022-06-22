def binarySearch(element, array):
    startIndex = 0
    endIndex = len(array) - 1

    while startIndex <= endIndex:

        midIndex = (startIndex + endIndex) // 2

        if element == array[midIndex]:
            return midIndex

        elif element < array[midIndex]:
            endIndex = midIndex - 1

        else:
            startIndex = midIndex + 1

    return None
