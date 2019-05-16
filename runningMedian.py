import heapq
import random
from bisect import bisect_left
import time

random.seed(1)


def timeit(method):
    """
    A decorator used for time profiling functions and methods
    :param method:
    :return: time in ms for a method
    """

    def timed(*args, **kwargs):
        timeStart = time.time()
        result = method(*args, **kwargs)
        timeEnd = time.time()

        if 'log_time' in kwargs:
            name = kwargs.get('log_name', method.__name__.upper())
            kwargs['log_time'][name] = int((timeEnd - timeStart) * 1000)
        else:
            print('%r %2.2f ms' % (method.__name__, int(timeEnd - timeStart) * 1000))
        return result

    return timed


def push_pop(arr, oldItem, newItem):
    arr.pop(arr.index(oldItem))
    index = bisect_left(arr, newItem)
    arr.insert(index, newItem)
    return arr


@timeit
def running_median(arr, k):
    s = sorted(arr[:k])

    medians = []
    median = s[(k - 1) // 2]
    medians.append(median)

    for i in range(len(arr) - k):
        newItem = arr[i + k]
        oldItem = arr[i]
        s = push_pop(s, oldItem, newItem)

        median = s[(k - 1) // 2]
        medians.append(median)
    return medians


@timeit
def brute_force(arr, k):
    medians = []
    for i in range(len(arr) - k + 1):
        s = sorted(arr[i:i + k])
        median = s[(k - 1) // 2]
        medians.append(median)
    return medians


@timeit
def running_median_2(arr, k):
    n1, n2 = arr[0], arr[1]
    min_heap = [n1 if n1 > n2 else n2]
    max_heap = [n2 if n1 < n2 else n1]

    medians = []
    for i, num in enumerate(arr[2:]):
        # Compute median
        if (i + 1) % 2 == 0:
            median = (min_heap[0] + max_heap[0]) / 2

        else:
            if len(min_heap) > len(max_heap):
                median = min_heap[0]
            else:
                median = max_heap[0]
        medians.append(median)

        # Insert item into one of the heaps and heapify
        if num > median:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappush(max_heap, num)

        # Balance the number of items in either heaps
        if abs(len(min_heap) - len(max_heap)) > 1:
            if len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, heapq.heappop(min_heap))
            else:
                heapq.heappush(min_heap, heapq.heappop(max_heap))

        heapq._heapify_max(max_heap)
        print("Min : {}\nMax : {}\nArr : {}\nMed : {}\n".format(min_heap, max_heap, sorted(arr[:2+i+1]), median))
    print(medians)


if __name__ == '__main__':
    n = 40000
    k = 4001
    arr = list(range(n))
    random.shuffle(arr)
    m1 = brute_force(arr, k)
    m2 = running_median(arr, k)
    assert m1 == m2

