from collections import deque
def solution(priorities, location):
    process = deque([x for x in range(len(priorities))])
    queue = deque([])
    
    while process:
        if len(process) == 1:
            queue.append(process.popleft())
            break
        p = process.popleft()
        pPri = priorities[p]
        isPriority = False
        for e in process:
            if priorities[e] > pPri:
                process.append(p)
                isPriority = True
                break
        if isPriority:
            continue
        else:
            queue.append(p)
    print(queue)
    answer = 0
    for i in range(len(queue)):
        if queue[i] == location:
            answer = i+1
    return answer