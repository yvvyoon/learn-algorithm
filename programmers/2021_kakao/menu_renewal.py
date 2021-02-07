from itertools import combinations
from collections import Counter, defaultdict


def sort_orders(orders):
    sorted_orders = []

    for order in orders:
        temp_order = list(order)
        temp_order.sort()
        sorted_orders.append(''.join(temp_order))

    return sorted_orders


def count_orders(orders, course):
    most_orders = []

    for num in course:
        total_orders = []

        for order in orders:
            order_combinations = list(combinations(order, num))
            total_orders += order_combinations

        orders_count = Counter(total_orders).most_common()

        most_order = [''.join(
            key) for key, value in orders_count if value == orders_count[0][1] and value > 1]
        most_orders += most_order

    most_orders.sort()

    return most_orders


def solution(orders, course):
    sorted_orders = sort_orders(orders)
    count_result = count_orders(sorted_orders, course)

    return count_result
