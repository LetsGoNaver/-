n, m = map(int, input().split())

numbers = []
def bt(depth):
    if depth == m:
        print(*numbers)
        return
    for i in range(1,n+1):
        if i in numbers:
            continue
        numbers.append(i)
        bt(depth+1)
        numbers.pop()
bt(0)
