def fibonacci(n):
    sequence = [0, 1]
    if n < 0:
        raise ValueError('The number must be a positive integer')
    
    for number in range(2, n + 1):
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence[n]


