""" Implement insertion sort """

import random


def insertion_sort(array):
    """ Sort array using insertion sort """

    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            # Swap until every item until i is sorted
            j = i + 1
            while j > 0:
                temp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = temp
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
