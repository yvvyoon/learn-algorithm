import re


def change_to_lower(id):
    return id.lower()


def delete_char(id):
    return re.sub('[^0-9a-z-_.]', '', id)


def replace_dot(id):
    for _ in range(len(id)):
        if '.'*2 in id:
            id = id.replace('.'*2, '.')

    return id


def strip_dot(id):
    return id.lstrip('.').rstrip('.')


def replace_space(id):
    if not id:
        return 'a'

    return id


def maintain_fifteen_strings(id):
    if len(id) > 15:
        id = id[:15]

        if id[0] == '.' or id[-1] == '.':
            id = strip_dot(id)

    return id


def repeat_to_three_strings(id):
    if len(id) < 3:
        id += id[-1] * (3 - len(id))

        return id

    return id


def solution(new_id):
    answer = change_to_lower(new_id)
    answer = delete_char(answer)
    answer = replace_dot(answer)
    answer = strip_dot(answer)
    answer = replace_space(answer)
    answer = maintain_fifteen_strings(answer)
    answer = repeat_to_three_strings(answer)

    return answer
