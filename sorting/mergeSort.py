"""
Implement merge sort using recursion
Time complexity O(n*log(n))
Space complexity O(n)
"""
import random


def merge(L, R):
    """
    :param L: sorted array of numbers
    :param R: sorted array of numbers
    :return: L and R merged into one
    """
    L = sorted(L)
    R = sorted(R)

    output = []

    while L or R:
        # If none of the two lists are empty
        if L and R:
            if L[0] > R[0]:
                num = R.pop(0)
            else:
                num = L.pop(0)
            output.append(num)
        else:
            if L:
                output += L
            else:
                output += R
            break
    return output


def split(array):
    """
    :param array: the array to be splitted into two
    :return: returns two arrays
    """
    mid = len(array) // 2
    L = array[:mid]
    R = array[mid:]
    return L, R


def merge_sort(array, split_min=20):
    # Stop recursive splitting if the array has less than split_min elements
    if array.__len__() >= split_min:
        L, R = split(array)
        L = merge_sort(L)
        R = merge_sort(R)
    else:
        L, R = split(array)
    output = merge(L, R)
    return output


if __name__ == '__main__':
    array = list(range(60))
    random.shuffle(array)
    sorted_a = merge_sort(array)

    assert sorted_a == sorted(array)

    print("Random : ", array)
    print("Sorted : ", sorted_a)
