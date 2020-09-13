import heapq

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)

    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result

def heapsort_reverse(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)

    for i in range(len(h)):
        result.append(-heapq.heappop(h))

    return result

result = heapsort([1, 3, 4, 67, 9, 4, 2, 6, 8, 10])
result_reverse = heapsort_reverse([1, 3, 4, 67, 9, 4, 2, 6, 8, 10])
print(result)
print(result_reverse)