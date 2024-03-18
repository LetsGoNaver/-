from collections import deque
def solution(s):
    bucket = deque(s)
    stack = []
    while bucket:
        bk = bucket.popleft()
        if bk == "(":
            stack.append(bk)
        elif bk == ")":
            if stack:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(bk)
            else:
                stack.append(bk)
    if len(stack) == 0: 
        return True
    else:
        return False