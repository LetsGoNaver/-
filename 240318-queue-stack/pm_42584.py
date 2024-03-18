from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        p = prices.popleft()
        time = 0
        if len(prices) == 0:
            answer.append(time)
            break
        for price in prices:
            if price < p:
                time += 1
                break
            else:
                time += 1
        answer.append(time)
                
            
    
    return answer