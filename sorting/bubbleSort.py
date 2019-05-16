"""
Implement bubble sort : if two adjacent items are not sorted, swap them.
Time complexity O(n*n)
Space complexity O(n)
"""

import random


def swap(array, pos1, pos2):
    temp = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = temp


def bubble_sort(array):
    """ Sort array using insertion sort """

    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j + 1] < array[j]:
                # Swap two items
                swap(array, j, j + 1)
    return array


if __name__ == '__main__':
    array = list(range(60))
    random.shuffle(array)

    print("Random : ", array)
    sorted_a = bubble_sort(array)

    assert sorted_a == sorted(array)
    print("Sorted : ", sorted_a)
