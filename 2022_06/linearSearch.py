def linearSearch(element, array):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return None