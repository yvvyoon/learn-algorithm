def solution(phone_book):
    if len(phone_book) < 1 or len(phone_book) > 1000000:
        return

    phone_book.sort()

    for first, second in zip(phone_book, phone_book[1:]):
        if second.startswith(first):
            return False

    return True
