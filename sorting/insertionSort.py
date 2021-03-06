"""
Implement insertion sort
Time complexity O(n*n)
Space complexity O(n)
"""
import random


def swap(array, pos1, pos2):
    temp = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = temp

def insertion_sort(array):
    """ Sort array using insertion sort """

    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            # Swap until every item until i is sorted
            j = i + 1
            while j > 0:
                swap(array, j, j - 1)
                j -= 1
                if array[j] > array[j - 1]:
                    break

    return array


if __name__ == '__main__':
    array = list(range(60))
    random.shuffle(array)
    sorted_a = insertion_sort(array)

    assert sorted_a == sorted(array)

    print("Random : ", array)
    print("Sorted : ", sorted_a)
