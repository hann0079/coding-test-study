from heapq import heapify, heappop, heappush

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while len(scoville) > 1:
        first = heappop(scoville)
        
        if first < K:
            answer += 1
            second = heappop(scoville)
            heappush(scoville, first + (second * 2))
        else:
            break
    
    return -1 if scoville[0] < K else answer