from heapq import heappush, heappop, heapify
def solution(scoville, K):
    heapify(scoville)
    answer = 0
    while True:
        min_sk = heappop(scoville)
        if len(scoville) == 0 and min_sk < K:
            return -1
        if min_sk >= K:
            break
        sec_min_sk = heappop(scoville)
        mixed_sk = min_sk + sec_min_sk * 2
        answer += 1
        heappush(scoville, mixed_sk)
    
    return answer