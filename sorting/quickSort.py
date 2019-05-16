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


def quick_sort(array, start=0, end=-1):
    """ Sort array using insertion sort """

    if len(array) == 1: return array

    start = 0
    end = len(array)
    pivot = random.randint(start, end)
    for i in range(start, end):
        if array[start] < array[end]:
            swap(array, start, end)

    # Recursively sort the smaller part
    if start != pivot: quick_sort(array, start, pivot)
    if end != pivot + 1: quick_sort(array, pivot, end)

    return array


if __name__ == '__main__':
    array = list(range(6))
    random.shuffle(array)

    print("Random : ", array)
    sorted_a = quick_sort(array)

    assert sorted_a == sorted(array)
    print("Sorted : ", sorted_a)
