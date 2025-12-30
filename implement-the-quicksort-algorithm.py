def quick_sort(array: list) -> list:
    sorted_array = []
    
    if len(array) <= 1:
        return array

    pivot = array[0]
    smaller, equal, bigger = [], [], []

    for el in array:
        if el < pivot:
            smaller.append(el)
        elif el == pivot:
            equal.append(el)
        else:
            bigger.append(el)

    #print('small:', smaller, '\nmedium:', equal, '\nbig:', bigger, '\n')

    sorted_smaller = quick_sort(smaller)
    sorted_bigger = quick_sort(bigger)

    sorted_array = sorted_smaller + equal + sorted_bigger

    return sorted_array

