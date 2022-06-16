array = [8,4,6,2,9,1,3,7,5]

def insertionSort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i, 0, -1):
            print(j)
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
        print(array[:i+1])


insertionSort(array)