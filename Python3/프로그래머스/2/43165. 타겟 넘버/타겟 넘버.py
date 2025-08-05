from collections import deque

def bfs(numbers, target):
    answer = 0
    q = deque()
    q.append((0,0))
    
    while q:
        cur_sum, idx = q.popleft()
        
        if idx == len(numbers):
            if cur_sum == target:
                answer += 1
            continue
        
        q.append((cur_sum + numbers[idx], idx + 1))
        
        q.append((cur_sum - numbers[idx], idx + 1))
        
    return answer
    
def solution(numbers, target):
    return bfs(numbers, target)