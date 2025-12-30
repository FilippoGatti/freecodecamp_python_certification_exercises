def helper(value, tolerance, iterations):
    if value > 1:
        low = 1
        high = value
    else:
        low = value
        high = 1
    
    while iterations > 0:
        iterations -= 1
        mid = (low + high) / 2

        if mid ** 2 > value:
            high = mid
        else:
            low = mid

        if high - low < tolerance:
            return mid
        
    return None


def square_root_bisection(value, tolerance=1e-5, iterations=100):
    if value < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if value == 0 or value == 1:
        print(f"The square root of {value} is {value}")
        return value
    
    root = helper(value, tolerance, iterations)

    if root is None:
        print(f"Failed to converge within {iterations} iterations")
    else:
        print(f"The square root of {value} is approximately {root}")
    
    return root
