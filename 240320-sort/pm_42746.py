from functools import cmp_to_key
def cmp_key(x, y):
    if x + y > y + x:
        return -1
    else:
        return 1

def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key = cmp_to_key(cmp_key))
    if sum(numbers) == 0:
        return "0"
    return "".join(str_numbers)