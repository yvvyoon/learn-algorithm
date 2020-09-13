from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)

    print(left_index, right_index)

    return right_index - left_index


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 5, 1, 0, 2, 5]

print(count_by_range(a, 4, 4))
print(count_by_range(sorted(a), 3, 9))
