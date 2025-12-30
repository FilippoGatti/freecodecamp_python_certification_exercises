def selection_sort(array):
    for i in range(len(array)):
        min_value = min(array[i:])
        min_index = array[i:].index(min_value)
        array[min_index + i] = array[i]
        array[i] = min_value
    return array
