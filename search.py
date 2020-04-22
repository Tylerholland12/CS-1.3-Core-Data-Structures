def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
   
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    
    if index >= len(array):
        return None
    elif item == array[index]:
        return index
    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    
    return binary_search_recursive(array, item, 0, len(array) - 1)
   

def binary_search_iterative(array, item):
  
    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index: 

        middle_index = (right_index + left_index) // 2
        print("Middle index", middle_index)
        print("Left index", left_index)
        print("Right index", right_index)
        

        if array[middle_index] == item:
            print("item found")
            return middle_index

        elif item < array[middle_index]:
            right_index = middle_index - 1

        elif item > array[middle_index]:
            left_index = middle_index + 1


def binary_search_recursive(array, item, left=None, right=None):
    #Is the middle item what we are looking for?
    if left <= right:
        middle = (right + left) // 2
        if array[middle] < item:
            return binary_search_recursive(array, item, middle + 1, right)
        elif array[middle] > item:
            return binary_search_recursive(array, item, left, middle - 1)
        else:
            return middle