def sort_linear_array(arr):
    """
    Sorts the given array of numbers in ascending order using the quicksort algorithm.
    Returns the sorted array.
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    
    for num in arr[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    
    return sort_linear_array(left) + [pivot] + sort_linear_array(right)
