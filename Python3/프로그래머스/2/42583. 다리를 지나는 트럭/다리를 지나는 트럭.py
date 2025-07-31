from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_queue = deque(truck_weights)
    total_weight = 0 

    while bridge:
        answer += 1
        total_weight -= bridge.popleft()

        if truck_queue:
            if total_weight + truck_queue[0] <= weight:
                truck = truck_queue.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)  
    return answer