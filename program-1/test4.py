import random

from copilot_workshop import sort_linear_array

def test_sort_linear_array():
    # Test case 1: Empty array
    arr = []
    assert sort_linear_array(arr) == []
    
    # Test case 2: Array with one element
    arr = [42]
    assert sort_linear_array(arr) == [42]
    
    # Test case 3: Array with repeated elements
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert sort_linear_array(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    
    # Test case 4: Array with negative elements
    arr = [-3, 1, -4, 1, 5, -9, 2, 6, 5, -3, 5]
    assert sort_linear_array(arr) == [-9, -4, -3, -3, 1, 1, 2, 5, 5, 5, 6]
    
    # Test case 5: Array with 50,000 random elements
    arr = [random.randint(0, 1000) for _ in range(50000)]
    sorted_arr = sorted(arr)
    assert sort_linear_array(arr) == sorted_arr
    
    print("All test cases pass")
    
test_sort_linear_array()
