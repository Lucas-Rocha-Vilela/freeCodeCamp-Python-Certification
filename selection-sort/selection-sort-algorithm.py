def selection_sort(list_of_items):
    if len(list_of_items) <= 1:
        return list_of_items

    j = 0
    for i in range(len(list_of_items)):
        minimum = list_of_items[j]
        min_index = j
        for index, value in enumerate(list_of_items[j:], j):
            if value < minimum:
                minimum = value
                min_index = index
        if(j != min_index):
            list_of_items[min_index] = list_of_items[j]
            list_of_items[j] = minimum
        j += 1
    
    return list_of_items

print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))


