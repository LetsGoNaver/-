from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([ 0 for x in range(bridge_length)])
    truck_weights = deque(truck_weights)
    bridge_weight = 0
    answer = 0
    
    while truck_weights:
        truck = truck_weights.popleft()
        bridge_weight -= bridge.pop()
        if bridge_weight + truck <= weight:
            bridge.appendleft(truck)
            bridge_weight += truck
            answer += 1
        else:
            bridge.appendleft(0)
            truck_weights.appendleft(truck)
            answer += 1
        
    return answer + bridge_length