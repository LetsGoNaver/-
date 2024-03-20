import heapq
def solution(operations):
    h = []
    heapq.heapify(h)
    for op in operations:
        cmd, num = op.split(" ")
        num = int(num)
        if cmd == "I":
            heapq.heappush(h, num)
        elif cmd == "D":
            if len(h) == 0:
                continue
            if num == -1:
                heapq.heappop(h)
            elif num == 1:
                h.pop()
    if len(h) == 0:
        return [0,0]    
    return [max(h), min(h)]