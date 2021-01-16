def solution(clothes):
    answer = 1
    clothes_map = {}

    for cloth in clothes:
        if cloth[1] in clothes_map:
            clothes_map[cloth[1]] += 1
        else:
            clothes_map[cloth[1]] = 1

    for count in clothes_map.values():
        answer *= count + 1

    return answer - 1
