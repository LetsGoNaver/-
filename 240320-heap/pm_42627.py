import heapq
def solution(jobs):
    index, cursor, runtime = 0, 0, 0
    latest = - 1
    h = []
    heapq.heapify(h)
    while index < len(jobs):
        for job in jobs:
            if latest < job[0] <= cursor:
                heapq.heappush(h, (job[1], job[0]))
        if len(h) > 0:
            job = heapq.heappop(h)
            latest = cursor
            cursor += job[0]
            runtime += cursor - job[1]
            index += 1
        else:
            cursor += 1
    return runtime // len(jobs)