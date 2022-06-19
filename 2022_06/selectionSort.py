array = [8,4,6,2,9,1,3,7,5]


## O(n^2)
def selectionSort(array):
    n = len(array)
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if array[minIndex] > array[j]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
        print(array)

selectionSort(array)