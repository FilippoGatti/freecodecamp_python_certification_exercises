def verify_card_number(digits: str) -> str:
    double_array = []
    summed_array = []

    if ' ' in digits:
        array = digits.replace(' ','')[::-1]
    elif '-' in digits:
        array = digits.replace('-','')[::-1]
    else:
        array = digits[::-1]

    for index, el in enumerate(array):
        if (index + 1) % 2 == 0:
            double_array.append(int(el) * 2)
        else:
            double_array.append(int(el))
    
    for num in double_array:
        if num >= 10:
            d = num // 10
            u = num - (d * 10)
            summed_array.append(d + u)
        else:
            summed_array.append(num)

    value = sum(summed_array)
    
    if value % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'
