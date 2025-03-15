from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses :
        cnt = 0
        while progresses and progresses[0] >= 100:
            cnt+=1
            progresses.popleft()
            speeds.popleft()
        progresses = deque([progresses[i]+speeds[i] for i in range(len(progresses))])
        if cnt:
            answer.append(cnt)
    
    return answer