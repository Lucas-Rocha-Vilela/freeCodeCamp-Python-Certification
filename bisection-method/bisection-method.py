def square_root_bisection(number, tolerance=1e-3, maximum=50):
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if number == 0 or number == 1:
        print(f'The square root of {number} is {number}')
        return number

    i = 0
    if number > 1:
        low = 0
        high = number
    else:
        low = number
        high = 1
        
    while high > low and i < maximum:
        mid = (low + high) / 2
        if mid ** 2 == number:
            break
        elif mid ** 2 > number:
            high = mid - tolerance
        else:
            low = mid + tolerance
        print(mid, (high - low)/2)
        i += 1

    if i < maximum:
        print(f'The square root of {number} is approximately {mid}')
        return mid

    print(f'Failed to converge within {maximum} iterations')
    return None

square_root_bisection(225, 1e-7, 10)

