def quick_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted
    pivot = unsorted[0]
    less_p = []
    equal_p = []
    greater_p = []

    for number in unsorted:
        if number == pivot:
            equal_p.append(number)
        elif number < pivot:
            less_p.append(number)
        else:
            greater_p.append(number)

    less_p = quick_sort(less_p)
    greater_p = quick_sort(greater_p)
    less_p.extend(equal_p)
    less_p.extend(greater_p)
    return less_p


#print(quick_sort([4, 42, 16, 23, 15, 8]))


