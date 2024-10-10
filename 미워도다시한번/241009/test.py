from collections import deque
def solution(stones, k):
    stones = [(i-1, i+1, stones[i]) for i in range(len(stones))]
    answer = 0
    
    q = deque()
    q.append(0)
    while q:
        i = q.popleft()
        ni = stones[i][1]
        while stones[ni][2] != 0 and ni < len(stones):
            ni = stones[ni][1]
        if ni - i >= k:
            return answer
        stones[i][2] -= 1
        if ni == len(stones):
            answer += 1
            q.append(0)
        else:
            q.append(ni)
            
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))
