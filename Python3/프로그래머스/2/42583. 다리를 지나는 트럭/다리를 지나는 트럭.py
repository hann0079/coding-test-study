from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque()  # (트럭 무게, 진입 시각) 튜플을 저장
    truck_queue = deque(truck_weights)
    time = 0
    
    while truck_queue or bridge:
        time += 1
        
        # 다리를 건넌 트럭을 뺀다
        if bridge and time - bridge[0][1] >= bridge_length:
            bridge.popleft()
        
        # 다리에 새 트럭을 올릴 수 있는지 확인
        if truck_queue:
            # 현재 다리 위의 무게를 계산
            current_weight = sum(t[0] for t in bridge)
            
            if current_weight + truck_queue[0] <= weight and len(bridge) < bridge_length:
                new_truck = truck_queue.popleft()
                bridge.append((new_truck, time))
                
    return time