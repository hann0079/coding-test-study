from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()
    
    # 각 작업이 완료되기까지 필요한 일수를 미리 계산
    for p, s in zip(progresses, speeds):
        days.append(-((p - 100) // s))  # 올림 효과를 위해 음수 사용
    
    while days:
        count = 1
        current = days.popleft()
        
        while days and days[0] <= current:
            days.popleft()
            count += 1
        
        answer.append(count)
    
    return answer